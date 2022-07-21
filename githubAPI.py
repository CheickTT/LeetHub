from github import Github
import requests
import json
import pprint

def github_oath()

    headers = {
        "client_id": "Iv1.f336d7f755c7fc9d",
    }

    AUTH_URL = "https://github.com/login/oauth/authorize"

def github_tags(login, access_token)
    g = Github("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")
    BASE_URL = "https://api.github.com/users/" + login
    response = requests.get(BASE_URL).json()


    github_components = {"avatar_url": "", "url": "", "repos_url": ""}
    for resp in response:
        for github in github_components:
            if github == resp:
                github_components[github] = response[resp]

    avatar_icon = github_components["avatar_url"]
    repository = github_components["repos_url"]



    repository_names = []
    repo_request = requests.get(repository).json()
    for repo_dict in repo_request:
        for repo_dict in repo_request:
            r_components = {}
            for r in repo_dict:
                if r == "full_name":
                    r_components[r] = repo_dict[r]
                elif r == "description":
                    r_components[r] = repo_dict[r]
            
            repository_names.append(r_components)

    for rcontent in repository_names:
        repo = rcontent["full_name"]
        repo_content = g.get_repo(repo)

        print("----------------------------------------------------------------------------------------------")
        print("Description:")
        print(rcontent["description"])
        print("-------------------------------------------------")

        '''
        print("Workflows")
        for r in repo_content.get_workflows():
            print(r)
        print("-------------------------------------------------")
        '''

        print("Topics")
        for r in repo_content.get_topics():
            print(r)
        print("-------------------------------------------------")

        '''
        print("Projects")
        for r in repo_content.get_projects():
            print(r)
        print("-------------------------------------------------")
        '''

        print("Languages")
        for r in repo_content.get_languages():
            print(r)
        print("-------------------------------------------------")

login = input("Enter your Github username: ")
github_tags(login)


    
