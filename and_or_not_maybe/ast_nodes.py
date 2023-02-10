class And:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.left} & {self.right})"

	def eval(self, INPUT_TABLE):
		return self.left.eval(INPUT_TABLE) & self.right.eval(INPUT_TABLE)

class Or(And):
	def __repr__(self):
		return f"({self.left} | {self.right})"

	def eval(self, INPUT_TABLE):
		return self.left.eval(INPUT_TABLE) | self.right.eval(INPUT_TABLE)

class Not:
	def __init__(self, input_):
		self.input = input_

	def __repr__(self):
		return f"!{self.input}"

	def eval(self, INPUT_TABLE):
		return int(not self.input.eval(INPUT_TABLE))

class Input(Not):
	def __repr__(self):
		return self.input

	def eval(self, INPUT_TABLE):
		return INPUT_TABLE[self.input]
