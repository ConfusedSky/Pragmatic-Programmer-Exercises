"""
Generates a message signature struct in various different languages.

Uses a simple generic format in order to generate the message structs.
"""

import sys

if(len(sys.argv) < 2):
    print("Please enter an input file.");
    sys.exit();

with open(sys.argv[1], "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]

data = []
prevSplit = 0

for i, x in enumerate(content):
	if x == "":
		data.append(content[prevSplit:i])
		prevSplit = i+1
data.append(content[prevSplit:])

for c in data:
	print("{}".format(c))