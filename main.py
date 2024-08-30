import os
from pr import GithubAPI


class Main:
    def __init__(self):

        # Enter repo owner and repo name
        repo_owner = ""
        repo_name = ""
        
        git = GithubAPI(repo_owner, repo_name)
        
        # Title
        title = "[TICKET-123]"
        
        # Body
        
        # Add Ticket and Ticket link here
        body = "**JIRA Ticket/Release** \n"
        body += "- [TXT-123](https://google.com) \n"
        body += "- [TXT-6969](https://google.com) \n" 
        
        body += "\n"
        
        # Add bullet here
        body += "**Description** \n"
        body += "- Fix Data Sync \n"
        body += "- Fix Data Sync \n"
        
        body += "\n"
        
        body += "Refer to the checklist "
        body += "[here](https://qualitytrade.atlassian.net/wiki/spaces/BDT/pages/2708307969/Pull+request+guidelines) \n"
        body += "- [x] Checklist covered"
        
        # Enter working branch
        head = "dev"
        
        # Enter branches you want to create PR for
        branches = [
            "test",
            "on-cloud",
        ]
        
        reviewers = [
            "iamgraypix",
            "karriv18"
        ]
        
        git.create_pull_request(head=head, branches=branches, body=body, title=title)
        #git.list_pulls("all")
        git.request_reviewers(reviewers)
        
if __name__ == '__main__':
    Main()