class And_Node:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.left} & {self.right})"

	def eval(self, INPUT_TABLE):
		return self.left.eval(INPUT_TABLE) & self.right.eval(INPUT_TABLE)

class Or_Node(And_Node):
	def __repr__(self):
		return f"({self.left} | {self.right})"

	def eval(self, INPUT_TABLE):
		return self.left.eval(INPUT_TABLE) | self.right.eval(INPUT_TABLE)

class Not_Node:
	def __init__(self, input_):
		self.input = input_

	def __repr__(self):
		return f"!{self.input}"

	def eval(self, INPUT_TABLE):
		return int(not self.input.eval(INPUT_TABLE))

class Input_Node(Not_Node):
	def __repr__(self):
		return self.input

	def eval(self, INPUT_TABLE):
		return INPUT_TABLE[self.input]
