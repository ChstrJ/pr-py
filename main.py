from pr import GithubAPI

class Main:
    def __init__(self):
        git = GithubAPI()
        
        # Title
        title = "[IAF-123][IAF-6969][HOTFIX]"
        
        # Body
        body = "**JIRA Ticket/Release** \n"
        body += "- [IAF-123](https://google.com) \n"
        body += "- [IAF-6969](https://google.com) \n" 
        body += "\n"
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
            "main",
            "release-a",
            "release-b"
        ]
        
        git.create_pull_request(head=head, branches=branches, body=body, title=title)
        #git.list_pulls("all")
        #git.request_reviewers(reviewers)

if __name__ == '__main__':
    Main()