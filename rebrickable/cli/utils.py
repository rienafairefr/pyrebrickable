import json
import os
import re
from enum import EnumMeta

import click
from appdirs import AppDirs

config_dir = AppDirs('pyrebrickable').user_config_dir

try:
    os.makedirs(config_dir)
except OSError:
    pass

DATA_PATH = os.path.join(config_dir, 'config.json')


def write_data(data, data_path=DATA_PATH):
    with open(data_path, 'w+') as data_file:
        json.dump(data, data_file)


def get_data(data_path=DATA_PATH):
    try:
        with open(data_path, 'r') as data_file:
            return json.load(data_file)
    except (IOError, ValueError):
        print('error getting config data from %s' % data_path)
        return {}


class EnumType(click.Choice):
    def __init__(self, enum, casesensitive=True):
        if isinstance(enum, EnumMeta):
            choices = enum.__members__
        else:
            raise TypeError("`enum` must be `Enum`")

        if not casesensitive:
            choices = (_.lower() for _ in choices)

        self.__enum = enum
        self.__casesensitive = casesensitive

        # TODO choices do not have the save order as enum
        super(EnumType, self).__init__(list(sorted(set(choices))))

    def convert(self, value, param, state):
        if not self.__casesensitive:
            value = value.lower()

        value = super(EnumType, self).convert(value, param, state)

        if not self.__casesensitive:
            return next(_ for _ in self._EnumType__enum if _.name.lower() ==
                        value.lower())
        else:
            return next(_ for _ in self._EnumType__enum if _.name == value)

    def get_metavar(self, param):
        word = self.__enum.__name__

        # Stolen from jpvanhal/inflection
        word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
        word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
        word = word.replace("-", "_").lower().split("_")

        if word[-1] == "enum":
            word.pop()

        return ("_".join(word)).upper()
