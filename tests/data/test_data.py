import pytest
from sqlalchemy import create_engine

from rebrickable.data.database import Session
from rebrickable.data.models import *

models = [Color, Inventory, InventorySet,
          InventoryPart, Part, PartCategory, Set, Theme]


@pytest.fixture(scope='module')
def session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session.configure(bind=engine)
    # You probably need to create some tables and
    # load some test data, do so here.

    # To create tables, you typically do:
    Base.metadata.create_all(engine)
    yield Session()
    Session.close_all()


@pytest.fixture
def objects():
    return [
        Color(id=1, name='black', rgb='123456', is_trans=True),
        Inventory(id=1, version=42, set_num='7189-1'),
        InventoryPart(inventory_id=1, part_num='3001', color_id=1, quantity=12),
        InventorySet(inventory_id=1, set_num='7189-1', quantity=1),
        Part(part_num='3001', name='Brick 2X4', part_cat_id=1),
        PartCategory(id=1, name='bricks'),
        Set(set_num='7189-1', name='Dumy Test', year=2015, theme_id=42, num_parts=12),
        Theme(id=42, name='Town', parent_id=None),
        Theme(id=43, name='Police', parent_id=42)
    ]


def test_models(session, objects):
    session.add_all(objects)

    session.commit()

    for obj in objects:
        session.refresh(obj)
        print(obj)
