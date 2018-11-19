import time
import random

from rebrickable_api import LegoApi
from rebrickable_api.rest import ApiException
from rebrickable_cli.cli.main import get_api_client
from rebrickable_data.database import Session, engine
from rebrickable_data.models import Base, Moc, InventoryPart, Inventory, Color, Part

client = get_api_client()

api = LegoApi(client)

metadata = Base.metadata

metadata.create_all(engine)

session = Session()

ids = list(range(1000, 20000))
random.shuffle(ids)

for i in ids:
    moc = 'MOC-%i' % i
    print(moc)
    try:
        if session.query(Moc).get(moc):
            continue
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
        session.add(moc_data)
        session.add(inventory)
        session.commit()
    except ApiException, e:
        if e.status != 404:
            pass
        pass

    time.sleep(0.5)
