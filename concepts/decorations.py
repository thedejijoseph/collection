

def secure(action, *args, **kwargs):
	def auth(*args):
		print("**", args)
		return action(*args)
	return auth

def logout():
	print("logging out")

@secure
def login():
	print("logged in")

login()