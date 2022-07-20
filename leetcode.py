import requests
#import leetcode

def get_all_submissions(username):
    """Get all recent submited problems on github"""

    query="""query getRecentSubmissionList($username: String!, $limit: Int) {
            recentSubmissionList(username: $username, limit: $limit) {
                title
                titleSlug
                statusDisplay
                lang
            }
        }"""

    variables = {'username':username}
    request = requests.post(" https://leetcode.com/graphql", json={'query': query,'variables':variables})
    return request.json()

def get_accepted_submissions(all_submissions):
    """Retrieve accepted submissions and languages"""
    submissions = all_submissions['data']['recentSubmissionList']
    ac_submissions = {}
    for submission in submissions:
        if submission['statusDisplay'] == "Accepted" and submission['title'] not in ac_submissions.keys():
            ac_submissions[submission['title']] = submission['lang']

    return ac_submissions