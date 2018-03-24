import csv
import os

from sqlalchemy import inspect, Table

from rebrickable_data.models import Base
from rebrickable_data.utils import data_dir, data_files
from rebrickable_data.database import db_url, engine, Session


def get_class_by_tablename(tablename):
    """Return class reference mapped to table.

    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in Base._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c
    return Base.metadata.tables.get(tablename)


def import_main():
    print('')
    metadata = Base.metadata

    metadata.create_all(engine)

    # create a Session
    session = Session()

    for data_file in data_files:
        print('Importing %s ... ' % data_file, end='')

        model_type = get_class_by_tablename(data_file)

        assert model_type is not None

        if session.query(model_type).first():
            print('There is already data in %s, not importing.' % data_file)
            continue

        csv_path = os.path.join(data_dir, data_file+'.csv')
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            objects = list(reader)

            print(' %i rows ...' % len(objects), end='')

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


if __name__ == '__main__':
    import_main()
