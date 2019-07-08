# encode messages using a fairly light, quite insecure
# encryption trick

# mimi :: ma3ma3/

import random
message = input("message: ")

def mystify(msg):
	# encrypt message
	# return encrypted text
	
	sauce = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}
	hex = ""
	key = random.choice("aeiou")
	
	for char in msg:
		if char in "aeiou":
			hex += sauce.get(char)
		elif char in "bcdfghjklmnpqrstvwxyz":
			hex += char+key
		else:
			hex += char
	
	return hex

def demystify(hex):
	# decrypt message
	# return successfully decrypted message
	
	spice = {"1":"a", "2":"e", "3":"i", "4":"o", "5":"u"}
	msg = ""
	
	for char in hex:
		if char in "12345":
			msg += spice.get(char)
		elif char in "aeiou":
			msg += ""
		elif char in "bcdfghjklmnpqrstvwxyz":
			msg += char
		else:
			msg += char
	
	return msg

blergh = mystify(message)

print(blergh)
print(demystify(blergh))