from pr import GithubAPI

class Main:
    def __init__(self):
       git = GithubAPI()
       
       data = {
           
       }
       
       git.create_pull_request()
       

if __name__ == '__main__':
    Main()