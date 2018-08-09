# Used to answer https://bricks.stackexchange.com/q/10233/9843
from sqlalchemy import and_

from rebrickable_data.models import Part, Inventory, InventoryPart, Color
from rebrickable_data.database import Session

session = Session()

# Plate, Modified 1 x 2 with Handle on Side - Free Ends
part1 = session.query(Part).get("2540")
# seems to be white

# Hinge Plate 1 x 2 Locking with 2 Fingers on Side
part2 = session.query(Part).get("60471")
# in black

# Plate 1 X 2
part3 = session.query(Part).get("3023")
# in transparent


black = session.query(Color).filter_by(name='Black').one()
trans_clear = session.query(Color).filter_by(name='Trans-Clear').one()
red = session.query(Color).filter_by(name='Red').one()

set_parts = [part1, part2, part3]

part1s = session.query(Inventory).join(InventoryPart).filter(InventoryPart.part_num == "2540").all()
part2s = session.query(Inventory).join(InventoryPart).filter(and_(InventoryPart.part_num == "60471",
                                                                  InventoryPart.color == black)).all()
part3s = session.query(Inventory).join(InventoryPart).filter(
    and_(InventoryPart.part_num == "3023", InventoryPart.color == trans_clear)).all()

intersection = set(part1s).intersection(part2s, part3s)

for set in intersection:
    print(set.set_num)