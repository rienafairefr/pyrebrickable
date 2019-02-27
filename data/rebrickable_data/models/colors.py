from rebrickable_data.models import Base
from sqlalchemy import Integer, Column, String, Boolean, JSON


class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rgb = Column(String)
    is_trans = Column(Boolean)
    external_ids = Column(JSON)

    def __repr__(self):
        return '<Color %s>' % self.name

