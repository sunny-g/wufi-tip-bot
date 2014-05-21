import ripple
# import json
# import test_account

client = ripple.Client("ws://127.0.0.1:6006")


# need to piece together a txn
#   follow example in serialize.py L:638 to form JSON object
#   also look to https://ripple.com/wiki/Example_API_Transactions#Trust_Set and others on that page
#




# may need to subscribe to server txn data streams for the DBa
#   the metadata is sent separately when streaming than when querying the ledger

