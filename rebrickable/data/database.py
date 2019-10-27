import os

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base
from .utils import data_dir

db_path = os.path.join(data_dir, 'rebrickable.db')
db_url = 'sqlite:///%s' % db_path
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)


@click.command(name='reset-db')
def reset_db_main():


    metadata = Base.metadata

    print('Deleting all tables ... ')
    metadata.drop_all(engine)

    print('Creating all tables ... ')
    metadata.create_all(engine)
