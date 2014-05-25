# import ripple
import praw
# import json
# import time
import secure
from test_account import rootAccountAddr, rootSeed


# user accounts:
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

    msgs = []
    currentInbox = list(redditObj.get_inbox())
    for msg in currentInbox:
        if isinstance(msg, praw.objects.Comment):
            newMsg = Tip(msg).get_tuple()
            msgs.append(newMsg)

            ## process comment for other variables

    return(msgs)

class Tip():
    def __init__(self, comment):
        self.username = comment.author.__str__()
        self.commentBody = comment.body
        self.tipAmount = None

    # def parseForTipAmounts(self):
        body = self.commentBody
        # encodes to ascii, splits by whitespace, reverses to get last bot mention
        body = body.encode("ascii", "ignore").split()[::-1]
        if '/u/wufaux-bot' in body:
            if body[body.index('/u/wufaux-bot') + 1] == 'wufi':
                self.tipAmount = body[body.index('wufi') + 1]

    def get_tuple(self):
        return((self.username, self.commentBody, self.tipAmount))



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
