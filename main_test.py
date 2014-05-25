import praw
import secure
import main

redditCxn = praw.Reddit('practice-praw-bot')
redditCxn.login('wufaux-bot', secure.password)

# returns the unicode body of the comment
# commentBody = main.parse_inbox(redditCxn)[0][1]

# prints the parsedComment
parsedComment = main.parse_inbox(redditCxn)
print parsedComment