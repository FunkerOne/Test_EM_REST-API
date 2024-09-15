import os
import requests
from dotenv import load_dotenv

load_dotenv()


class TestGithubApi:

    BASE_URL = 'https://api.github.com'
    TOKEN = os.getenv('TOKEN')
    TEST_REPO_NAME = os.getenv('TEST_REPO_NAME')
    USERNAME = os.getenv('USER')

    def setup_method(self):
        self.headers = {
            'Authorization': f'Bearer {self.TOKEN}',
            'Accept': 'application/vnd.github+json'
        }
        self.run_teardown = True

    def test_create_repo(self):
        repo_data = {
            'name': self.TEST_REPO_NAME,
            'private': False,
            'is_template': True
        }
        response = requests.post(f'{self.BASE_URL}/user/repos', headers=self.headers, json=repo_data)

        assert response.status_code == 201 and response.json()['name'] == self.TEST_REPO_NAME

    def teardown_method(self):
        if self.run_teardown:
            response = requests.delete(
                f'{self.BASE_URL}/repos/{self.USERNAME}/{self.TEST_REPO_NAME}', headers=self.headers
            )

            assert response.status_code == 204
