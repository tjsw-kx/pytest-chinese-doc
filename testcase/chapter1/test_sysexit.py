import pytest
def f():
    # 当你调用 raise SystemExit(1) 时，程序会引发一个 SystemExit 异常，
    # 传入的参数 1 通常表示程序以错误状态退出。一般来说，返回 0 表示成功，非零值（如 1）通常表示错误或异常。
    raise SystemExit(1)

def test_f():
    # with 主要作用是确保在代码块执行完成后，自动清理资源，比如关闭文件、释放网络连接、锁定对象等。
    '''这行代码使用了
    pytest
    的上下文管理器
    raises。它的作用是监视代码块中的异常。
    当代码块中引发
    SystemExit
    异常时，这个上下文管理器会捕获它，并且测试会通过。
    如果在代码块中没有引发
    SystemExit
    异常，那么测试将失败。
    '''
    with pytest.raises(SystemExit):
        f()
