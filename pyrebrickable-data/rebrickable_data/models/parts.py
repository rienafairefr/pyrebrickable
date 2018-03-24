from _operator import and_

from sqlalchemy import Integer, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from rebrickable_data.models import Base


class PartCategory(Base):
    __tablename__ = 'part_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)


PartRelationship = Table('part_relationships', Base.metadata,
                         Column('rel_type', String),
                         Column('child_part_num', String, ForeignKey('parts.part_num')),
                         Column('parent_part_num', String, ForeignKey('parts.part_num'))
                         )


class Part(Base):
    __tablename__ = 'parts'

    part_num = Column(String, primary_key=True)
    name = Column(String)
    part_cat_id = Column(Integer, ForeignKey('part_categories.id'))

    category = relationship('PartCategory')
    printed_variants = relationship('Part',
                                    secondary=PartRelationship,
                                    primaryjoin=and_(PartRelationship.c.parent_part_num == part_num,
                                                     PartRelationship.c.rel_type == 'P'),
                                    secondaryjoin=PartRelationship.c.child_part_num == part_num,
                                    foreign_keys=[PartRelationship.c.child_part_num,
                                                  PartRelationship.c.parent_part_num])

    printed_variant_of = relationship('Part',
                                      secondary=PartRelationship,
                                      primaryjoin=and_(PartRelationship.c.child_part_num == part_num,
                                                       PartRelationship.c.rel_type == 'P'),
                                      secondaryjoin=PartRelationship.c.parent_part_num == part_num,
                                      foreign_keys=[PartRelationship.c.child_part_num,
                                                    PartRelationship.c.parent_part_num],
                                      uselist=False)

    def __repr__(self):
        return '<Part %s %s>' % (self.part_num, self.name)
