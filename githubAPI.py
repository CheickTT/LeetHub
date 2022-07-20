from github import Github
import requests
import json
import pprint

headers = {
    "client_id": "Iv1.f336d7f755c7fc9d",
}

AUTH_URL = "https://github.com/login/oauth/authorize"


g = Github("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")


login = input("Enter your Github username: ")
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
    r_components = {}
   for r in repo_dict:
       if r == "full_name":
            r_components[r] = repo_dist[r]
            print(r_components)
            repository_names.append(r_components.copy())
            break
    break

'''
for repo in repository_names:
    print(repo)


for r_names in repository_names:
    repo_content = g.get_repo(r_names)
    print("----------------------------------------------------------------------------------------------")

    print("Workflows")
    for r in repo_content.get_workflows():
        print(r)
    print("-------------------------------------------------")

    print("Topics")
    for r in repo_content.get_topics():
        print(r)
    print("-------------------------------------------------")

    print("Projects")
    for r in repo_content.get_projects():
        print(r)
    print("-------------------------------------------------")

    print("Languages")
    for r in repo_content.get_languages():
        print(r)
    print("-------------------------------------------------")
'''
    
