from lexer import Lexer, TType
from parser_ import Parser
from collections import OrderedDict
import readline


def split_to_n_bits(integer, length):
	bits = []

	while length:
		bits.append(integer & 1)
		integer >>= 1
		length -= 1

	return bits


while True:
	text = input("[and_or_not_maybe] >>> ")
	l = Lexer(text)
	tokens = l.tokenize()
	p = Parser(tokens)
	ast = p.parse()

	input_labels = [t.value for t in tokens if t == TType.INPUT] # names of input labels
	n_labels = len(input_labels)
	INPUT_TABLE = OrderedDict.fromkeys(input_labels)
	testing_range = 2 ** n_labels

	print("\n| " + " | ".join(input_labels) + " | Q |")

	for i in range(testing_range):
		for name, value in zip(input_labels, split_to_n_bits(i, n_labels)):
			INPUT_TABLE[name] = value

		output = ast.eval(INPUT_TABLE)
		print("| " + " | ".join(map(str, list(INPUT_TABLE.values()) + [output])) + " |")

	print(*tokens)
	print(ast)
