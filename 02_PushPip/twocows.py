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

cow1_split = cow1.split('\n')
cow2_split = cow2.split('\n')

max_lenght_1 = max([len(i) for i in cow1_split])

max_weight_1 = len(cow1_split)
max_weight_2 = len(cow2_split)

if max_weight_1 > max_weight_2:
    cow2_split = [" "] * (max_weight_1 - max_weight_2) + cow2_split
else:
    cow1_split = [" "] * (max_weight_2 - max_weight_1) + cow1_split

for i in range(max(max_weight_1, max_weight_2)):
    len_line = len(cow1_split[i])
    print(cow1_split[i] + ' ' * (max_lenght_1 - len_line), cow2_split[i])
