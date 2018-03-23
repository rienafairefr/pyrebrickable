import csv
import glob
import os

from progress.bar import Bar
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rebrickable_data.models import Base

engine = create_engine('sqlite:///rebrickable.db')

# create a configured "Session" class
Session = sessionmaker(bind=engine)


def get_class_by_tablename(tablename):
    """Return class reference mapped to table.

    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in Base._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c


def import_main():
    print('')
    metadata = Base.metadata

    metadata.create_all(engine)

    # create a Session
    session = Session()

    csv_paths = glob.glob('*.csv')

    for csv_path in csv_paths:
        print('Importing %s ... ' % csv_path, end='')

        tablename, _ = os.path.splitext(csv_path)
        model_type = get_class_by_tablename(tablename)

        assert model_type is not None

        objects = []
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            objects = list(reader)

            print(' %i rows ...' % len(objects), end='')

            for k in reader.fieldnames:
                if k.startswith('is_'):
                    for row in objects:
                        row[k] = row[k] == 't'

        session.bulk_insert_mappings(model_type, objects)

        session.commit()
        print('ok')


if __name__ == '__main__':
    import_main()
