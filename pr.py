import requests as req
import os
import utils
from dotenv import load_dotenv

class GithubAPI:
    def __init__(self, repo_owner, repo_name):
        load_dotenv()
        self.token = os.getenv("TOKEN")
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        self.pull_number = []
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        
    def create_pull_request(self, body, head, branches, title):
        url = f"{self.base_url}/pulls"
        
        for i in range(len(branches)):
        
            payload = {
            "title": f"{title}/[{head}] -> {branches[i]}",
            "body": body,
            "head": head,
            "base": branches[i]
            }
            
            if not self.branch_exists(branches[i]):
                print(f"Branch {branches[i]} doesn't exist")
                break
            
            # Create PR
            request = req.post(url, json=payload, headers=self.headers)
            response = request.json()
            
            try:
                if request.status_code == 201:
                    print(f"Creating PR for {branches[i]}...")
                    print(f"Repo Owner / Repo Name: {self.repo_owner} / {self.repo_name}")
                    print(f"Successfully created PR at {utils.getToday()}")
                    print(f"{head} -> {branches[i]}")
                    print("--------------------------------------------------- \n")
                    self.pull_number.append(response['number'])
                print(f"Something went wrong while creating PR for {branches[i]}, please try again.")
            except Exception as e:
                print(f"An error occured: {e}")
                
    def branch_exists(self, branch_name):
        url = f"{self.base_url}/branches/{branch_name}"
        request = req.get(url, headers=self.headers)
        return request.status_code == 200

            
    def list_pulls(self, state):
        url = f"{self.base_url}/pulls"
        
        params = {
            "state": state 
        }
        
        res = req.get(url, headers=self.headers, params=params)
        
        if res.status_code == 200:
            prs = res.json()
            for pr in prs:
                pr_number = pr['number']
                pr_title = pr['title']
                pr_status = pr['state']
                print(f"PR #{pr_number}: {pr_title} - Status: {pr_status}")
    
      
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
        
        
        