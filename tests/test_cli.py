#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyrebrickable` package."""

import click
import mock
import pytest
from click.testing import CliRunner
from mock import MagicMock

from rebrickable_api import LegoApi, UsersApi, UsersTokenResponse
from rebrickable_api.rest import ApiException
from rebrickable_cli import cli
from rebrickable_cli.cli import (lego_colors_list,
                                 lego_colors_read,
                                 lego_elements_read,
                                 lego_mocs_parts_list,
                                 lego_mocs_read,
                                 lego_part_categories_list,
                                 lego_part_categories_read,
                                 lego_parts_colors_list,
                                 lego_parts_colors_read,
                                 lego_parts_colors_sets_list,
                                 lego_parts_list,
                                 lego_parts_read,
                                 lego_sets_alternates_list,
                                 lego_sets_list,
                                 lego_sets_parts_list,
                                 lego_sets_read,
                                 lego_sets_sets_list,
                                 lego_themes_list,
                                 users_allparts_list,
                                 users_badges_list,
                                 users_badges_read,
                                 users_build_read,
                                 users_lost_parts_create,
                                 users_lost_parts_delete,
                                 users_lost_parts_list,
                                 users_partlists_create,
                                 users_partlists_delete,
                                 users_partlists_list,
                                 users_partlists_partial_update,
                                 users_partlists_parts_create,
                                 users_partlists_parts_delete,
                                 users_partlists_parts_list,
                                 users_partlists_parts_read,
                                 users_partlists_parts_update,
                                 users_partlists_read,
                                 users_partlists_update,
                                 users_parts_list,
                                 users_profile_list,
                                 users_setlists_create,
                                 users_setlists_delete,
                                 users_setlists_list,
                                 users_setlists_partial_update,
                                 users_setlists_read,
                                 users_setlists_sets_create,
                                 users_setlists_sets_delete,
                                 users_setlists_sets_list,
                                 users_setlists_sets_partial_update,
                                 users_setlists_sets_read,
                                 users_setlists_sets_update,
                                 users_setlists_update,
                                 users_sets_create,
                                 users_sets_delete,
                                 users_sets_list,
                                 users_sets_read,
                                 users_sets_sync_create,
                                 users_sets_update,
                                 users_token_create, lego_themes_read,

                                 UsersContext,
                                 users,
                                 main,
                                 lego)


@pytest.fixture(scope='function')
def runner(request):
    return CliRunner()


def test_command_line_interface(runner):
    """Test the CLI."""
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_command_line_interface_api_calls(runner):
    lego_entrypoints = [
        lego_colors_list,
        lego_colors_read,
        lego_elements_read,
        lego_mocs_parts_list,
        lego_mocs_read,
        lego_part_categories_list,
        lego_part_categories_read,
        lego_parts_colors_list,
        lego_parts_colors_read,
        lego_parts_colors_sets_list,
        lego_parts_list,
        lego_parts_read,
        lego_sets_alternates_list,
        lego_sets_list,
        lego_sets_parts_list,
        lego_sets_read,
        lego_sets_sets_list,
        lego_themes_list,
        lego_themes_read]
    users_entrypoints = [
        users_allparts_list,
        users_badges_list,
        users_badges_read,
        users_build_read,
        users_lost_parts_create,
        users_lost_parts_delete,
        users_lost_parts_list,
        users_partlists_create,
        users_partlists_delete,
        users_partlists_list,
        users_partlists_partial_update,
        users_partlists_parts_create,
        users_partlists_parts_delete,
        users_partlists_parts_list,
        users_partlists_parts_read,
        users_partlists_parts_update,
        users_partlists_read,
        users_partlists_update,
        users_parts_list,
        users_profile_list,
        users_setlists_create,
        users_setlists_delete,
        users_setlists_list,
        users_setlists_partial_update,
        users_setlists_read,
        users_setlists_sets_create,
        users_setlists_sets_delete,
        users_setlists_sets_list,
        users_setlists_sets_partial_update,
        users_setlists_sets_read,
        users_setlists_sets_update,
        users_setlists_update,
        users_sets_create,
        users_sets_delete,
        users_sets_list,
        users_sets_read,
        users_sets_sync_create,
        users_sets_update,
        users_token_create
    ]

    def treat_(fun, obj, mocked_call):
        args = ['0' for param in fun.params]
        result = runner.invoke(fun, obj=obj, args=args)
        assert mocked_call.called
        print(fun.callback.__name__)
        assert result.exception is None

    for func in lego_entrypoints:
        name = func.callback.__name__
        with mock.patch('rebrickable_api.LegoApi', spec=LegoApi) as ctx_mock:
            mocked_call = MagicMock()
            setattr(ctx_mock, name, mocked_call)
            treat_(func, ctx_mock, mocked_call)

    for func in users_entrypoints:
        name = func.callback.__name__
        with mock.patch('rebrickable_cli.cli.UsersContext', spec=UsersContext) as ctx_mock:
            mocked_call = MagicMock()
            ctx_mock.api = MagicMock(spec=UsersApi)
            ctx_mock.token = 'ttt'
            setattr(ctx_mock.api, name, mocked_call)
            treat_(func, ctx_mock, mocked_call)


