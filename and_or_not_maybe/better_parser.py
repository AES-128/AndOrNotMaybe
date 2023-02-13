# shift-reduce

class Parser:
	def __init__(self):
		self.stack = []
		self.grammar = []
	
	def reduce(self):
		for non_terminal, rule in possible_reductions:
			if stack[-len(rule):] == rule:
