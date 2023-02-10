from enum import Enum
from string import ascii_letters

WHITESPACE = " \n\t"

class TType(Enum):
	INPUT = 0
	AND = 1
	OR = 2
	NOT = 3
	LPAREN = 4
	RPAREN = 5

OPERATORS = {"&": "AND", "|": "OR", "!": "NOT", "(": "LPAREN", ")": "RPAREN"}

class Token:
	def __init__(self, type_, value = None):
		self.type = type_
		self.value = value

	def __repr__(self):
		if self.value is not None:
			return f"Token({self.type}, {self.value})"

		return f"Token({self.type})"

	def __eq__(self, other):
		return self.type == other

class Lexer:
	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	def advance(self):
		self.current_char = next(self.text, None)

	def get_input_label(self):
		input_label = ""

		while self.current_char is not None and self.current_char in ascii_letters:
			input_label += self.current_char
			self.advance()

		return input_label

	def tokenize(self):
		tokens = []

		while self.current_char is not None:
			if (cc := self.current_char) in WHITESPACE:
				self.advance()
			elif cc in ascii_letters:
				input_name = self.get_input_label()
				tokens.append(Token(TType.INPUT, input_name))
			elif cc in OPERATORS:
				op_type = OPERATORS[cc]
				tokens.append(Token(TType[op_type]))
				self.advance()
			else:
				raise Exception(f"Invalid syntax: '{cc}'")

		return tokens