import os
from appdirs import AppDirs
from sqlalchemy import inspect

from .models import *

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


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
