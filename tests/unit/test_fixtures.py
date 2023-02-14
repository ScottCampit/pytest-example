import pytest

@pytest.fixture
def example_return_1():
	return 1

def test_fixture(example_return_1):
	assert example_return_1 == 1