from __future__ import print_function

import pytest
from click import Command


def parametrized(*args, **kwargs):
    def decorator(fun):
        if 'ids' not in kwargs:
            def get_id(param):
                if isinstance(param, Command):
                    return param.callback.__name__
                return str(param)

            kwargs['ids'] = get_id
        return pytest.mark.parametrize(*args, **kwargs)(fun)

    return decorator


def do_test(cli_func, method, cli_args, call_kwargs, runner, state):
    mocked_method = getattr(state.api, method)
    mocked_method.return_value = 'stuff'
    result = runner.invoke(cli_func, cli_args, obj=state)
    if result.exit_code != 0:
        print(result.output)
        pass
    mocked_method.assert_called_with(**call_kwargs)
    assert 'stuff\n' == result.output


