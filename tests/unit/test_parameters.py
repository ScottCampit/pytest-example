# test_parameters.py
import pytest
@pytest.mark.parametrize("text", [
    "",
    "i",
    "Robby",
    "Another one bites the dust.",
])

def test_is_text(text):
	assert isinstance(text, str) 