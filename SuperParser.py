import os
import subprocess
import time

def main():
	# while True:
	# 		try:
	# 			print("Enter name of folder containing genomes for parsing: ")
	# 			targetFolder = input()
	# 			if targetFolder not in os.listdir():
	# 				raise ValueError
	# 			else:
	# 				pass
	# 		except ValueError:
	# 			print("Folder not found.")
	# 		except FileNotFoundError:
	# 			print("Folder not found.")
	# 		else:
	# 			break
	# 	#navigate into target folder
	# os.chdir(targetFolder)

	#FOR DEBUGGING----------------------------------------------------------------------------
	# GeneFileList = list()
	# for file in os.listdir():
	# 	currentFile = GeneFile(file)
	# 	GeneFileList.append(currentFile)

	# for file in GeneFileList:
	# 	file.readFile()

	# for file in GeneFileList:
	# 	file.printFastaEntries()
	# 	file.normalClean()
	# 	file.printCleanedGenes()
	# 	file.findGeneTypes()
	# 	file.printGeneTypes()
	# 	testList = file.geneTreeFormat()
	# 	for entry in testList:
	# 		print(entry[0])
	# 		print(entry[1])

	#os.chdir(os.path.dirname(os.getcwd()))

	print("Enter name of chart: ")
	chartName = input()
	print("Enter name of folder: ")
	targetFolder = input()
	fileRename(chartName, targetFolder)

#======================================================NOTE=======================: Finished with renamer, need to make geneTree method work


#method for renaming files
#only works with tab-delimited name charts in the format name [tab] accession
def fileRename(chartName, targetFolder):
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
		if file.endswith(".clean.fasta"):
			#find correct name in chart
			for entry in nameChart:
				if file.startswith(entry[1]):
					os.rename(file, entry[0] + "_" + entry[1] + ".clean.fasta")
	#return to starting folder
	os.chdir(os.path.dirname(os.getcwd()))

#method for writing output files that can be used to make a gene tree
def geneTree():
	pass


class GeneFile:
	def __init__(self, fileName):
		#initialized with only fileName, the rtest is filled in once the file is read
		self.fileName = fileName
		#not all of these attributes need to be populated, some may be left unused
		#the name of the sample
		self.sampleName = "None"
		#the species of the sample
		self.species = "None"
		#the type of tissue the smaple was taken from, in genomes this will be null
		self.tissue = "None"
		#boolean that trakcs wether the data is from a genome or from rnaSeq data, set to genome by default
		self.isGenome = True
		#the raw fasta entries, made up of headers and sequences, populated by a class method
		self.fastaEntries = list()
		#the cleaned genes, made up of a type, a coding status, and a sequence
		#this doesnt not have to be performed
		self.cleanedGenes = list()
		#a list of the types of gene found in the file, genes of the same family are counted separately based on coding status
		self.geneTypes = list()
		#a list of the number of genes in each gene type, made up of a gene type and a count
		self.geneCounts = list()

	#class method for reading in data from file
	def readFile(self):
		#temporary varibles for holding the header and sequence
		tempHeader = ""
		tempSeq = ""
		#open the file
		with open(self.fileName) as fh:
			for line in fh:
				#remove line breaks from each line
				line = line.strip("\n")
				#if the line is a header
				if line.startswith(">"):
					#check if seq has been populated yet
					if tempSeq == "":
						tempHeader = line
					elif tempSeq != "":
						#add entry to list
						self.fastaEntries.append(tuple([tempHeader, tempSeq]))
						#change header to new line
						tempHeader = line
						#dump tempSeq memory
						tempSeq = ""
				else:
					tempSeq += line
		#add last entry as there are no more ">" to signal the final addition
		self.fastaEntries.append(tuple([tempHeader, tempSeq]))

	#class method for printing all fasta entries
	def printFastaEntries(self):
		#check if fastaEntries list is empty
		if len(self.fastaEntries) == 0:
			print("fastaEntries is empty")
		else:
			#print all entries plus a total 
			counter = 0
			for entry in self.fastaEntries:
				print("Header: " + entry[0])
				print("Sequence: " + entry[1])
				counter += 1
			print("Total Fasta Entries: " + str(counter))

	#class method for converting fastaEntries in cleanedGenes
	#this version of the method uses the normal procedure for typical pipeline output
	def normalClean(self):
		#temporary variables to hold the type, coding statuts, and sequence
		tempType = ""
		tempStatus = ""
		tempSeq = ""
		#go through each fasta entry
		for entry in self.fastaEntries:
			#split entry up into two temporary variables
			tempHeader = entry[0]
			tempSeq = entry[1]
			#trim tempHeader
			tempHeader = tempHeader.split("|")
			#determine if tempHeader is a coding gene or a psuedogene
			if len(tempHeader) == 2:
				tempType = tempHeader[1]
				tempStatus = "CODING"
			elif len(tempHeader) == 3:
				tempType = tempHeader[1]
				tempStatus = tempHeader[2]
			#add entry to cleanedGenes
			self.cleanedGenes.append(tuple([tempType, tempStatus, tempSeq]))
			#dump temporary variable memory
			tempType = ""
			tempStatus = ""
			tempSeq = ""
			tempHeader = ""
		#delete the raw fasta entries to save memory
		self.fastaEntries = None

	#class method fro printing all the cleaned genes
	def printCleanedGenes(self):
		#check if cleanedGenes list is empty
		if len(self.cleanedGenes) == 0:
			print("cleanedGenes is empty")
		else:
			#print all entries plus a total
			counter = 0
			for entry in self.cleanedGenes:
				print("Type: " + entry[0])
				print("Coding Status: " + entry[1])
				print("Sequence: " + entry[2])
				counter += 1
			print("Total Cleaned Genes: " + str(counter))

	#class method for filling the geneTypes list
	def findGeneTypes(self):
		#temporary variable to hold combined type and status
		tempType = ""
		#run through all genes
		for gene in self.cleanedGenes:
			#combine gene type and coding status
			tempType = gene[0] + "_" + gene[1]
			#check if new type needs to be added to geneTypes
			if tempType not in self.geneTypes:
				self.geneTypes.append(tempType)
			#dump tempType memory
			tempType = ""

	#class method for printing all the geneTypes list
	def printGeneTypes(self):
		#check if geneTypes is empty
		if len(self.geneTypes) == 0:
			print("geneTypes is empty")
		else:
			#print all entries plus a total
			counter = 0
			for geneType in self.geneTypes:
				print(geneType)
				counter += 1
			print("Total geneTypes: " + str(counter))

	#class method that returns all the cleaned genes
	def getGenes(self):
		return(self.cleanedGenes)

	#class method for refromating and returning genes to allow for gene tree friendly output
	def geneTreeFormat(self):
		#make a list to hold the newly formated output
		#the list will be made up of headers in a Name_Type_Status format and seqeunces
		newGeneList = list()
		#run through all genes in cleanedGenes
		for gene in self.cleanedGenes:
			tempHeader = ">" + self.species + "_" + gene[0] + "_" + gene[1]
			newGeneList.append(tuple([tempHeader, gene[2]]))
		#return newly formated list
		return(newGeneList)
		







if __name__ == '__main__':
	main()


