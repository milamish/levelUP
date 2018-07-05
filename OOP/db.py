class user_db:
    def register(username,password):
	    db.update({username:password})

    def comment(username,comment):
	    db.update({username:comment})