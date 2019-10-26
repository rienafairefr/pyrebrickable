# Used to answer https://bricks.stackexchange.com/q/10233/9843
from sqlalchemy import and_

from rebrickable.data.models import Part, Inventory, InventoryPart, Color, Set
from rebrickable.data.database import Session

session = Session()

parts = session.query(Part)
colors = session.query(Color)
sets = session.query(Set.set_num).join(Inventory).join(InventoryPart)

# Plate, Modified 1 x 2 with Handle on Side - Free Ends
part1 = parts.get("2540")
# seems to be white

# Hinge Plate 1 x 2 Locking with 2 Fingers on Side
part2 = parts.get("60471")
# in black

# Plate 1 X 2
part3 = parts.get("3023")
# in transparent

black = colors.filter_by(name='Black').one()
trans_clear = colors.filter_by(name='Trans-Clear').one()
red = colors.filter_by(name='Red').one()

part1s = sets.filter(InventoryPart.part == part1).all()
part2s = sets.filter(and_(InventoryPart.part == part2, InventoryPart.color == black)).all()
part3s = sets.filter(and_(InventoryPart.part == part3, InventoryPart.color == trans_clear)).all()

intersection = set(part1s).intersection(part2s, part3s)
print('')
print('')
for set in intersection:
    print(set.set_num)
