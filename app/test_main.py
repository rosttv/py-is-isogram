import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ('playgrounds', True),
        ('look', False),
        ('Adam', False),
        ('', True),
    ]
)
def test_isogram(word, result) -> None:
    assert (
        is_isogram(word) == result
    ), f"{word} should be equal to {result}"
