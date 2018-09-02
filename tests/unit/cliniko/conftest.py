import pytest

from cliniko.client import ClinikoClient


@pytest.fixture(scope='function')
def client():
    # return ClinikoClient.from_environment('CLINIKO_PYTHON_API_KEY')
    return ClinikoClient('2632611e770c57f3166a4b44fb542048')