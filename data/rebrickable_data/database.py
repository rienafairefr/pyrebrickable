import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rebrickable_data.utils import data_dir

db_path = os.path.join(data_dir, 'rebrickable.db')
db_url = 'sqlite:///%s' % db_path
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)