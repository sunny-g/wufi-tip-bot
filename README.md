wufi-tip-bot

Requires:

* miracle2k/ripple-python
* praw-dev/praw

NEED TO-DO:

* deal with non-perfect comments (input validation?, etc)
* use exceptions like a fucking professional
* testing (also something a fucking professional would do)
* store this shit in a db so I don't have to parse my entire inbox every time I start the server like a fucking n00b

WANT TO-DO:

*

WHERE I LEFT OFF AS OF THE END OF CODEDAY:

* figuring out the Comment obj and its attributes
* trying to get the author of the parent comment (may need to parse thru the entire submission Comment Tree to find our comment, then go back up the tree one level)
* need to store the comment_id or permalink (so I don't double spend and don't have to reparse the inbox)