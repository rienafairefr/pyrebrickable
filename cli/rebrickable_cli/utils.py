import json
import os

from appdirs import AppDirs

config_dir = AppDirs('pyrebrickable').user_config_dir

try:
    os.makedirs(config_dir)
except OSError:
    pass

DATA_PATH = os.path.join(config_dir, 'config.json')


def update_data(key, value, data_path=DATA_PATH):
    data = get_data(data_path)
    data[key] = value
    write_data(data, data_path)


def write_data(data, data_path=DATA_PATH):
    with open(data_path, 'w+') as data_file:
        json.dump(data, data_file)


def get_data(data_path=DATA_PATH):
    try:
        with open(data_path, 'r') as data_file:
            return json.load(data_file)
    except IOError:
        return {}
    except ValueError:
        return {}

