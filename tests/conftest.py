import pytest
from click.testing import CliRunner
from mock import mock, patch

from rebrickable.api import *


@pytest.fixture(scope='session')
def runner():
    return CliRunner()


def _read_echo(type_):
    def fun(*args, **kwargs):
        return type_(*args, **kwargs)

    return fun


@pytest.fixture
def mocked_lego_api():
    with mock.patch('rebrickable.api.LegoApi', spec=LegoApi) as state_mock, \
            patch.object(LegoApi, 'lego_colors_read', side_effect=_read_echo(Color)), \
            patch.object(LegoApi, 'lego_elements_read', side_effect=_read_echo(Element)), \
            patch.object(LegoApi, 'lego_mocs_read', side_effect=_read_echo(Moc)), \
            patch.object(LegoApi, 'lego_part_categories_read', side_effect=_read_echo(PartCategory)), \
            patch.object(LegoApi, 'lego_parts_colors_read', side_effect=lambda *args, **kwargs: PartColorsElement()), \
            patch.object(LegoApi, 'lego_parts_read', side_effect=_read_echo(Part)), \
            patch.object(LegoApi, 'lego_sets_read', side_effect=_read_echo(Set)), \
            patch.object(LegoApi, 'lego_themes_read', side_effect=_read_echo(Theme)):
        yield state_mock


@pytest.fixture
def mocked_users_api():
    with mock.patch('rebrickable.api.UsersApi', spec=UsersApi) as state_mock, \
            patch.object(UsersApi, 'users_badges_read', side_effect=_read_echo(Badge)), \
            patch.object(UsersApi, 'users_build_read', side_effect=lambda *args, **kwargs: Build()), \
            patch.object(UsersApi, 'users_partlists_parts_read', side_effect=_read_echo(PartListPart)), \
            patch.object(UsersApi, 'users_partlists_read', side_effect=_read_echo(PartList)), \
            patch.object(UsersApi, 'users_setlists_read', side_effect=_read_echo(SetList)), \
            patch.object(UsersApi, 'users_sets_read', side_effect=_read_echo(Set)):
        yield state_mock
