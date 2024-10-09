import pytest


def test_record_property(record_property):
    record_property("test_id",10010)
    assert 1

def test_record_property2(record_xml_attribute):
    record_xml_attribute('test_id',10010)
    record_xml_attribute('classname','custom_classname')
    assert 1

@pytest.fixture(scope="session")
def log_global_env_facts(record_testsuite_property):
    record_testsuite_property("EXECUTOR","lkx")
    record_testsuite_property("LOCATION","GD")
    
def test_record_property3(log_global_env_facts):
    assert 1
