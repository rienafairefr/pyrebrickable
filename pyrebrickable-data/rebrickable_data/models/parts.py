from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from rebrickable_data.models import Base


class PartCategory(Base):
    __tablename__ = 'part_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class PartRelationship(Base):
    __tablename__ = 'part_relationships'

    id = Column(Integer, primary_key=True, autoincrement=True)

    rel_type = Column(String)
    child_part_num = Column(String)
    parent_part_num = Column(String)


class Part(Base):
    __tablename__ = 'parts'

    part_num = Column(String, primary_key=True)
    name = Column(String)
    part_cat_id = Column(Integer, ForeignKey('part_categories.id'))

    category = relationship('PartCategory')
