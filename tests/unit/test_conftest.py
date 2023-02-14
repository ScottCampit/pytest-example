# test_conftest.py
import pytest

def test_fixture(test_dataset):
	assert test_dataset['Name'] == 'John Doe'