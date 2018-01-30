#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyrebrickable` package."""
from unittest import mock
from unittest.mock import MagicMock

import click
from click.testing import CliRunner

from rebrickable import cli, LegoApi, UsersApi
from inspect import getmembers


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
            if name.startswith('users'):
                api_class = 'rebrickable.api.users_api.UsersApi',UsersApi
            elif name.startswith('lego'):
                api_class = 'rebrickable.api.lego_api.LegoApi', LegoApi

            with mock.patch(api_class[0], spec=api_class[1]) as api_mock:
                setattr(api_mock,name, mocked_call)
                args = ['0' for param in fun.params]
                result = runner.invoke(fun, obj=api_mock, args=args)
                print(result)
                assert mocked_call.called

            pass
    pass
