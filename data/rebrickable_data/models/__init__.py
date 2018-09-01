from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from rebrickable_data.models.colors import *
from rebrickable_data.models.inventories import *
from rebrickable_data.models.parts import *
from rebrickable_data.models.sets import *
from rebrickable_data.models.themes import *