@main.command(name='test')
@click.pass_obj
def command_dummy(obj):
    pass


def data_context(value={}):
    def get_data():
        return value

    return mock.patch('rebrickable_cli.cli.get_data', side_effect=get_data)


def test_main_command_pass_obj_valid(runner):
    with data_context({'api_key':'api_key_value'}):
        result = runner.invoke(main, ['test'])
        assert result.exception is None


def test_main_command_pass_obj_invalid(runner):
    with data_context():
        result = runner.invoke(main, ['test'])
        assert result.exception is not None


@users.command(name='test')
@click.pass_obj
def users_test(obj):
    pass


def test_users_command_pass_obj_valid(runner):
    with data_context({'api_key':'api_key_value', 'users_token': 'users_token_value'}):
        result = runner.invoke(main, ['users', 'test'])
        assert result.exception is None


def test_users_command_pass_obj_invalid(runner):
    with data_context():
        result = runner.invoke(main, ['users', 'test'])
        assert result.exception is not None


@lego.command(name='test')
@click.pass_obj
def lego_test(obj):
    pass


def test_lego_command_pass_obj_valid(runner):
    with data_context({'api_key':'api_key_value'}):
        result = runner.invoke(main, ['lego', 'test'])
        assert result.exception is None


def test_lego_command_pass_invalid(runner):
    with data_context():
        result = runner.invoke(main, ['lego', 'test'])
        assert result.exception is not None


def test_users_login_no_username(runner):
    with data_context({'api_key':'api_key_value'}):
        result = runner.invoke(main, ['users', 'login'])
        # no username
        assert result.exception is not None


def test_users_login(runner):
    def users_token_create(s, user, password):
        assert user == 'username'
        assert password == 'password'
        return UsersTokenResponse(user_token='user_token')

    def update_data(key, value):
        assert key == 'users_token'
        assert value == 'user_token'

    def getpass():
        return 'password'

    with data_context({'api_key':'api_key_value'}), \
         mock.patch('rebrickable_cli.cli.getpass', new=getpass), \
         mock.patch.object(UsersApi,'users_token_create', new=users_token_create),\
                mock.patch('rebrickable_cli.cli.update_data', side_effect=update_data):

        result = runner.invoke(main, ['users', 'login', 'username'])

        assert result.exception is None


def test_users_login_invalid_login(runner):
    def users_token_create(s, user, password):
        raise ApiException()

    def getpass():
        return 'password'

    with data_context({'api_key': 'api_key_value'}), \
         mock.patch('rebrickable_cli.cli.getpass', new=getpass), \
         mock.patch.object(UsersApi, 'users_token_create', new=users_token_create):
        result = runner.invoke(main, ['users', 'login', 'username'])

        assert result.exception is not None


def test_users_profile_invalid_login(runner):
    with data_context({'api_key': 'api_key_value'}):
        result = runner.invoke(main, ['users', 'profile'])

        assert result.exception is not None


def test_register_valid(runner):
    def getpass(prompt):
        return 'api_key_value'

    def update_data(key, value):
        assert key == 'api_key'
        assert value == 'api_key_value'

    with mock.patch('rebrickable_cli.cli.getpass', new=getpass), \
         mock.patch('rebrickable_cli.cli.update_data', side_effect=update_data):
        result = runner.invoke(main, ['register'])

        assert result.exception is None
