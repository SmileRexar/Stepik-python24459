import pytest

from SimpleApi.basic_Controller.get_method import describe_booking

res=(describe_booking(1))
print(res.text)

def test_status_code_is_200():
    assert res.status_code==200

@pytest.fixture
def test_response_include_mock():
    '''Check context'''
    assert ['lastname', 'firstname', 'totalprice'] in res.text