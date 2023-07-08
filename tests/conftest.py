import pytest
from website import create_app

# over here you start with fixtures, a base for all of the tests

@pytest.fixture()
def app():
    app = create_app()