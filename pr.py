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
        self.txt_file = "logs.txt"
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
                    print(f"WORKING BRANCH: {head} -> MERGING BRANCH: {branches[i]}")
                    print("--------------------------------------------------- \n")
                    self.pull_number.append(response['number'])
                    utils.log(self.txt_file, f"Repo Owner / Repo Name: {self.repo_owner} / {self.repo_name}")
                    utils.log(self.txt_file, f"Sucessfully created PR for {head} -> {branches[i]} -> PR # {response['number']}")
                else: 
                    print(f"Something went wrong while creating PR for {branches[i]}, please try again.")
                    utils.log(self.txt_file, f"Something went wrong in {branches[i]}")
            except req.RequestException as e:
                print(f"An error occured: {e}")
                
            
    def list_pulls(self, state, per_page = 100, page = 1):
        url = f"{self.repo_url}/pulls"
        
        params = {
            "state": state,
            "per_page": per_page,
            "page": page 
        }
        
        res = req.get(url, headers=self.headers, params=params)
        
        if res.status_code == 200:
            prs = res.json()
            for pr in prs:
                pr_number = pr['number']
                pr_title = pr['title']
                pr_status = pr['state']
                print(f"PR #{pr_number}: {pr_title} - Status: {pr_status}")
                utils.log(self.txt_file, f"PR #{pr_number}: {pr_title} - Status: {pr_status}")
        
    def request_reviewers(self, reviewers):
        
            # payload = {
            #     "reviewers": reviewers
            # }
            
        
            # print(f"Requesting reviewers...")
            
            # for i in range(len(self.pull_number)):
                
            #     reviewer = reviewers[i]
            #     pull = self.pull_number[i]
                
            #     url = f"{self.repo_url}/pulls/{pull}/requested_reviewers"
                
            #     if not self.user_exists(reviewer):
            #         print(f"{reviewer} does not exists")
            #         break
            #     else: 
            #         req.post(url, json=payload, headers=self.headers)
            #         branch = self.get_branch(pull)
            #         print(f"Successfully requested reviewers -> {reviewers} -> PR # {pull}") 
            #         utils.log(self.txt_file, f"REVIEWERS: {reviewers} WORKING BRANCH: {branch[0].get("head")} MERGING BRANCH: {branch[0].get("base")} PR: ")

            print(f"Requesting reviewers...")

            for reviewer in reviewers:

                payload = {
                    "reviewers": [reviewer]
                }

                for i in range(len(self.pull_number)):

                    pull = pull_number[i]

                    url = f"{self.repo_url}/pulls/{pull}/requested_reviewers"

                    res = req.post(url, json=payload, headers=self.headers)

                    if res.status_code == 201:
                        branch = self.get_branch(pull)
                        print(f"Successfully requested reviewers -> {reviewer} -> PR # {pull}") 
                        utils.log(self.txt_file, f"REVIEWERS: {reviewer} WORKING BRANCH: {branch[0].get("head")} MERGING BRANCH: {branch[0].get("base")} PR: ")
                    else: 
                        utils.log(self.txt_file, f"Error: {res.json()}")


                    
                
    def branch_exists(self, branch_name):
        url = f"{self.repo_url}/branches/{branch_name}"
        request = req.get(url, headers=self.headers)
        return request.status_code == 200
    
    def user_exists(self, user):
        user_url = f"https://api.github.com/users/{user}"
        res = req.get(user_url, headers=self.headers)
        return res.status_code == 200 
    
    def get_branch(self, pr_number):
        url = f"{self.repo_url}/pulls/{pr_number}"
        request = req.get(url, headers=self.headers)
        response = request.json()
        
        return [ 
            {
            "head": response['head']['ref'],
            "base": response['base']['ref']
            }
        ] 
    
class PRFormatter:
    
    def body_mapper(self, tickets, descriptions):
        
        # Add Ticket and Ticket link here
        body = "**JIRA Ticket/Release** \n \n"
        body += self.add_ticket(tickets)
        
        body += "\n"
        
        # Add bullet here
        body += "**Description** \n"
        body += self.add_description(descriptions)
        
        body += "\n"
        
        body += "Refer to the checklist "
        body += "[here](https://qualitytrade.atlassian.net/wiki/spaces/BDT/pages/2708307968/Pull+request+guidelines) \n"
        body += "- [x] Checklist covered"  
        
        return body
        
    def add_ticket(self, tickets):
        format_tickets = []
        
        for ticket in tickets:
            format_tickets.append(f"- {ticket} \n")
            
        return "\n".join(format_tickets) 
    
    def add_description(self, descriptions): 
        format_descriptions = []
        
        for description in descriptions:
            format_descriptions.append(f"- {description} \n")
        
        return "\n".join(format_descriptions)        
