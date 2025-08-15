import requests

# создать проект
key = ""
headers = {
"Authorization": key,
"Content-Type": "application/json"
}

base_url = "https://ru.yougile.com"

    # создать проект

def test_add_new():
    body={
  "title": "Skypro1"
}

    resp = requests.post(base_url+'/api-v2/projects', headers=headers, json=body) # Получаем список

    assert resp.status_code == 201

def test_edit_new():
    body={
  "title": "Skypro1"
}

    resp = requests.post(base_url+'/api-v2/projects', headers=headers, json=body)
    project_id = resp.json()["id"]
    body = {
        "title": "Skypro2"
    }
    resp = requests.put(base_url+'/api-v2/projects/'+project_id, headers=headers, json=body)

    assert resp.status_code == 200
    resp = requests.get(base_url + "/api-v2/projects/" + project_id, headers=headers)
    data = resp.json()
    assert data["title"] == "Skypro2"

def test_get_new():
    body={
  "title": "Skypro1"
}

    resp = requests.post(base_url+'/api-v2/projects', headers=headers, json=body)
    project_id = resp.json()["id"]

    resp = requests.get(base_url + "/api-v2/projects/" + project_id, headers=headers)
    data = resp.json()
    assert data["title"] == "Skypro1"

def test_add_new_negativ():
    body={
  "title": ""
}

    resp = requests.post(base_url+'/api-v2/projects', headers=headers, json=body) # Получаем список

    assert resp.status_code == 400

def test_edit_new_negativ():
    body={
  "title": "Skypro1"
}

    resp = requests.post(base_url+'/api-v2/projects', headers=headers, json=body)
    project_id = resp.json()["id"]
    body = {
        "title": ""
    }
    resp = requests.put(base_url+'/api-v2/projects/'+project_id, headers=headers, json=body)

    assert resp.status_code == 400

def test_get_new_negativ():

    resp = requests.get(base_url + "/api-v2/projects/" + "1", headers=headers)
    assert resp.status_code == 404