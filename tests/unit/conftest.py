# conftest.py
import pytest

@pytest.fixture()
def test_dataset():
	return {
            'Name': 'John Doe', 
            'Phone': '8008889999'
        }