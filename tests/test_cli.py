#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyrebrickable` package."""

import click
from mock import patch, Mock
from functools import wraps

from rebrickable_api import Part, Color, Element, Moc, LegoApi, PartColorsElement
from rebrickable_api.rest import ApiException
from rebrickable_cli.cli.common import pass_usercontext, pass_global, GlobalContext
from rebrickable_cli.cli.lego import lego, lego_part, lego_part_color, lego_color, lego_element, lego_moc
from rebrickable_cli.cli.main import main
from rebrickable_cli.cli.user import user


def test_command_line_interface(runner):
    """Test the CLI."""
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert 'main' in result.output
    help_result = runner.invoke(main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output


@main.command(name='test')
@pass_global
def command_dummy(obj):
    pass


def mocked_data(value=None):
    def get_():
        return value

    def decorator(fun):
        @patch('rebrickable_cli.cli.common.get_data', new=Mock(side_effect=get_))
        @patch('rebrickable_cli.cli.main.get_data', new=Mock(side_effect=get_))
        @patch('rebrickable_cli.cli.users.get_data', new=Mock(side_effect=get_))
        @wraps(fun)
        def wrapper(*args, **kwargs):
            return fun(*args, **kwargs)
        return wrapper
    return decorator


def with_mocked_api():
    def decorator(fun):
        def get_part(part_num, *args, **kwargs):
            return Part(part_num=part_num)

        @wraps(fun)
        @patch.object(LegoApi, 'lego_parts_read', Mock(side_effect=get_part))
        def wrapper(*args, **kwargs):
            return fun(*args, **kwargs)

        return wrapper
    return decorator

@mocked_data({'api_key': 'api_key_value'})
def test_main_command_pass_obj_valid(runner):
    result = runner.invoke(main, ['test'])
    assert result.exception is None


@mocked_data({})
def test_main_command_pass_obj_invalid(runner):
    result = runner.invoke(main, ['test'])
    assert result.exception is not None


@user.command(name='test')
@pass_usercontext
def user_test(users_context):
    assert users_context.token == 'user_token_value'


@mocked_data({'api_key': 'api_key_value', 'users': {'%%default%%': {'token': 'user_token_value'}}})
def test_users_command_pass_obj_valid(runner):
    result = runner.invoke(main, ['user', 'test'])
    assert result.exception is None


@mocked_data(None)
def test_users_command_pass_obj_invalid(runner):
    result = runner.invoke(main, ['user', 'test'])
    assert result.exception is not None


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_parts_read', Mock(return_value=Part(part_num='3002')))
def test_lego_part_command_pass_obj(runner):
    @lego_part.command(name='test')
    @click.pass_context
    def lego_part_test(ctx):
        part = ctx.find_object(Part)
        assert part.part_num == "3002"

    result = runner.invoke(main, ['lego', 'part', '3002', 'test'])
    assert result.exception is None


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_parts_read', Mock(return_value=Part(part_num='3002')))
@patch.object(LegoApi, 'lego_parts_colors_read', Mock(return_value=PartColorsElement(elements=[Element(color=Color(id=5), part=Part(part_num="3002"))])))
def test_lego_part_color_command_pass_obj(runner):
    @lego_part_color.command(name='test')
    @click.pass_context
    def lego_part_color_test(ctx):
        part_colors_element = ctx.find_object(PartColorsElement).elements[0]
        assert part_colors_element.color.id == 5
        assert part_colors_element.part.part_num == "3002"

    result = runner.invoke(main, ['lego', 'part', '3002', 'color', '5', 'test'])
    assert result.exception is None


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_colors_read', Mock(return_value=Color(id=1234)))
def test_lego_color_command_pass_obj(runner):
    @lego_color.command(name='test')
    @click.pass_context
    def lego_color_test(ctx):
        color = ctx.find_object(Color)
        assert color.id == 1234

    result = runner.invoke(main, ['lego', 'color', '1234', 'test'])
    assert result.exception is None


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_elements_read', Mock(return_value=Element(element_id=1234)))
def test_lego_element_command_pass_obj(runner):
    @lego_element.command(name='test')
    @click.pass_context
    def lego_element_test(ctx):
        element = ctx.find_object(Element)
        assert element.element_id == 1234

    result = runner.invoke(main, ['lego', 'element', '1234', 'test'])
    assert result.exception is None


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@patch.object(LegoApi, 'lego_mocs_read', Mock(return_value = Moc(set_num='MOC-1234')))
def test_lego_moc_command_pass_obj(runner):
    @lego_moc.command(name='test')
    @click.pass_context
    def lego_moc_test(ctx):
        moc = ctx.find_object(Moc)
        assert moc.set_num == "MOC-1234"

    result = runner.invoke(main, ['lego', 'moc', 'MOC-1234', 'test'])
    assert result.exception is None


@lego.command(name='test')
def lego_test():
    pass


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@mocked_data({'api_key': 'api_key_value'})
def test_lego_command_pass_obj_valid(runner):
    result = runner.invoke(main, ['lego', 'test'])
    assert result.exception is None


@mocked_data({})
def test_lego_command_pass_invalid(runner):
    result = runner.invoke(main, ['lego', 'test'])
    assert result.exception is not None


@patch('rebrickable_cli.cli.main.get_api_client', new=Mock())
@mocked_data({'api_key': 'api_key_value'})
def test_users_login_no_username(runner):
    result = runner.invoke(main, ['users', 'login'])
    # no username
    assert result.exception is not None


@mocked_data({'api_key': 'api_key_value'})
def test_users_login(runner):
    def write_data(data):
        assert data == {'api_key': 'api_key_value',
                        'users': {
                            '%%default%%': {
                                'token': 'user_token'
                            },
                            'username': {
                                'token': 'user_token'
                            }
                        }}

    with patch('rebrickable_cli.cli.users.create_auth', return_value='user_token'), \
         patch('rebrickable_cli.cli.users.write_data', side_effect=write_data):
        result = runner.invoke(main, ['users', 'login', 'username'])

        assert result.exception is None


@mocked_data({'api_key': 'api_key_value'})
def test_users_login_other(runner):
    def write_data(data):
        assert data == {'api_key': 'api_key_value',
                        'users': {
                            'username': {
                                'token': 'user_token'
                            }
                        }}

    with patch('rebrickable_cli.cli.users.create_auth', return_value='user_token'), \
         patch('rebrickable_cli.cli.users.write_data', side_effect=write_data):
        result = runner.invoke(main, ['users', 'login', '--other', 'username'])

        assert result.exception is None


@mocked_data({'api_key': 'api_key_value'})
def test_users_login_invalid_login(runner):
    def create_auth(users_api, username):
        raise ApiException()

    with patch('rebrickable_cli.cli.users.create_auth', side_effect=create_auth):
        result = runner.invoke(main, ['users', 'login', 'username'])

    assert result.exception is not None


@mocked_data({'api_key': 'api_key_value'})
def test_users_profile_invalid_login(runner):
    result = runner.invoke(main, ['users', 'profile'])

    assert result.exception is not None


def test_register_valid(runner):
    def write_data(data):
        assert data['api_key'] == 'api_key_value'

    with patch('rebrickable_cli.cli.main.get_api_key', return_value='api_key_value'), \
         patch('rebrickable_cli.cli.main.write_data', side_effect=write_data):
        result = runner.invoke(main, ['register'])

        assert result.exception is None
