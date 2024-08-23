from pr import GithubAPI

class Main:
    def __init__(self):
        git = GithubAPI()
        
        title = "test2"
        body = "body"
        head = "dev"
        ticket = "SI-320"
        
        # Body
        body = "TEST TEST"
        
        
        # Enter branches you want to create PR for
        branches = [
            "main",
            'staging',
            "release-a",
            "release-b",   
        ]
        
        reviewers = [
            "nerdydaemon10",
        ]
        
        git.create_pull_request(head=head, branches=branches, ticket=ticket, body=body)
        #git.request_reviewers(reviewers)

if __name__ == '__main__':
    Main()