from pr import GithubAPI

class Main:
    def __init__(self):
        git = GithubAPI()
        
        title = "test2"
        body = "body"
        head = "dev"
        base = "main"
        ticket = "SI-320"
        
        branches = [
            "main",
            'staging',
            "release-a",
            "release-b",   
        ]
        
        git.create_pull_request(head=head, branches=branches, ticket=ticket, body=body)

if __name__ == '__main__':
    Main()