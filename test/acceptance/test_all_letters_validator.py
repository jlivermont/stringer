import requests
import pytest

PORT=8888

@pytest.fixture
def url():
    return 'http://localhost:{port}/all-letters-validator'.format(port=PORT)

@pytest.fixture
def headers():
    return {'Content-Type': 'application/json'}

@pytest.mark.parametrize('method', [
    ('put'),
    ('get'),
    ('delete'),
])
def test_unsupported_methods_return_405(method, url):
    response = requests.request(method, url)
    assert response.status_code == 405

def test_post_without_payload_returns_400(url):
    response = requests.post(url)
    assert response.status_code == 400

def test_post_with_improperly_formatted_payload_returns_400(url, headers):
    payload = {'foo': 'bar'}
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 400

def test_post_with_valid_payload_returns_200(url, headers):
    payload = {'string': 'abc'}
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200

@pytest.mark.parametrize('string,result', [
    ('abc', 'fail'),
    ('abcdefghijklmnopqrstuvwxyz', 'pass'),
])
def test_post_returns_expected_result_based_on_payload(string, result, url, headers):
    payload = {'string': string}
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()['result'] == result
