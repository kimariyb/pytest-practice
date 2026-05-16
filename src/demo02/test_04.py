import pytest
import datetime
        
    

@pytest.fixture(scope='module')
def fixture_fn():
    print("用例的开始时间：", datetime.datetime.now())
    yield '我是 fixture'
    print("用例的结束时间：", datetime.datetime.now())
    

class TestUser:
    def test_web(self, fixture_fn):
        print(fixture_fn)
    
    def test_api(self, fixture_fn):
        pass
    
class TestGoods:
    def test_web(self, fixture_fn):
        pass
    
    def test_api(self, fixture_fn):
        pass
    
