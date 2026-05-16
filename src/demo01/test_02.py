import pytest


def test_pass():
    assert 1 == 1
    
    
def test_fail():
    assert 1 == 2


@pytest.fixture
def f():
    assert 1 == 2


def test_error(f):
    pass


@pytest.mark.skip
def test_skip():
    assert 1 == 2


@pytest.mark.xfail
def test_xpass():
    pass