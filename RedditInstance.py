import praw


class Reddit:

    def __init__(self):
        self.reddit = praw.Reddit(client_id='P5SI_N8EYTPR4w', 
                                  client_secret='_P-Q3vMgMXzISX79Cx1kCoD85wQ', 
                                  user_agent='Melliano user agent here')   
        self.subreddit = self.reddit.subreddit('nba')
        self.gameThread = 'game thread'

    def getGameThreads(self, subreddit, gameThread):
        # Get submissions objects of previous game thread
        # Limited to 100
        submissions = []
        for submission in subreddit.search(gameThread):
            submissions.append(submission)
        return submissions

    def getCommentsFromGameThread(self, submission):
        comments = submission.comments.list()
        return comments


if __name__ == "__main__":
    redditInstance = Reddit()
    submissions = redditInstance.getGameThreads(redditInstance.subreddit,                                    
                                                redditInstance.gameThread)                          
    print("Number of submissions - " + str(len(submissions)))
