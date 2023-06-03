import requests

def test_add():
    data = {
        'username':'aaa',
        'password':'1234',
        'birthday':'2022-12-09',
    }
    r = requests.post("http://localhost:8000/user?", data=data)
    assert r.status_code == 200

def test_get1():
    r = requests.post("http://localhost:8000/token", data={
        "grant_type": "password",
        "username": "asdf",
        "password": "1234",
    })
    print(r.status_code, r.text)
    assert(r.status_code == 401)
    return r

def test_get2():
    r = requests.post("http://localhost:8000/token", data={
        "grant_type": "password",
        "username": "aaa",
        "password": "1234",
    })
    print(r.status_code, r.text)
    assert(r.status_code == 200)
    return r

def test_get3():
    r = requests.post("http://localhost:8000/token", data={
        "grant_type": "password",
        "username": "aaa",
        "password": "4321",
    })
    print(r.status_code, r.text)
    assert(r.status_code == 401)
    return r

def test_auth():
    r = test_get2()
    headers = {
        "Authorization": f"{r.json()['token_type']} {r.json()['access_token']}"
    }
    response = requests.get("http://localhost:8000/user", headers=headers)
    print(response.status_code)
    print(response.json())
    assert(response.json()['username'] == 'aaa')
    return headers

def test_update():
    headers = test_auth()
    response = requests.put("http://localhost:8000/user", headers=headers)

def test_delete():
    r = test_get2()
    headers = {
        "Authorization": f"{r.json()['token_type']} {r.json()['access_token']}"
    }
    response = requests.get("http://localhost:8000/user", headers=headers)
    print(response.status_code)
    print(response.json())
    assert(response.json()['username'] == 'aaa')
    return headers

if __name__ == '__main__':
    test_get2()