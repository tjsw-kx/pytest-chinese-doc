
class Foo:
    def __init__(self, val):
        self.val = val
        
    def __str__(self,other):
        return self.val == other.val

    def __repr__(self):
        return str(self.val)
def test_foo_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2

# from test_foo_compare import Foo
# def pytest_foo_compare(op,left,right):
#     if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
#         return [
#             "比较两个 Foo 实例:",
#             "   值: {} != {}".format(left.val, right.val),
#         ]

