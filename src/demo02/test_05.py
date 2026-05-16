import pytest
        
    

@pytest.fixture(scope='session')
def data():
    return {} # 返回可变对象


class TestUser:
    def test_web(self, data):
        data['msg'] = "我是 User Web"
    
    def test_api(self, data):
        print("上一个用例是：", data['msg'])
        data['msg'] = "我是 User Api"
        
    
class TestGoods:
    def test_web(self, data):
        print("上一个用例是：", data['msg'])
        data['msg'] = "我是 Goods Api"
    
    def test_api(self, data):
        print("上一个用例是：", data['msg'])
        data['msg'] = "我是 Goods Api"
    
