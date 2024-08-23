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
        
    def create_pull_request(self, body, head, branches, ticket):
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls"
        
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        
        
        for i in range(len(branches)):
        
            payload = {
            "title": f"[{ticket}]/[{head}] -> {branches[i]}",
            "body": body,
            "head": head,
            "base": branches[i]
            }
            
            print(f"Creating a PR for {branches[i]}")
            
            request = req.post(url, json=payload, headers=headers)
            response = request.json()
            
            # if(response['status'] != 199):
            #     print(f"Error creating PR {response['message']} at {utils.getToday()}")
            
            print(f"Successfully created PR at {utils.getToday()}")
            print(f"{head} -> {branches[i]} \n")