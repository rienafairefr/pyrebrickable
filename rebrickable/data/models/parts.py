from sqlalchemy import Integer, Column, String, ForeignKey, Table, func, select, and_
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from rebrickable.data.models import Base


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

    @hybrid_property
    def has_variants(self):
        return any(self.printed_variants) or \
               any(self.alt_variants) or \
               any(self.mold_variants) or \
               any(self.patterned_variants)

    @has_variants.expression
    def has_variants(cls):
        return (
            select([func.count(PartRelationship.c.parent_part_num)])
                .where(PartRelationship.c.parent_part_num == cls.part_num)
                .label('has_variants')
        )

    variants = relationship('Part',
                            secondary=PartRelationship,
                            primaryjoin=PartRelationship.c.parent_part_num == part_num,
                            secondaryjoin=PartRelationship.c.child_part_num == part_num,
                            foreign_keys=[PartRelationship.c.child_part_num,
                                          PartRelationship.c.parent_part_num])

    printed_variants = relationship('Part',
                                    secondary=PartRelationship,
                                    primaryjoin=and_(PartRelationship.c.parent_part_num == part_num,
                                                     PartRelationship.c.rel_type == 'P'),
                                    secondaryjoin=PartRelationship.c.child_part_num == part_num,
                                    foreign_keys=[PartRelationship.c.child_part_num,
                                                  PartRelationship.c.parent_part_num])

    alt_variants = relationship('Part',
                                secondary=PartRelationship,
                                primaryjoin=and_(PartRelationship.c.parent_part_num == part_num,
                                                 PartRelationship.c.rel_type == 'A'),
                                secondaryjoin=PartRelationship.c.child_part_num == part_num,
                                foreign_keys=[PartRelationship.c.child_part_num,
                                              PartRelationship.c.parent_part_num])

    mold_variants = relationship('Part',
                                 secondary=PartRelationship,
                                 primaryjoin=and_(PartRelationship.c.parent_part_num == part_num,
                                                  PartRelationship.c.rel_type == 'M'),
                                 secondaryjoin=PartRelationship.c.child_part_num == part_num,
                                 foreign_keys=[PartRelationship.c.child_part_num,
                                               PartRelationship.c.parent_part_num])

    patterned_variants = relationship('Part',
                                      secondary=PartRelationship,
                                      primaryjoin=and_(PartRelationship.c.parent_part_num == part_num,
                                                       PartRelationship.c.rel_type == 'T'),
                                      secondaryjoin=PartRelationship.c.child_part_num == part_num,
                                      foreign_keys=[PartRelationship.c.child_part_num,
                                                    PartRelationship.c.parent_part_num])

    def __repr__(self):
        return '<Part %s %s>' % (self.part_num, self.name)
