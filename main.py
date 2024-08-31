import os
from pr import GithubAPI, PRFormatter


class Main:
    def __init__(self):
        os.system("clear")

        # Enter repo owner and repo name
        repo_owner = ""
        repo_name = ""
        
        git = GithubAPI(repo_owner, repo_name)
        pr_format = PRFormatter()
        
        # Add title here
        title = "[TICKET-123]"
        
        # Add tickets here
        tickets = [
            "[IAS-22](https://google.com)",
            "[IAS-222](https://google.com)" 
        ]
        
        # Add descriptions here
        descriptions = [
            "Desc1",
            "Desc2"
        ]
        
        # Enter working branch
        head = "dev"
        
        # Enter branches you want to create PR for
        branches = [
            "test",
            "on-cloud"
        ]
        
        # Add username of reviewers here
        reviewers = [
            "iamgraypix",
            "karriv18"
        ]
        
        body = pr_format.body_mapper(tickets, descriptions)
        
        git.create_pull_request(head=head, branches=branches, body=body, title=title)
        git.request_reviewers(reviewers)
        #git.list_pulls("all")
        
if __name__ == '__main__':
    Main()