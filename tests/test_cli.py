import logging
import os
import pytest

from structs.commands import commands

dir_name = os.path.abspath(__file__)
pytest.main(args=['-s', dir_name])
logging.basicConfig(filename='log_file', level=logging.DEBUG)


def recursive_command_check(cmd, cli):
    logging.debug('Executing {} ...'.format(cmd['expected_message']))
    assert cmd['expected_message'] == cli.execute(cmd['command'])
    if 'sub_commands' in cmd:
        for name, values in cmd['sub_commands'].items():
            recursive_command_check(values, cli)


def test_cli_commands(cli_mock):
    logging.debug('Start test of cli commands')
    recursive_command_check(commands['user'], cli_mock)
    logging.debug('End test of cli commands')



