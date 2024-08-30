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
        self.repo_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        self.user_url = f"https://api.github.com/users/";
        self.pull_number = []
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        
    def create_pull_request(self, body, head, branches, title):
        url = f"{self.repo_url}/pulls"
        
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
                else: 
                    print(f"Something went wrong while creating PR for {branches[i]}, please try again.")
            except req.RequestException as e:
                print(f"An error occured: {e}")
                
            
    def list_pulls(self, state):
        url = f"{self.repo_url}/pulls"
        
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
        
            payload = {
                "reviewers": reviewers
            }
            
        
            print(f"Requesting reviewers...")
            
            for i in range(len(self.pull_number)):
                
                reviewer = reviewers[i]
                pull = self.pull_number[i]
                
                url = f"{self.repo_url}/pulls/{pull}/requested_reviewers"
                
                if not self.user_exists(reviewer):
                    print(f"{reviewer} does not exists")
                    break
                else: 
                    req.post(url, json=payload, headers=self.headers)
                    print(f"Successfully requested reviewers -> {reviewers} -- PR # {pull}") 
                
                    
                    
        
    def branch_exists(self, branch_name):
        url = f"{self.repo_url}/branches/{branch_name}"
        request = req.get(url, headers=self.headers)
        return request.status_code == 200
    
    def user_exists(self, user):
        user_url = f"https://api.github.com/users/{user}"
        res = req.get(user_url, headers=self.headers)
        return res.status_code == 200 