from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from rebrickable_data.models import Base

class Theme(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer)