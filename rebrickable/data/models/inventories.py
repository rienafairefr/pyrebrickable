from sqlalchemy import Integer, Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Inventory(Base):
    """
    an inventory is a collection with multiple sets in it
    it also links a set with a collection of parts
    """
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    set_num = Column(String, ForeignKey('sets.set_num'))

    parts = relationship("InventoryPart", backref='inventories')
    sets = relationship('InventorySet', backref='inventories')


class InventoryPart(Base):
    """ Parts content of set """
    __tablename__ = 'inventory_parts'

    inv_part_id = Column(Integer, primary_key=True, autoincrement=True)

    inventory_id = Column(  Integer, ForeignKey('inventories.id'))
    part_num = Column(String, ForeignKey('parts.part_num'))
    color_id = Column(Integer, ForeignKey('colors.id'))
    quantity = Column(Integer, default=1)
    is_spare = Column(Boolean, default=False)

    color = relationship('Color')
    part = relationship('Part')


class InventorySet(Base):
    __tablename__ = 'inventory_sets'

    id = Column(Integer, primary_key=True, autoincrement=True)

    inventory_id = Column(Integer, ForeignKey('inventories.id'))
    set_num = Column(String, ForeignKey('sets.set_num'))
    quantity = Column(Integer)

    set = relationship('Set')