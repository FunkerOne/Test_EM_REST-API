# Задание 2: "GitHub API" тестирование 
Для тестирования был выбран сервис [GitHub API](https://api.github.com/) 

> Публичный API сервиса GitHub.

Тесты: 

[Создание репозитория](test_api.py)
- Проверка успешного создания и удаления репозитория

---
### Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
### Задать переменные окружения TOKEN, USER_NAME, TEST_REPO_NAME
```shell
dotenv set TOKEN <token>
dotenv set USER_NAME <username>
dotenv set TEST_REPO_NAME <repo_name> 
```
### Запустить тесты с подробным описанием
```shell
pytest -v
```