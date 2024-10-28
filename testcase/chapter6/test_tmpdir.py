CONTENT="content"

def test_create_file(tmpdir):
    p= tmpdir.mkdir("sub").join("hello.txt")
    p.write(CONTENT)
    assert p.read()==CONTENT
    assert len(tmpdir.listdir())==1 #用于获取临时目录下的文件和子目录的列表
    assert 0 # 为了演示，强制置为失败
