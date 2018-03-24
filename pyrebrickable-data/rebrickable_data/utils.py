import os
from appdirs import AppDirs

data_dir = AppDirs('pyrebrickable').user_data_dir


try:
    os.makedirs(data_dir)
except OSError:
    pass

data_files = ['themes',
              'colors',
              'part_categories',
              'parts',
              'inventories',
              'sets',
              'inventory_parts',
              'inventory_sets',
              'part_relationships']