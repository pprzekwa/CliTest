import pytest
from models.cli_mock import CliMock


@pytest.fixture(scope='module')
def cli_mock():
    return CliMock()
