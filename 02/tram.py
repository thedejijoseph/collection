ticket=input("enter ticket number (6 digits): ")
#ticket="103100"


def valid(ticket):
	tmin=10**5; tmax=10**6-2
	
	try:
		ticket=int(ticket)
		if ticket >= tmin and ticket <= tmax:
			return True
		else:
			return False
	except:
		print(ticket, "is invalid")
		import sys; sys.exit(1)

def lucky(ticket):
	if valid(ticket):
		ticket=str(ticket)
		tk = [int(t) for t in ticket]
		
		a,b,c,d,e,f=tk
	
		fhalf=sum(tk[:3])
		shalf=sum(tk[3:])

		return True if fhalf==shalf else False
	else:
		print (ticket, "is invalid")
		import sys
        sys.exit(1)

def nextup(ticket):
	ticket=int(ticket)
	if valid(ticket):
		while valid(ticket):
			ticket+=1
			if lucky(ticket):
				print(f"next lucky ticket: {ticket}")
				break

print (f"is {ticket} lucky?: {lucky(ticket)}")
nextup(ticket)