# anna.py

# im having a nasty problem with the large volume of
# documents i have. pdfs in particular
# i do have a system, but every now and then you find 
# that one that strays

# i want to be able to do a quick lookup
# let me know what i missed and where i can find them

# anna is from the reason why they're this much in
# the first place; i read a lot
# a bookie? a curious mind?
# anna could help me out

# problem defined, expected results described
# solution underway

# on my phone, we'll work with the sdcard alone
# walk the sdcard, picking those docs that are not 
# in ignored directories

import os
from operator import itemgetter

# defaults
default = [
	# filetypes
	['pdf', 'doc', 'docx', 'txt',],
	# ignore
	['airdroid', 'codde', 'code', 'download', 'documents',],
	# root ['c:/' or '/']
	'/',
]

class Settings():
	def __init__(self, mode):
		self.filetypes = mode[0]
		self.ignore = mode[1]
		self.root = mode[2]
		
		self.folders = 1
		self.files = 0

settings = Settings(default)
found = []

hello = """
hi, i'm anna, and i like to call myself a fileworm
i do the heavy lifting in finding files hidden in god knows where

@wrecodde
"""

help = """
usage and documentation coming up
"""

def setup():
	mode = input("use default options? (yes/no): ")
	
	if mode.lower() not in ['no', 'n', 'false']:
		print("using default options")
		settings = Settings(default)
		return
	
	print(hello)
	print(help)
	
	print("filetype filter (ex: pdf, docx)")
	filetypes = input("... ")
	
	print("folders to ignore (ex: documents, downloads)")
	ignore = input("... ")
	
	print("target folder [absolute path] ('c:' or '/' is the default)")
	root = input("... ")
	
	# parse inputs
	filetypes = [ext.strip() for ext in filetypes.split(',')]
	ignore = [dir.strip() for dir in ignore.split(',')]
	root = os.path.abspath(root)
	
	settings = Settings([filetypes, ignore, root])
	return

def start():
	for path, subdirs, files in os.walk(os.path.join(settings.root, '')):
		
		cdr = os.path.basename(path)
		sdr = len(subdirs)
		fls = len(files)
		
		for dir in subdirs:
			if dir in settings.ignore or dir.startswith('.'):
				subdirs.remove(dir)
		
		for file in files:
			split = os.path.splitext(file)
			ext = split[1].strip('.')
			if ext in settings.filetypes:
				find = {'ext': ext, 'file': file, 'cdr': cdr, 'path': os.path.abspath(cdr)}
				found.append(find)
		
		settings.folders += sdr
		settings.files += fls

def finish():
	# print("folders dug: ", settings.folders)
	# print("files poked: ", settings.files)
	
	strays = sorted(found, key=itemgetter('ext'))
	
	if not strays:
		print("no stray files were found")
	
	for find in strays:
		print(
			find['ext'].rjust(4),
			find['cdr'],
			find['file'],
			find['path'],)

setup()
start()
finish()

# not done.. but im bored now
