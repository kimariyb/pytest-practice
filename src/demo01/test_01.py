"""
1. 文件名：以 test_ 开头
2. 函数名：以 test_ 开头
3. 函数内容：包含断言，不能有返回值，必须返回 None
"""


def test_web():
    assert 1 == 1
    
    
def test_api():
    assert 1 == 2
    
class Test01:
    def __init__(self):
        pass
    
    def test_init(self):
        assert 1 == 100
