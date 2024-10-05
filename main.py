import os
from pr import GithubAPI, PRFormatter
import utils


class Main:
    def __init__(self):
        os.system("clear")

        # Enter repo owner
        repo_owner = ""
                
        # Initialize value 
        repo_name = ""
        title = ""
        head = ""
        tickets = []
        descriptions = []
        branches = []
        
        
        # Default branches modify if needed.
        release = [
            "release/2.1.0",
            "release/2.1.0-b",
            "release/2.1.0-a",
            "develop",
            "master"
        ]
        
        default_branches = release
        
        while True:
            
            while not repo_name:
                repo_name = input("Enter repo name: ")
            
            while not head:
                head = input("Input working branch: ")
                
            while not title:
                title = input("Input title: ")
            
            while True:
            
                ticket = input("Enter ticket: ")
                tickets.append(ticket)
                
                condition = input("Do you want to add more ticket? (y/n): ").strip().lower()
                
                if condition != "y":
                    break 
                
            while True:
                description = input("Enter description: ")
                descriptions.append(description)
                
                condition = input("Do you want to add more description? (y/n): ").strip().lower()
                
                if condition != "y":
                    break
                
            while True:
                print("Default branches: ", default_branches)
                ask = input("Do you want to enter branches or go with the default? (y = yes / d = default): ").strip().lower()
                
                while True:
                    
                    if ask == "y":
                
                        branch = input("Enter branch: ")
                        branches.append(branch)
                
                        condition = input("Do you want to add more branch? (y/n): ").strip().lower()
                
                        if condition != "y":
                            break
                    
                    elif ask == "d":
                        print("Default branches: ", default_branches)
                        branches = default_branches
                        break
                    else:
                        exit()
                break
            
            break
        
        
        # Add username of reviewers here
        reviewers = utils.getVuReviewers()
        
        git = GithubAPI(repo_owner, repo_name)
        pr_format = PRFormatter()
        
        body = pr_format.body_mapper(tickets, descriptions)
        
        git.create_pull_request(head=head, branches=branches, body=body, title=title)
        git.request_reviewers(reviewers)
        #git.list_pulls("all")
        
        
if __name__ == '__main__':
    Main()