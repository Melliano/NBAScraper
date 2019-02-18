import praw
import datetime


class Reddit:

    def __init__(self):
        self.reddit = praw.Reddit(client_id='P5SI_N8EYTPR4w', 
                                  client_secret='_P-Q3vMgMXzISX79Cx1kCoD85wQ', 
                                  user_agent='Melliano user agent here')   
        self.subreddit = self.reddit.subreddit('nba')
        self.gameThread = 'game thread'
        self.submissionsAlreadyRead = []

    def getGameThreads(self, subreddit, gameThread):
        # Get submissions objects of previous game thread
        # Limited to 100
        submissionsToBeRead = []
        for submission in subreddit.search(gameThread):
            if submission not in self.submissionsAlreadyRead:
                submissionsToBeRead.append(submission)
        return submissionsToBeRead

    def getCommentsFromGameThread(self, submission):
        # Allows for the comment limit of more comments
        # To be removed and returna flat response of all comments
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        counter = 0        
        for comment in comments:
            print(str(counter) + " -  " + comment.body + "\n")
            counter += 1
        self.submissionsAlreadyRead.append(submission)    
        self.saveGameThreadToFile(submission, comments)
        return comments

    def getCommentsForAllSubmissions(self, submissions):
        for submission in submissions:
            print(submission.title + "\n")
            self.getCommentsFromGameThread(submission)            

    def saveGameThreadToFile(self, submission, comments):
        file = open("test.txt", "w+")
        file.write(comments)
        file.close()        

if __name__ == "__main__":
    startTime = datetime.datetime.now()
    redditInstance = Reddit()
    submissions = redditInstance.getGameThreads(redditInstance.subreddit,                                    
                                                redditInstance.gameThread)                          
    print("Number of submissions - " + str(len(submissions)))    
    allComments = redditInstance.getCommentsForAllSubmissions(submissions)    
    endTime = datetime.datetime.now() - startTime    
    print("Finished in " + str(endTime))
