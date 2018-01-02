from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client()
client.testing = True

def test_index():
    global client
    resp = client.get('/')
    assert_response(resp, status=404)

    resp = client.get('/hello')
    assert_response(resp)

    resp = client.post('/hello')
    assert_response(resp, contains="Nobody")

    testdata = {'name': 'Tim', 'greet': 'Moin'}
    resp = client.post('/hello', data=testdata)
    assert_response(resp, contains="Tim")
