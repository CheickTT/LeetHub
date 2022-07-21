import requests
from datetime import datetime
from pprint import pprint
import ast

def checkLeetCodeAccount(username):
    pass

def get_all_submissions(username):
    """Get all recent submited problems on github"""

    query="""query getRecentSubmissionList($username: String!) {
            recentSubmissionList(username: $username) {
                title
                titleSlug
                statusDisplay
                timestamp
                lang
            }


        }"""


    variables = {'username':username}
    request = requests.post(" https://leetcode.com/graphql", json={'query': query,'variables':variables})
    return request.json()

def user_stats_api(username):
    """Get user's submission statistics"""

    query="""query getUserProfile($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        
        matchedUser(username: $username) {
            
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                    submissions
                }
            }

            submissionCalendar

            profile {
                ranking
                reputation
                starRating
            }
        }
    }"""

    variables = {'username':username}
    request = requests.post(" https://leetcode.com/graphql", json={'query': query,'variables':variables})
    return request.json()

def get_user_stats(data):
    stats = data['data']['matchedUser']['profile']

    return {'ranking': stats['ranking'],'stars':stats['starRating']}


def get_submissions_difficulty(username):
    data = user_stats_api(username)
    difficulties = data['data']['allQuestionsCount']
    submissions = data['data']['matchedUser']['submitStats']['acSubmissionNum']
    results = {}
    for submission, difficulty in zip(submissions,difficulties):
        if submission['difficulty'] == 'All':
            results['solved'] = submission['count']
        else:
            results[submission['difficulty']] = str(submission['count']) +"/"+ str(difficulty['count'])

    return results

def get_submissions_date(username):   
    query ="""query getRecentSubmissionList($username: String!) {
            matchedUser(username: $username){

                submissionCalendar
                
            }

        }"""

    variables = {'username':username}
    request = requests.post(" https://leetcode.com/graphql", json={'query': query,'variables':variables})
    data = request.json()
    submissions = ast.literal_eval(data['data']['matchedUser']['submissionCalendar'])
    results = {}
    for date,count in submissions.items():
        time = datetime.fromtimestamp(int(date)).strftime("%m-%d-%Y")
        results[time] = count

    return results

def get_submissions(username):
    """Retrieve accepted submissions and languages"""
    all_submissions = get_all_submissions(username)
    submissions = all_submissions['data']['recentSubmissionList']
    ac_submissions = {}
    for submission in submissions:
        ac_submissions[submission['title']] = submission['lang']

    return ac_submissions