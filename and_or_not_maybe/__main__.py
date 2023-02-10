from lexer import Lexer, TType

while True:
	text = input("[and_or_not_maybe] >>> ")
	l = Lexer(text)
	tokens = l.tokenize()

	print(*tokens)