import os
from appdirs import AppDirs

from rebrickable_data.models import *

data_dir = AppDirs('pyrebrickable').user_data_dir

try:
    os.makedirs(data_dir)
except OSError:
    pass

data_mapping = {
    'themes': Theme,
    'colors': Color,
    'part_categories': PartCategory,
    'parts': Part,
    'inventories': Inventory,
    'sets': Set,
    'inventory_parts': InventoryPart,
    'inventory_sets': InventorySet,
    'part_relationships': PartRelationship
}
