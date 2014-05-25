# import ripple
import praw
# import json
# import time
import secure
from test_account import rootAccountAddr, rootSeed


# reddit accounts:
#   djarum-root:        mapped to the rootAccountAddr and rootSeed
#   djarum-dummie1:     a dummie account to leave comments
#   wufaux-bot:         a bot to process comments
#   myusername:         moderator for the r/djarum test sub

# clientConnection = ripple.Client("ws://127.0.0.1:6006")


###########################################
###########################################
###########################################
#  PRAW STUFF
#   praw.objects.Comment is a comment obj
#       this is the object we want when parsing our inbox for tips
#       ergo, we need to sift through only these objects and get their:
#           commenter_username
#           op_of_comment
#           comment_id (so we don't double count comments)

botPassword = secure.password
botUserAgent = "practice-tip-bot"
redditCxn = praw.Reddit(user_agent=botUserAgent)
redditCxn.login('wufaux-bot', password=botPassword)

##########################################

def parse_inbox(redditObj):
    '''Takes obj of type Reddit and returns a list of tuples containing Tip attributes'''
    msgs_as_tips = []
    comments = []
    currentInbox = list(redditObj.get_inbox())
    for msg in currentInbox:
        if isinstance(msg, praw.objects.Comment):
            comments.append(msg)
            newMsg = Tip(msg).get_tuple()
            msgs_as_tips.append(newMsg)
    return(msgs_as_tips, comments)

class Tip():
    # should inherit from Comment type, since it is already taking a Comment obj in
    def __init__(self, tip_comment):
        self.username = tip_comment.author.__str__()
        self.commentBody = tip_comment.body
        self.tipAmount = None

    # get tip amounts
        '''Currently, only gets tips if they mention of /u/wufaux-bot at the end of the comment'''
        body = self.commentBody
        # encodes to ascii, splits by whitespace, reverses to get last bot mention
        body = body.encode("ascii", "ignore").split()[::-1]
        if '/u/wufaux-bot' in body:
            if body[body.index('/u/wufaux-bot') + 1] == 'wufi':
                self.tipAmount = body[body.index('wufi') + 1]

    # if tip_comment.is_root():
    #   self.recipient = postAuthor
    # else:
    #   self.recipient =

    # get recipient's username


    def get_tuple(self):
        return(self.username, self.commentBody, self.tipAmount)



# code for piecing together a txn
#   follow example in serialize.py L:638 to form JSON object
#   also look to https://ripple.com/wiki/Example_API_Transactions#Trust_Set and others on that page
#   also look to rsign.py for ex txn and use of signing stuff

exampleTrustSet_txblob = '''
    "tx_json" : {
      "TransactionType" : "TrustSet",
      "Account" : "rMmTCjGFRWPz8S2zAUUoNVSQHxtRQD4eCx",
      "LimitAmount" : { "currency" : "USD", "value" : "100", "issuer" : "r3kmLJN5D28dHuH8vZNUZpMC43pEHpaocV" }
      "Flags" : "65536"
    },
'''





# may need to subscribe to server txn data streams for the DB
#   the metadata is sent separately when streaming than when querying the ledger



# code for generating secret and address
