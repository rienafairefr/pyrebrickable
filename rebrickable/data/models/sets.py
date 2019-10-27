from sqlalchemy import Integer, Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from rebrickable.data.models import Base, InventorySet


class Set(Base):
    __tablename__ = 'sets'
    set_num = Column(String, primary_key=True)
    name = Column(String)
    year = Column(Integer)
    theme_id = Column(Integer, ForeignKey('themes.id'))
    num_parts = Column(Integer)

    theme = relationship('Theme')
    inventories = relationship('Inventory')
