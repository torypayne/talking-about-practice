class BoardGame(object):
	"""docstring for BoardGame"""
	def __init__(self, name, minplayers, maxplayers):
		super(BoardGame, self).__init__()
		self.name = name
		self.minplayers = minplayers
		self.maxplayers = maxplayers
		def playable(self, players):
			print True
		self.fun = True


class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)