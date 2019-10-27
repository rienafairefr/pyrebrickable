#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyrebrickable` package."""
import decorator
import pytest

from mock import patch, Mock

from rebrickable.api import Part, Color, Element, Moc, LegoApi, PartColorsElement, UsersApi
from rebrickable.cli.common import pass_state, State
from rebrickable.cli.lego import lego, lego_part, lego_part_color, lego_color, lego_element, lego_moc
from rebrickable.cli.main import main
from rebrickable.cli.user import user


def test_command_line_interface(runner):
    """Test the CLI."""
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert 'main' in result.output
    help_result = runner.invoke(main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output


def mocked_data(value=None):
    def get_():
        return value

    def wrapper(fun, *args, **kwargs):
        @patch('rebrickable.cli.common.get_data', new=Mock(side_effect=get_))
        @patch('rebrickable.cli.main.get_data', new=Mock(side_effect=get_))
        @patch('rebrickable.cli.users.get_data', new=Mock(side_effect=get_))
        def decorated(*a, **kwa):
            return fun(*a, **kwa)

        return decorated
    return decorator.decorator(wrapper)


@main.command(name='test')
def command_dummy():
    pass


@mocked_data({})
def test_main_command_pass_obj_invalid(runner):
    result = runner.invoke(main, ['test'])
    assert result.exception is not None


@mocked_data(None)
def test_users_command_pass_obj_invalid(runner):
    result = runner.invoke(main, ['user', 'test'])
    assert result.exception is not None


@mocked_data({'api_key': 'api_key_value'})
def test_main_command_pass_obj_valid(runner):
    result = runner.invoke(main, ['test'])
    assert result.exception is None


@mocked_data({'api_key': 'api_key_value', 'default_user': 'username', 'users': {'username': {'token': 'user_token_value'}}})
def test_users_command_pass_obj_valid(runner):
    @user.command(name='test')
    @pass_state
    def user_test(state):
        assert isinstance(state.api, UsersApi)
        assert state.user_token == 'user_token_value'

    result = runner.invoke(main, ['user', 'test'])
    assert result.exception is None


@mocked_data({'api_key': 'api_key_value', 'users': {'username': {'token': 'user_token_value'}}})
def test_users_command_pass_obj_valid(runner):
    @user.command(name='test')
    @pass_state
    def user_test(state):
        assert isinstance(state.api, UsersApi)
        assert state.user_token == 'user_token_value'

    result = runner.invoke(main, ['user', '-u', 'username', 'test'])
    assert result.exception is None


@pytest.fixture
def mocked_state():
    return State()


@patch('rebrickable.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_parts_read', Mock(return_value=Part(part_num='3002')))
def test_lego_part_command_pass_obj(runner):
    @lego_part.command(name='test')
    @pass_state
    def lego_part_test(state):
        assert state.part_num == "3002"

    result = runner.invoke(main, ['lego', 'part', '3002', 'test'])
    assert result.exception is None


@patch('rebrickable.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_parts_read', Mock(return_value=Part(part_num='3002')))
@patch.object(LegoApi, 'lego_parts_colors_read', Mock(return_value=PartColorsElement(elements=[Element(color=Color(id=5), part=Part(part_num="3002"))])))
def test_lego_part_color_command_pass_obj(runner):
    @lego_part_color.command(name='test')
    @pass_state
    def lego_part_color_test(state):
        assert state.color_id == 5
        assert state.part_num == "3002"

    result = runner.invoke(main, ['lego', 'part', '3002', 'color', '5', 'test'])
    assert result.exception is None


@patch('rebrickable.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_colors_read', Mock(return_value=Color(id=1234)))
def test_lego_color_command_pass_obj(runner):
    @lego_color.command(name='test')
    @pass_state
    def lego_color_test(state):
        assert state.color_id == 1234

    result = runner.invoke(main, ['lego', 'color', '1234', 'test'])
    assert result.exception is None


@patch('rebrickable.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_elements_read', Mock(return_value=Element(element_id=1234)))
def test_lego_element_command_pass_obj(runner):
    @lego_element.command(name='test')
    @pass_state
    def lego_element_test(state):
        assert state.element_id == '1234'

    result = runner.invoke(main, ['lego', 'element', '1234', 'test'])
    assert result.exception is None


@patch('rebrickable.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_mocs_read', Mock(return_value = Moc(set_num='MOC-1234')))
def test_lego_moc_command_pass_obj(runner):
    @lego_moc.command(name='test')
    @pass_state
    def lego_moc_test(state):
        assert state.set_num == "MOC-1234"

    result = runner.invoke(main, ['lego', 'moc', 'MOC-1234', 'test'])
    assert result.exception is None


@patch('rebrickable.cli.utils.get_api_client', new=Mock())
@mocked_data({'api_key': 'api_key_value'})
def test_lego_command_pass_obj_valid(runner):
    @lego.command(name='test')
    @pass_state
    def lego_test(state):
        assert isinstance(state.api, LegoApi)

    result = runner.invoke(main, ['lego', 'test'])
    assert result.exception is None


@mocked_data({})
def test_lego_command_pass_invalid(runner):
    result = runner.invoke(main, ['lego', 'test'])
    assert result.exception is not None


@mocked_data({'api_key': 'api_key_value'})
def test_user_profile(runner):
    result = runner.invoke(main, ['user', 'profile'])

    assert result.exception is not None


def test_register_valid(runner):
    def write_data(data):
        assert data['api_key'] == 'api_key_value'

    with patch('rebrickable.cli.main.prompt', return_value='api_key_value'), \
         patch('rebrickable.cli.utils.write_data', side_effect=write_data):
        result = runner.invoke(main, ['register'])

        assert result.exception is None
