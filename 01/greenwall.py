# python module to work with for unittesting

def implode(rf, armour, sheet=''):
	# where rf is reinforcement
	# and armour is used to attack the wall
	
	# implode is successful if armour is greater
	# than installed reinforcements
	
	if not sheet:
		return True if armour > rf else False
	else:
		return False if sheet + armour > rf else False

def get_region(city, country):
	return f"{city}, {country}.".title()

def get_region_pop(region, pop):
	region = region.title()
	return f"{region} - {pop}."

class GatePass():
	"""Provide a gate pass to gain access."""
	
	def __init__(self, pass_id):
		self.pass_id = pass_id
		self.pass_usage = []
	
	def show_id(self):
		"""Show the id on the gate pass."""
		print(pass_id)
	
	def use_pass(self, gate):
		"""Record a usage on the card."""
		self.pass_usage.append(gate)
	
	def show_usage(self):
		"""Show usages on the gate pass."""
		print("Pass Usage:")
		for use in self.pass_usage:
			print("- " + use)