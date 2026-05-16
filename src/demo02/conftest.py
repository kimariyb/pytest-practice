import pytest
import datetime

@pytest.fixture(scope='session')
def fixture_fn():
    print("用例的开始时间：", datetime.datetime.now())
    yield
    print("用例的结束时间：", datetime.datetime.now())