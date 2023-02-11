from ast_nodes import *
from lexer import TType

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def advance(self):
		self.current_token = next(self.tokens, None)

	def parse(self):
		return self.parse_bool_expr()

	def parse_bool_expr(self):
		bool_expr = self.parse_term()

		while self.current_token == TType.OR:
			self.advance()
			right_term = self.parse_term()
			bool_expr = Or_Node(bool_expr, right_term)

		return bool_expr

	def parse_term(self):
		term = self.parse_factor()

		while self.current_token == TType.AND:
			self.advance()
			right_factor = self.parse_factor()
			term = And_Node(term, right_factor)

		return term

	def parse_factor(self):
		t = self.current_token

		match t:
			case TType.LPAREN:
				self.advance()
				bool_expr = self.parse_bool_expr()

				if self.current_token != TType.RPAREN:
					raise Exception("Missing ')'")

				self.advance()
				return bool_expr
			case TType.INPUT:
				self.advance()
				return Input_Node(t.value)
			case TType.NOT:
				self.advance()
				return Not_Node(self.parse_factor())