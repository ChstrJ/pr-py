import requests as req
import os
from dotenv import load_dotenv

class GithubAPI:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TOKEN")
        self.repo_owner = os.getenv("REPO_OWNER")
        self.repo_name = os.getenv("REPO_NAME")
        self.base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        
    def create_pull_request(self, head, base, title, body, ticket_no, link):
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls"
        
        headers = {
            "Authorization": "Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": 2022-11-28
        }
        
        payload = {
            title: title,
            body: body,
            head: head,
            base: base
        }
        
        try:
            response = req.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print("Success PR!")
                return response.json()
            return response.json()
        except Exception as e:
            raise(f"Something went wrong: {e}")
        
        
        