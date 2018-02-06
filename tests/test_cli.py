#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyrebrickable` package."""
import mock
from mock import MagicMock

import click
from click.testing import CliRunner

from rebrickable_api import LegoApi, UsersApi
from inspect import getmembers

from rebrickable_cli import cli
from rebrickable_cli.cli import UsersContext


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_command_line_interface_api_calls():
    alldefs = getmembers(cli)
    runner = CliRunner()
    for (name, fun) in alldefs:
        if name == 'register':
            continue
        if name == 'users_login':
            continue
        mocked_call = MagicMock()

        if isinstance(fun, click.Command) and not isinstance(fun, click.Group):
            def treat_(obj):
                args = ['0' for param in fun.params]
                result = runner.invoke(fun, obj=obj, args=args)
                print(result)
                assert mocked_call.called

            if name.startswith('users'):
                with mock.patch('rebrickable_cli.cli.UsersContext', spec=UsersContext) as ctx_mock:
                    ctx_mock.api = MagicMock(spec=UsersApi)
                    ctx_mock.token = 'ttt'
                    setattr(ctx_mock.api, name, mocked_call)
                    treat_(ctx_mock)
            elif name.startswith('lego'):
                with mock.patch('rebrickable_api.LegoApi', spec=LegoApi) as ctx_mock:
                    setattr(ctx_mock, name, mocked_call)
                    treat_(ctx_mock)
