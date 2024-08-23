import requests as req
import os
import utils
from dotenv import load_dotenv

class GithubAPI:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TOKEN")
        self.repo_owner = os.getenv("REPO_OWNER")
        self.repo_name = os.getenv("REPO_NAME")
        self.base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        self.pull_number = []
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        
    def create_pull_request(self, body, head, branches, ticket):
        url = f"{self.base_url}/pulls"
        
        for i in range(len(branches)):
        
            payload = {
            "title": f"[{ticket}]/[{head}] -> {branches[i]}",
            "body": body,
            "head": head,
            "base": branches[i]
            }
            
            print(f"Creating a PR for {branches[i]}")
            
            request = req.post(url, json=payload, headers=self.headers)
            response = request.json()
            
            if request.status_code == 201:
                print(f"Successfully created PR at {utils.getToday()}")
                print(f"{head} -> {branches[i]} \n")
                self.pull_number.append(response['number'])
            
            
    def request_reviewers(self, reviewers):
        
        for i in range(len(reviewers)):
            url = f"{self.base_url}/pulls/{self.pull_number[i]}/requested_reviewers"
            
            payload = {
                "reviewers": reviewers[i]
            }
            
            res = req.post(url, json=payload, headers=self.headers)
            
            print(f"Requesting reviewers: {reviewers[i]}")
            
            if res.status_code == 201:
                print("Reviewers successfully requested. \n")
        
        
        