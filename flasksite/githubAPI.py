from github import Github as gH
import requests


# from flask_bcrypt import Bcrypt
# from forms import RegistrationForm, LoginForm, SearchForm, PostForm
# from flask_behind_proxy import FlaskBehindProxy
# from flask_sqlalchemy import SQLAlchemy
# from model import User,MyChart,circleChart

def github_oath():

    headers = {
        "client_id": "Iv1.f336d7f755c7fc9d",
    }

    AUTH_URL = "https://github.com/login/oauth/authorize"

def github_tags(user_dict, access_token):
    g = gH(access_token)
    # BASE_URL = "https://api.github.com/users/" + login
    response = user_dict
    # print(response)

    github_components = {"avatar_url": "", "url": "", "repos_url": ""}
    for resp in response:
        for github in github_components:
            if github == resp:
                github_components[github] = response[resp]

    avatar_icon = github_components["avatar_url"]
    repository = github_components["repos_url"]

    # {
    #     user:
    #     profile_pic
    #     repos: [{name, description, languages=[]},]

    # }


    repositories = []
    repo_request = requests.get(repository).json()
    for repo_dict in repo_request:
        r_components = {}
        for r in repo_dict:
            if r in ["full_name", "name", "description"]:
                r_components[r] = repo_dict[r]

        
        repositories.append(r_components)
    
    for repo in repositories:
        repo_obj = g.get_repo(repo["full_name"])
        languages = []
        for lang in repo_obj.get_languages():
            languages.append(lang)
        
        repo['languages'] = languages

    user_info = {}
    user_info['pic_url'] = avatar_icon
    user_info['repositories'] = repositories
    return user_info
    # print(f"user_info: {user_info}")

    # for rcontent in repositories:
    #     repo = rcontent["full_name"]
    #     repo_content = g.get_repo(repo)

    #     print("Repo Name")
    #     print(rcontent["name"])
    #     print("----------------------------------------------------------------------------------------------")
    #     print("Description:")
    #     print(rcontent["description"])
    #     print("-------------------------------------------------")


    #     print("Languages")
    #     for r in repo_content.get_languages():
    #         print(r)
    #     print("-------------------------------------------------")

# login = input("Enter your Github username: ")
# github_tags(login)


