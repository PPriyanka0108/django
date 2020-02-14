class S:
	def __init__(self):
		self.name="pavan"
		S.name='Priyanka'
	@classmethod
	def s2(cls):
		print(cls.name)

s=S()
S.s2()
	