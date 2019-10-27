from __future__ import print_function
import time

import click

from rebrickable.api import LegoApi
from rebrickable.api.rest import ApiException
from rebrickable.cli.common import pass_state
from rebrickable.data.database import Session, engine
from rebrickable.data.models import Base, Moc, InventoryPart, Inventory, Color, Part


# the smallest number MOC
MOC_MIN = 1000


def is_moc_absent(api, i):
    # we can get a few 404 for deleted mocs, only declare not found if all not found +/-10
    around = range(i - 10, i + 10)
    mocs_found = []
    for i in around:
        moc = get_moc(api, i)
        mocs_found.append(not moc.absent)
    if any(mocs_found):
        return False
    else:
        return True


def get_max(api, erase=False):
    session = Session()
    if erase:
        # reset the not found
        session.query(Moc).filter(Moc.moc_url.is_(None)).delete()
        session.commit()

    MOC_MAX = MOC_MIN
    for moc in session.query(Moc):
        i = int(moc.set_num[4:])
        if i > MOC_MAX:
            MOC_MAX = i

    i = MOC_MAX

    while True:
        # geometrical growing
        if is_moc_absent(api, i):
            break
        i = i * 2
        time.sleep(0.1)

    # now we bisect
    i0 = MOC_MIN  # found
    i1 = i  # not found

    while True:
        if i1-i0 == 1:
            break
        i = int((i0 + i1) / 2)
        if is_moc_absent(api, i):
            i1 = i
        else:
            i0 = i
        print('%i %i' % (i0, i1))

    print('MOC_MAX %i' % i0)
    return i0


def get_moc(api, i):
    session = Session()

    moc = 'MOC-%i' % i
    print('getting %s... ' % moc, end='')
    try:
        moc_data = session.query(Moc).get(moc)
        if moc_data:
            print(' in database')
            return moc_data
        moc_data = Moc(**api.lego_mocs_read(moc).to_dict())
        mocs_parts_list = api.lego_mocs_parts_list(moc_data.set_num)

        inventory = Inventory(set_num=moc_data.set_num)

        for inventory_part in mocs_parts_list.results:
            inventory_part_dict = inventory_part.to_dict()
            inventory_part_dict.pop('inv_part_id')
            inventory_part_dict.pop('id')

            color = inventory_part_dict.pop('color')
            color.pop('external_ids')
            db_color = session.query(Color).get(color['id'])
            inventory_part_dict['color'] = db_color
            part = inventory_part_dict.pop('part')
            db_part = session.query(Part).get(part['part_num'])
            inventory_part_dict['part'] = db_part

            inventory.parts.append(InventoryPart(**inventory_part_dict))
            session.add(inventory)
        print(' ok')
    except ApiException as e:
        # insert a -not-found- null value
        moc_data = Moc(set_num=moc)
        print(' absent')

    session.add(moc_data)
    session.commit()
    return moc_data


@click.command(name='download-extra')
@pass_state
def download_extra_main(state):
    client = state.client

    api = LegoApi(client)

    metadata = Base.metadata

    metadata.create_all(engine)

    MOC_MAX = get_max(api, erase=False)

    ids = list(range(MOC_MIN, MOC_MAX))
    for i in ids:
        get_moc(api, i)

        time.sleep(0.1)
