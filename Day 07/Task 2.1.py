import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--penalty", type=int, default=12)

args = parser.parse_args()

print(args.penalty)