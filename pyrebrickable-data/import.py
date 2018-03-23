import csv
import glob

import os

from progress.bar import Bar
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
from rebrickable_data.models import Base
from rebrickable_data.models.colors import *
from rebrickable_data.models.inventories import *
from rebrickable_data.models.parts import *
from rebrickable_data.models.sets import *
from rebrickable_data.models.themes import *

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
    metadata = Base.metadata

    metadata.create_all(engine)

    # create a Session
    session = Session()

    elements = [
            ('colors', Color),
        ]

    csv_paths = glob.glob('*.csv')

    for csv_path in csv_paths:
        context = {'items': []}

        tablename,_ = os.path.splitext(csv_path)
        model_type = get_class_by_tablename(tablename)

        assert model_type is not None

        objects = []

        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

            bar = Bar('Importing %s ...' % csv_path, max=len(rows))

            for row in rows:
                item = {}
                for k,v in row.items():
                    if v is None:
                        continue
                    elif k.startswith('is_'):
                        item[k] = v == 't'
                    else:
                        item[k] = v

                objects.append(model_type(**item))
                bar.next()

        session.bulk_save_objects(objects)

        session.commit()
        bar.finish()


if __name__ == '__main__':
    import_main()