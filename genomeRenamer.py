import os
import subprocess
import time

def main():
	print("Enter name of chart: ")
	chartName = input()
	print("Enter name of folder: ")
	targetFolder = input()

	#list to hold the names and corresponding accession numbers
	nameChart = list()
	#read in nameChart
	with open(chartName, "r") as fh:
		for line in fh:
			line = line.strip()
			line = line.split("\t")
			#remove space from binomial name
			name = line[0]
			name = name.split(" ")
			name = '_'.join(name)
			nameChart.append(tuple([name, line[1]]))
	#move into target folder
	os.chdir(targetFolder)
	for file in os.listdir():
		#check that file type is correct
		if file.endswith(".fna"):
			#find correct name in chart
			for entry in nameChart:
				if file.startswith(entry[1]):
					os.rename(file, entry[0] + "_" + entry[1] + "_genomic.fna")
	#return to starting folder
	os.chdir(os.path.dirname(os.getcwd()))



if __name__ == '__main__':
	main()

