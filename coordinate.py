class Coordinate:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def __str__(self):
		return "(" + str(self.row) + "," + str(self.col) + ")"