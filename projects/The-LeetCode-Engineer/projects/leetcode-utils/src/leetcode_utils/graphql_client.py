import json
from typing import Dict, List
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from leetcode_utils.leetcode_types import LCProblem, LCTopicTag

problem_query = """
            query getProblems($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
                problemsetQuestionList: questionList(
                  categorySlug: $categorySlug
                  limit: $limit
                  skip: $skip
                  filters: $filters
                ) {
                  total: totalNum
                  questions: data {
                    acRate
                    difficulty
                    freqBar
                    questionFrontendId
                    isFavor
                    isPaidOnly
                    status
                    title
                    titleSlug
                    topicTags {
                        name
                        id
                        slug
                    }
                    hasSolution
                    hasVideoSolution
                  }
                }
              }
        """
        
globalData_query = """
query:    
    query globalData {
        userStatus {
            userId
            isSignedIn
            isMockUser
            isPremium
            isVerified
            username
            realName
            avatar
            isAdmin
            isSuperuser
            permissions
            isTranslator
            activeSessionId
            checkedInToday
            completedFeatureGuides
            notificationStatus {
                lastModified
                numUnread
            }
        }
    }
"""

{"query":"\n    query userSessionProgress($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  matchedUser(username: $username) {\n    submitStats {\n      acSubmissionNum {\n        difficulty\n        count\n        submissions\n      }\n      totalSubmissionNum {\n        difficulty\n        count\n        submissions\n      }\n    }\n  }\n}\n    ","variables":{"username":"briancabbott"},"operationName":"userSessionProgress"}

{"query":"\n    query getStreakCounter {\n  streakCounter {\n    streakCount\n    daysSkipped\n    currentDayCompleted\n  }\n}\n    ","operationName":"getStreakCounter"}

