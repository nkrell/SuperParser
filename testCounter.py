import os

for file in os.listdir():
	with open(file, "r") as fh:
		counter = 0
		for line in fh:
			if line.startswith(">"):
				couter += 1
		print(file)
		print(couter)