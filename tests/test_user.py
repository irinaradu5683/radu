from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Существующие пользователи для тестов
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    '''Получение существующего пользователя'''
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    '''Попытка получить несуществующего пользователя'''
    response = client.get("/api/v1/user", params={'email': 'nonexistent@mail.com'})
    assert response.status_code == 404
    assert response.json()['detail'] == "User not found"

def test_create_user():
    '''Создание нового пользователя'''
    new_user = {'name': 'Anna Ivanova', 'email': 'anna.ivanova@mail.com'}
    response = client.post("/api/v1/user", json=new_user)
    assert response.status_code == 201
    assert isinstance(response.json(), int)  # возвращается ID нового пользователя

def test_create_user_conflict():
    '''Попытка создать пользователя с уже существующим email'''
    existing_user = {'name': 'Ivan Ivanov', 'email': users[0]['email']}
    response = client.post("/api/v1/user", json=existing_user)
    assert response.status_code == 409
    assert response.json()['detail'] == "User with this email already exists"

def test_delete_user():
    '''Удаление пользователя'''
    # Сначала создаём пользователя для удаления
    new_user = {'name': 'Test User', 'email': 'test.user@mail.com'}
    client.post("/api/v1/user", json=new_user)
    # Теперь удаляем
    response = client.delete("/api/v1/user", params={'email': new_user['email']})
    assert response.status_code == 204
    # Проверка, что пользователя больше нет
    response = client.get("/api/v1/user", params={'email': new_user['email']})
    assert response.status_code == 404
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Существующие пользователи для тестов
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    '''Получение существующего пользователя'''
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    '''Попытка получить несуществующего пользователя'''
    response = client.get("/api/v1/user", params={'email': 'nonexistent@mail.com'})
    assert response.status_code == 404
    assert response.json()['detail'] == "User not found"

def test_create_user():
    '''Создание нового пользователя'''
    new_user = {'name': 'Anna Ivanova', 'email': 'anna.ivanova@mail.com'}
    response = client.post("/api/v1/user", json=new_user)
    assert response.status_code == 201
    assert isinstance(response.json(), int)  # возвращается ID нового пользователя

def test_create_user_conflict():
    '''Попытка создать пользователя с уже существующим email'''
    existing_user = {'name': 'Ivan Ivanov', 'email': users[0]['email']}
    response = client.post("/api/v1/user", json=existing_user)
    assert response.status_code == 409
    assert response.json()['detail'] == "User with this email already exists"

def test_delete_user():
    '''Удаление пользователя'''
    # Сначала создаём пользователя для удаления
    new_user = {'name': 'Test User', 'email': 'test.user@mail.com'}
    client.post("/api/v1/user", json=new_user)
    # Теперь удаляем
    response = client.delete("/api/v1/user", params={'email': new_user['email']})
    assert response.status_code == 204
    # Проверка, что пользователя больше нет
    response = client.get("/api/v1/user", params={'email': new_user['email']})
    assert response.status_code == 404

