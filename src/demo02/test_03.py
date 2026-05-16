import pytest
import datetime


class TestClass:
    @pytest.mark.api
    def test_01(self):
        assert 1 == 1
        
    @pytest.mark.web
    def test_02(self):
        assert 1 == 2
        

@pytest.fixture
def fixture_function(): 
    # 前置操作
    print(1)
    print(2)
    # 使用生成器
    yield
    
    # 后置操作
    print(3)
    

@pytest.fixture
def fixture_fn_v2():
    print("用例的开始时间：", datetime.datetime.now())
    yield
    print("用例的结束时间：", datetime.datetime.now())
    
    
@pytest.mark.usefixtures('fixture_fn_v2')
def test_fixture():
    print('我是测试用例 1')
    
@pytest.mark.usefixtures('fixture_fn_v2')
def test_web():
    print('我是测试用例 2')

@pytest.mark.usefixtures('fixture_fn_v2')
def test_api():
    print('我是测试用例 3')