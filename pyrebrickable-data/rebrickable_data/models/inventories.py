from sqlalchemy import Integer, Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from rebrickable_data.models import Base


class Inventory(Base):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    set_num = Column(String, ForeignKey('sets.set_num'))

    parts = relationship("InventoryPart")
    sets = relationship("InventorySet")


class InventoryPart(Base):
    __tablename__ = 'inventory_parts'

    id = Column(Integer, primary_key=True, autoincrement=True)

    inventory_id = Column(Integer, ForeignKey('inventories.id'))
    part_num = Column(String, ForeignKey('parts.part_num'))
    color_id = Column(Integer, ForeignKey('colors.id'))
    quantity = Column(Integer)
    is_spare = Column(Boolean)

    color = relationship('Color')


class InventorySet(Base):
    __tablename__ = 'inventory_sets'

    id = Column(Integer, primary_key=True, autoincrement=True)

    inventory_id = Column(Integer, ForeignKey('inventories.id'))
    set_num = Column(String, ForeignKey('sets.set_num'))
    quantity = Column(Integer)
