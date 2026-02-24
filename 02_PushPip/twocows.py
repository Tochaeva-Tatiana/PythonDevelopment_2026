from cowsay import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message_1")
parser.add_argument("-E", default="oo", type=str)
parser.add_argument("-F", default=None, type=str)
parser.add_argument("-N", action="store_true")

parser.add_argument("message_2")
parser.add_argument("-e", default="oo", type=str)
parser.add_argument("-f", default=None, type=str)
parser.add_argument("-n", action="store_true")


args = parser.parse_args()
cow1 = cowsay(args.message_1, eyes = args.e, cow=args.f, wrap_text=not(args.n))
cow2 = cowsay(args.message_2, eyes = args.E, cow=args.F, wrap_text=not(args.N))


print(cow1)
print(cow2)