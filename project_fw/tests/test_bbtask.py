import pytest
from bbtask.task import sum as s;

def test_sum():
    assert s(10,20) == 30;
