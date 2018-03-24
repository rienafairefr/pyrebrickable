from sqlalchemy import func

from rebrickable_data.models import Set, Theme, Part, PartRelationship
from rebrickable_data.database import Session

session = Session()


def random_row(session, model_name):
    return session.query(model_name).order_by(func.random()).first()


while True:
    random_part = random_row(session, Part)
    if random_part.printed_variants != [] or random_part.printed_variant_of != []:
        break

print(random_part)
print()
print('relationship is child  ' + str(session.query(PartRelationship).filter(PartRelationship.c.child_part_num == random_part.part_num).all()))
print('relationship is parent ' + str(session.query(PartRelationship).filter(PartRelationship.c.parent_part_num == random_part.part_num).all()))
print()
print('printed variants' + str(random_part.printed_variants))
print('printed variant of ' + str(random_part.printed_variant_of))

exit(0)


random_set = random_row(session, Set)
print(random_set.inventory)

def print_theme(theme, indent):
    print(' ' * indent + theme.name)
    for child in theme.children:
        print_theme(child, indent+4)


for theme in session.query(Theme):
    if theme.parent is not None:
        continue
    print_theme(theme, 0)

for theme in session.query(Theme):
    print(theme)