import pytest

from helper import get_least

@pytest.mark.parametrize(
    'src, exp_result',
    [
        ([0, 1, 2, 3], 0),
        ([-1, 0, 1, 2, 3], 0),
        ([-10, 1, 2, 3, -5], 1),
    ]
)

def test_success_get_least(src, exp_result):
    result = get_least(*src)
    assert result == exp_result
