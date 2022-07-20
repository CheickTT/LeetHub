from github import Github
import requests
import json

headers = {
    "client_id": "Iv1.cbcdae36a6f3f2a6",
}

AUTH_URL = "https://github.com/login/oauth/authorize"
g = Github("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")

repo = g.get_repo("pylast/pylast")

print("Workflows")
for r in repo.get_workflows():
    print(r)
print("-----------------------------------------------------------------------------------")
print("Topics")
for r in repo.get_topics():
    print(r)
print("-----------------------------------------------------------------------------------")
'''
print("Projects")
for r in repo.get_projects():
    print(r)
print("-----------------------------------------------------------------------------------")
'''
print("Languages")
for r in repo.get_languages():
    print(r)
print("-----------------------------------------------------------------------------------")
print("Content")
for r in repo.get_contents():
    print(r)
print("-----------------------------------------------------------------------------------")
