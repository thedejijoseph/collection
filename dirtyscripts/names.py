with open("names.txt", "r") as file:
	doc = file.read().splitlines()
	
	# first, those numbers come off
	for line in doc:
		if line.isdigit():
			doc.remove(line)
	
	# lets work with just what we need
	doc = doc[13:]
	
	names = []
	numbers = []
	
	# remove empty spaces
	for line in doc:
		if line == "" or line == " ":
			doc.remove(line)
	
	# split names and matric numbers
	for line in doc:
		if line.startswith("TMT") is False:
			names.append(line)
		elif line.startswith("TMT"):
			numbers.append(line)
	
	class_ = []
	
	# redo the class list
	for no in range(1, 76):
		person = f"{numbers[no-1]} >> {names[no-1]}"
		class_.append(person)
	
	# write that to a file 
	with open("class.txt", "w") as tmt:
		for person in class_:
			tmt.write(person+"\n")