# Used to answer https://bricks.stackexchange.com/q/10548/
import pprint

from sqlalchemy import and_

from rebrickable.data.database import Session
from rebrickable.data.models import Part, Inventory, InventoryPart, Color, Set
from rebrickable.data.utils import object_as_dict

session = Session()

parts = session.query(Part)
colors = session.query(Color)
sets = session.query(Set.set_num).join(Inventory).join(InventoryPart).join(Part).join(Color)

# cap
cap = parts.get("86035")
cone = parts.get('4589')
knit_cap = parts.get("41334")

white = colors.filter_by(name='White').one()
blue = colors.filter_by(name='Blue').one()
black = colors.filter_by(name='Black').one()
light_bley = colors.filter_by(name='Light Bluish Gray').one()

white_caps = sets.filter(and_(InventoryPart.part == cap, InventoryPart.color == white)).all()
black_knit_cap = sets.filter(and_(InventoryPart.part == knit_cap, InventoryPart.color == black)).all()
gray_cone = sets.filter(and_(InventoryPart.part == cone, InventoryPart.color == light_bley)).all()

intersection = set(white_caps).intersection(black_knit_cap).intersection(gray_cone)
print('')
print('')
for set in intersection:
    print(set.set_num)
    pprint.pprint(object_as_dict(session.query(Set).get(set)))