cardInfo_query = """
# https://leetcode.com/problems/api/card-info/
# {
#     "categories": {
#         "0": [
#             {
#                 "title": "Algorithms",
#                 "url": "/problemset/algorithms/",
#                 "slug": "algorithms"
#             },
#             {
#                 "title": "Database",
#                 "url": "/problemset/database/",
#                 "slug": "database"
#             },
#             {
#                 "title": "Shell",
#                 "url": "/problemset/shell/",
#                 "slug": "shell"
#             },
#             {
#                 "title": "Concurrency",
#                 "url": "/problemset/concurrency/",
#                 "slug": "concurrency"
#             },
#             {
#                 "title": "JavaScript",
#                 "url": "/problemset/javascript/",
#                 "slug": "javascript"
#             },
#             {
#                 "title": "pandas",
#                 "url": "/problemset/pandas/",
#                 "slug": "pandas"
#             }
#         ],
#         "1": [
#             {
#                 "title": "LeetCode Curated Algo 170",
#                 "url": "/problemset/leetcode-curated-algo-170/",
#                 "slug": "leetcode-curated-algo-170"
#             },
#             {
#                 "title": "LeetCode Curated SQL 70",
#                 "url": "/problemset/leetcode-curated-sql-70/",
#                 "slug": "leetcode-curated-sql-70"
#             },
#             {
#                 "title": "Top 100 Liked Questions",
#                 "url": "/problemset/top-100-liked-questions/",
#                 "slug": "top-100-liked-questions"
#             },
#             {
#                 "title": "Top Interview Questions",
#                 "url": "/problemset/top-interview-questions/",
#                 "slug": "top-interview-questions"
#             },
#             {
#                 "title": "Top Amazon Questions",
#                 "url": "/problemset/top-amazon-questions/",
#                 "slug": "top-amazon-questions",
#                 "isPremium": true
#             },
#             {
#                 "title": "Top Facebook Questions",
#                 "url": "/problemset/top-facebook-questions/",
#                 "slug": "top-facebook-questions",
#                 "isPremium": true
#             },
#             {
#                 "title": "Top Google Questions",
#                 "url": "/problemset/top-google-questions/",
#                 "slug": "top-google-questions",
#                 "isPremium": true
#             },
#             {
#                 "title": "Top Microsoft Questions",
#                 "url": "/problemset/top-microsoft-questions/",
#                 "slug": "top-microsoft-questions",
#                 "isPremium": true
#             },
#             {
#                 "title": "Challenges for New Users",
#                 "url": "/problemset/challenges-for-new-users/",
#                 "slug": "challenges-for-new-users"
#             }
#         ]
#     }
# }


{"query":"\n    query dailyCodingQuestionRecords($year: Int!, $month: Int!) {\n  dailyCodingChallengeV2(year: $year, month: $month) {\n    challenges {\n      date\n      userStatus\n      link\n      question {\n        questionFrontendId\n        title\n        titleSlug\n      }\n    }\n    weeklyChallenges {\n      date\n      userStatus\n      link\n      question {\n        questionFrontendId\n        title\n        titleSlug\n        isPaidOnly\n      }\n    }\n  }\n}\n    ","variables":{"year":2024,"month":12},"operationName":"dailyCodingQuestionRecords"}



{"query":"\n    query GetMyStudyPlan($progressType: PlanUserProgressTypeEnum!, $offset: Int!, $limit: Int!) {\n  studyPlanV2UserProgresses(\n    progressType: $progressType\n    offset: $offset\n    limit: $limit\n  ) {\n    hasMore\n    total\n    planUserProgresses {\n      nextQuestionInfo {\n        inPremiumSubgroup\n        nextQuestion {\n          id\n          questionFrontendId\n          title\n          titleSlug\n          translatedTitle\n        }\n      }\n      nextQuestionInfo {\n        inPremiumSubgroup\n        nextQuestion {\n          id\n          questionFrontendId\n          title\n          titleSlug\n          translatedTitle\n        }\n      }\n      quittedAt\n      startedAt\n      plan {\n        questionNum\n        slug\n        premiumOnly\n        name\n        onGoing\n        highlight\n        cover\n      }\n      latestSubmissionAt\n      id\n      allCompletedAt\n      finishedQuestionNum\n    }\n  }\n}\n    ","variables":{"offset":0,"limit":3,"progressType":"ON_GOING"},"operationName":"GetMyStudyPlan"}


{"query":"\n    query codingChallengeMedal($year: Int!, $month: Int!) {\n  dailyChallengeMedal(year: $year, month: $month) {\n    name\n    config {\n      icon\n    }\n  }\n}\n    ","variables":{"year":2024,"month":12},"operationName":"codingChallengeMedal"}

{"query":"\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n    date\n    userStatus\n    link\n    question {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      hasVideoSolution\n      hasSolution\n      topicTags {\n        name\n        id\n        slug\n      }\n    }\n  }\n}\n    ","variables":{},"operationName":"questionOfToday"}


https://leetcode.com/problems/api/favorites/
 {
        "id": "9s08jp01",
        "name": "Challenges for New Users",
        "questions": [
            13,
            234,
            383,
            412,
            908,
            1444,
            1463,
            1791
        ],
        "type": "leetcode_favorites"
    },
    
{"query":"\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ","variables":{"categorySlug":"all-code-essentials","skip":0,"limit":100,"filters":{}},"operationName":"problemsetQuestionList"}

{"query":"\n    query questionCompanyTags {\n  companyTags {\n    name\n    slug\n    questionCount\n  }\n}\n    ","variables":{},"operationName":"questionCompanyTags"}


{"query":"\n    query GetProblemSetStudyPlanAds {\n  studyPlansV2AdQuestionPage {\n    cover\n    highlight\n    name\n    onGoing\n    premiumOnly\n    questionNum\n    slug\n  }\n}\n    ","variables":{},"operationName":"GetProblemSetStudyPlanAds"}

https://leetcode.com/api/banner/problemset_primary/
[{
        "name": "LICC-SD",
        "displayTitle": null,
        "subheading": null,
        "imageLink": "https://assets.leetcode.com/users/images/49479bba-73b3-45d2-9272-99e773d784b2_1687290663.3168745.jpeg",
        "targetLink": "https://datayi.cn/w/4RzynQL9"
    },
    ]
    
    

class LCGraphQLClient:
    def __init__(self):
        transport = AIOHTTPTransport(url="https://leetcode.com/graphql", headers={'Content-Type': 'application/json', 'Referer': 'https://leetcode.com'})
        self.client = Client(transport=transport, fetch_schema_from_transport=False)
    
    def get_all_problems(self) -> List[LCProblem]:
        self.get_problems('', 100, 0, {})
    
    def get_problems(self, category_slug: str, limit: int, skip: int, filters: Dict) -> List[LCProblem]:
        query = gql(problem_query)
        retrieved_count = 0
        retrieved_problems: List[Dict] = []
        params = {'categorySlug': category_slug, 'limit': limit, 'skip': retrieved_count, 'filters': filters}
        while True:
            result = self.client.execute(query, variable_values=params)
            retrieved_problems.extend(result['problemsetQuestionList']['questions'])
            retrieved_count += limit
            if retrieved_count >= result['problemsetQuestionList']['total']:
                break
        lcproblems = []
        for problem in retrieved_problems:
            lcproblems.append(LCProblem(problem['acRate'],
                problem['difficulty'],
                problem['freqBar'],
                problem['questionFrontendId'],
                problem['isFavor'],
                problem['isPaidOnly'],
                problem['status'],
                problem['title'],
                problem['titleSlug'],
                [LCTopicTag.from_dict(p) for p in problem['topicTags']],
                problem['hasSolution'],
                problem['hasVideoSolution']))    
        return lcproblems
    
    def get_global_data(self):
        query = gql(
            globalData_query
        )
        result = self.client.execute(query)
        return result
        

def main():
    p = LCGraphQLClient().get_all_problems()
    print([problem.to_json() for problem in p])