from lexer import Lexer, TType
from parser_ import Parser
import readline

while True:
	text = input("[and_or_not_maybe] >>> ")
	l = Lexer(text)
	tokens = l.tokenize()

	p = Parser(tokens)
	ast = p.parse()

	print(*tokens)
	print(ast)