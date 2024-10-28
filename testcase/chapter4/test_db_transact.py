import pytest

class Db:
    def __init__(self):
        self.intransaction =[]
    def begin(self,name):
        self.intransaction.append(name)
    def rollback(self):
        self.intransaction.pop()

@pytest.fixture(scope="module")
def db():
    return Db()

class TestClass:
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        # 用request.function.__name__来获取当前正在执行的测试函数的名称
        db.begin(request.function.__name__)
        yield
        db.rollback()
        
    def test_method1(self,db):
        assert db.intransaction == ["test_method1"]
        
    def test_method2(self,db):
        assert db.intransaction == ["test_method2"]
