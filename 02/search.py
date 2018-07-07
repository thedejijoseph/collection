from operator import attrgetter

index = {}

class Post:
	def __init__(self, post):
		# post here is a list of
		# attributes of a post
		self.id = post[0]
		self.body = post[1]
	
	def freq(self, word):
		return freq(self.body, word)

class Hit(Post):
	def __init__(self, post):
		super().__init__(post)
		
		self.score = 0
	
	def __repr__(self):
		return f"Post {self.id}; Score: {self.score}"

# search indexing
def add_to_index(post):
	postid = post.id
	post = post.body.split()
	for word in post:
		word = word.strip(".")
		word = word.strip(",")
		findings = index.get(word)
		if findings == None:
			index[word] = [postid]
		elif findings != None:
			if type(findings) == type(list()):
				findings.append(postid)
				index[word] = findings

# index querying
def index_pull(query):
	queries = query.split()
	pool = []
	for word in queries:
		sightings = index.get(word, [])
		for sight in sightings:
			pool.append(sight)
	# use set() to remove multiple occurences
	# make a list out of it
	pool = list(set(pool))
	return pool

# freq of word in the post
def freq(post, word):
	results = []
	def dig(post, word):
	    cursor = post.find(word)
	    if cursor == -1:
		    return results
	    else:
			# check if the found word is
		    if results == []:
			    results.append(cursor)
		    elif results != []:
			    new_cursor = results[-1] + len(word) + cursor
			    results.append(new_cursor)
		    cut = cursor + len(word)
		    dig(post[cut:], word)
	dig(post, word)
	return results

def rank(pool, query):
	# where pool is list of documents where the search query can be found
	# we'll try using a relative score for each post
	
	# frequency of query in post: 1 for each occurrence
	# multiple word queries as a single occurrence: 2
	
	results = []
	query = query.split()
	for post_id in pool:
		hit = Hit(posts[post_id-1])
		
		for word in query:
			freqs = freq(hit.body, word)
			hit.score += len(freqs)
		
		if hit.body.find(' '.join(query)) > 0:
			hit.score += 2
		
		results.append(hit)
	# i think freq returns 'the' in 'them' as an occurrence of 'the'
	# it is so not supposed to be
	return sorted(results, key=attrgetter("score"), reverse=True)

def search(query):
	pool = index_pull(query)
	results = rank(pool, query)
	
	if results:
		print(f"{len(results)} found")
		for hit in results:
			print("|", hit.body, "\n")
	else:
		print(f"{query} was not found in the database.")

posts = [
[1, "the cat ran out the door, and has failed to return"],
[2, "same did the dog. i fear evil has befallen tem all"],
[3, "what then has the world come to, it bereaves me so"],
[4, "that it's safe no more for the little ones"],
[5, "when is a man not a man? when he loses his word"],
[6, "do not make an enemy of the little guy"],
]

for post in posts:
	# make a post object
	post = Post(post)
	add_to_index(post)

# print(f"there are {len(posts)} post(s) in the corpus")
# query = input("search: ")

# search(query)

print(freq("gthem and the dog", "the"))
