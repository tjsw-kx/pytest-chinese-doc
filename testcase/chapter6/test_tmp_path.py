CONTENT= "content"

def test_create_file(tmp_path):
    d= tmp_path / "sub"
    d.mkdir()  # 创建一个子目录
    p=d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1  # iterdir() 迭代目录，返回迭代器
    assert 0  # 为了展示，强制置为失败
    
