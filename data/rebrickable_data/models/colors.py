from sqlalchemy import Integer, Column, String, Boolean

from rebrickable_data.models import Base


class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rgb = Column(String)
    is_trans = Column(Boolean)

    def __repr__(self):
        return '<Color %s>' % self.name
