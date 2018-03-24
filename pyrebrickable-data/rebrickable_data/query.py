import random

from sqlalchemy import func, or_

from rebrickable_data.models import Set, Theme, Part, PartRelationship
from rebrickable_data.database import Session

session = Session()


for set in session.query(Set):
    if len(set.inventories) == 5:
        # the 421-2 set from 1966
        for inventory in set.inventories:
            print(len(inventory.parts) + ' parts in inventory')


for part in session.query(Part) \
        .filter(Part.has_variants).limit(50):
    print(part)
    for p in part.printed_variants:
        print('printed  : ' + str(p))
    for p in part.alt_variants:
        print('alt      : ' + str(p))
    for p in part.mold_variants:
        print('mold alt : ' + str(p))
    for p in part.patterned_variants:
        print('patterns : ' + str(p))


def print_theme(theme, indent=0):
    print(' ' * indent + theme.name)
    for child in theme.children:
        print_theme(child, indent+4)


for theme in session.query(Theme) \
        .filter(Theme.parent != None).limit(25):
    if theme.parent is not None:
        continue
    print_theme(theme)
