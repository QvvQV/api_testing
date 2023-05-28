from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert

def test_regist():
    email = 'eve.holt@reqres.in'
    password = '123'

    res = api.regist(email, password)



    assert res.status_code == HTTPStatus.CREATED
    Assert.validate_schema(res.json())

def test_valid():
    email = 'eve.holt@reqres.in'

    res = api.valid_regist(email)
    res_body = res.json()
    example = {
            'error': 'Missing password'
    }

    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.json())
    assert example == res_body
