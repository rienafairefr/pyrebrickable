from . import Base
from sqlalchemy import String, Column, Integer


class Moc(Base):
    """
        data for a Moc
    """
    __tablename__ = 'mocs'

    set_num = Column(String, primary_key=True)

    designer_name = Column(String)
    designer_url = Column(String)
    moc_img_url = Column(String)
    moc_url = Column(String)
    name = Column(String)
    num_parts = Column(Integer)
    theme_id = Column(Integer)
    year = Column(Integer)

    @property
    def absent(self):
        return self.moc_url is None
