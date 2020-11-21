import secrets

class ab :
	def __init__(self) :
		self.a = secrets.randbits(256)
		self.b = secrets.randbits(256)