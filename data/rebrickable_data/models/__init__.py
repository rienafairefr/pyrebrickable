import rebrickable_api
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from rebrickable_data.models.colors import *
from rebrickable_data.models.inventories import *
from rebrickable_data.models.mocs import *
from rebrickable_data.models.parts import *
from rebrickable_data.models.sets import *
from rebrickable_data.models.themes import *


class Badge(Base):
    __tablename__ = 'badges'

    id = Column(Integer)
    code = Column(String)
    descr = Column(String)
    level = Column(Integer)
    name = Column(String)

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rgb = Column(String)
    is_trans = Column(Boolean)
    external_ids = Column(JSON)

    def __repr__(self):
        return '<Color %s>' % self.name