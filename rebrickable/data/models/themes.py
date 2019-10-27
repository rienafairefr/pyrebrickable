from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Theme(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('themes.id'), nullable=True)
    parent = relationship('Theme', backref='children', uselist=False, remote_side=[id])

    def __repr__(self):
        if self.parent is None:
            return '<Theme ' +self.name
        else:
            return '%s.%s>' % (self.parent, self.name)
