import csv
import os

import click
from sqlalchemy import Table

from rebrickable_data.models import Base
from rebrickable_data.utils import data_dir, data_mapping
from rebrickable_data.database import engine, Session, db_path


@click.command(name='import')
@click.option('--force', is_flag=True, help='force to overwrite existing data in the database')
def import_main(force=False):
    print('database path %s' % db_path)
    metadata = Base.metadata

    metadata.create_all(engine)

    not_overwriting = False
    # create a Session
    session = Session()

    if force:
        print('Deleting all tables ... ')
        metadata.drop_all(engine)
        metadata.create_all(engine)

    for data_file in data_mapping:

        model_type = data_mapping[data_file]

        assert model_type is not None

        if session.query(model_type).first() and not force:
            not_overwriting = True
            continue

        print('Importing %s ... ' % data_file, end= '')

        csv_path = os.path.join(data_dir, data_file+'.csv')
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            objects = list(reader)

            print(' %i rows ... ' % len(objects), end= '')

            for k in reader.fieldnames:
                if k.startswith('is_'):
                    for row in objects:
                        row[k] = row[k] == 't'

        if isinstance(model_type, Table):
            ins = model_type.insert(objects)
            conn = engine.connect()
            conn.execute(ins)
        else:
            session.bulk_insert_mappings(model_type, objects)

        session.commit()
        print('ok')
    if not_overwriting:
        print('Not re-importing on existing data, add --force if that''s what you want')
