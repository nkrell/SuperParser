import os
import subprocess
import time

def main():
	#list to hold all data that will be read it
	genomeFileList = list()
# 	   _____                                 _____                                     
 #  / ____|                               |  __ \                                    
 # | (___    _   _   _ __     ___   _ __  | |__) |   __ _   _ __   ___    ___   _ __ 
 #  \___ \  | | | | | '_ \   / _ \ | '__| |  ___/   / _` | | '__| / __|  / _ \ | '__|
 #  ____) | | |_| | | |_) | |  __/ | |    | |      | (_| | | |    \__ \ |  __/ | |   
 # |_____/   \__,_| | .__/   \___| |_|    |_|       \__,_| |_|    |___/  \___| |_|   
 #                  | |                                                              
 #                  |_|                                                              
	print('\033[1;92m')
	print("   _____                                 _____                                     ")
	print("  / ____|                               |  __ \                                    ")
	print(" | (___    _   _   _ __     ___   _ __  | |__) |   __ _   _ __   ___    ___   _ __ ")
	print("  \___ \  | | | | | '_ \   / _ \ | '__| |  ___/   / _` | | '__| / __|  / _ \ | '__|")
	print("  ____) | | |_| | | |_) | |  __/ | |    | |      | (_| | | |    \__ \ |  __/ | |   ")
	print(" |_____/   \__,_| | .__/   \___| |_|    |_|       \__,_| |_|    |___/  \___| |_|   ")
	print("                  | |                                                              ")
	print("                  |_|                                                              ")
	print("                                                              By Nicholas Krell")
	print("                                                              Version 1.0")
	print('\033[0;39m')
	print('\n')

	while True:
		print('\n')
		print("1) Read in OR pipeline output files")
		print("2) Clean read-in data")
		print("3) Get gene types from cleaned data")
		print("4) Get gene counts")
		print("5) Output raw FASTA entries")
		print("6) Output cleaned Genes")
		print("7) Output gene types")
		print("8) Output gene counts")
		print("C) Output .csv chart of gene counts")
		print("T) Output files that can be used to make a gene tree")
		print("R) Rename genome files using name chart")
		print("Q) Quit program")

		print("Make a selection: ")
		userInput = input()
		print('\n')
		if userInput == "Q" or userInput == "q":
			exit()

		#Read in OR pipeline output files
		elif userInput == "1": 
			targetFolder = folderQuery("parsing")
			#navigate into target folder
			os.chdir(targetFolder) #IN 1 <-------
			for file in os.listdir():
				if file.endswith(".fna") or file.endswith(".fasta"):
					#temporary variable to hold data before it is added to main list
					tempGeneFile = GeneFile(file)
					print("Reading file " + file)
					tempGeneFile.readFile()
					genomeFileList.append(tempGeneFile)
					print("File read")
					#dump temporary variable memory
					tempGeneFile = ""
			print("Done")
			#navigate back to starting folder
			os.chdir(os.path.dirname(os.getcwd())) #OUT 1 <------

		#Clean read-in data
		elif userInput == "2": 
			if len(genomeFileList) == 0:
				print("No data has been read in")
			else:
				for entry in genomeFileList:
					print("Cleaning " + entry.getFileName())
					entry.normalClean()
					print(entry.getFileName() + " cleaned")

		#Get gene types from cleaned data
		elif userInput == "3": 
			if len(genomeFileList) == 0:
				print("No data has been read in")
			else:
				for entry in genomeFileList:
					print("Getting gene types from " + entry.getFileName())
					entry.findGeneTypes()
					print(entry.getFileName() + " done")

		#Get gene counts
		elif userInput == "4":
			if len(genomeFileList) == 0:
				print("No data has been read in")
			if genomeFileList[0].fastaEntries != None:
				print("Genes must be cleaned first")
				print("Use '2) Clean read-in data' first")
			test = genomeFileList[0].getGeneTypes()
			if len(test) == 0:
				print("Gene type list has not been generated")
				print("Use '3) Get gene types from cleaned data' first")
			else:
				for entry in genomeFileList:
					print("Getting gene counts from " + entry.getFileName())
					entry.findGeneCounts()
					print(entry.getFileName() + " done")


		#Output raw FASTA entries
		elif userInput == "5": 
			if len(genomeFileList) == 0:
				print("No data has been read in")
			if genomeFileList[0].fastaEntries == None:
				print("Raw fasta entries have been cleaned")
				print("Use '6) Output cleaned Genes' instead")
			else:
				for entry in genomeFileList:
					entry.printFastaEntries()

		#Output cleaned genes		
		elif userInput == "6": 
			if len(genomeFileList) == 0:
				print("No data has been read in")
			else:
				for entry in genomeFileList:
					entry.printCleanedGenes()

		#Output gene types
		elif userInput == "7":
			if len(genomeFileList) == 0:
				print("No data has been read in")
			test = genomeFileList[0].getGeneTypes()
			if len(test) == 0:
				print("Gene type list has not been generated")
				print("Use '3) Get gene types from cleaned data' first")
			else:
				for entry in genomeFileList:
					entry.printGeneTypes()

		#Output gene counts
		elif userInput == "8":
			test = genomeFileList[0].getGeneCounts()
			if len(genomeFileList) == 0:
				print("No data has been read in")
			if len(test) == 0:
				print("Gene counts have not been generated yet")
				print("Use '4) Get gene counts' first")
			else:
				for entry in genomeFileList:
					entry.printGeneCounts()

		#Output .csv chart of gene counts
		elif userInput == "C":
			test = genomeFileList[0].getGeneCounts()
			if len(genomeFileList) == 0:
				print("No data has been read in")
			if len(text) == 0:
				print("Gene counts have not been generated yet")
				print("Use '4) Get gene counts' first")
			else:
				pass 
				#do the thing---------------------------------------------------------------------------------


		#Output files that can be used to make a gene tree	
		elif userInput == "T":
			targetFolder = ""
			if len(genomeFileList) == 0:
				print("No data has been read in")
			if genomeFileList[0].fastaEntries != None:
				print("Raw entries must be cleaned before gene tree files can be generated")
				print("Use '2) Clean read-in data' first")
			test = genomeFileList[0].getGeneTypes()
			if len(test) == 0:
				print("Gene type list has not been generated")
				print("Use '3) Get gene types from cleaned data' first")
			else:
				while True:
					print("Enter name for folder to hold gene tree files: ")
					targetFolder = input()
					if targetFolder in os.listdir():
						print("A folder in your drectory already has that name")
					else:
						break

				geneTree(genomeFileList, targetFolder)
			
		#Rename genome files using name chart
		elif userInput == "R":
			yesNo = ""
			while True:
				print("Is there a name chart in the directory with the format 'Name [Tab] Accession' ? (y/n)")
				yesNo = input().upper()
				if yesNo == "Y" or yesNo == "N":
					break
				else:
					print("Invalid input")
			while True:
				print("Do the genome file names start with their accession number? (y/n)")
				yesNo = input().upper()
				if yesNo == "Y" or yesNo == "N":
					break
				else:
					print("Invalid input.")
			targetFolder = folderQuery("renaming")
			while True:
				print("Enter name of name chart: ")
				yesNo = input()
				if yesNo in os.listdir():
					break
				else:
					print("File not found")
			fileRename(yesNo, targetFolder)

		



		#For bad input
		else:
			print('\n')
			print("Invalid input")

def printCSV():
	#code goes here


def folderQuery(action):
	#variable to hold folder name
	targetFolder = ""
	while True:
		try:
			print("Enter name of folder containing genomes for " + action + ": ")
			targetFolder = input()
			if targetFolder not in os.listdir():
				raise ValueError
			else:
				pass
		except ValueError:
			print("Folder not found")
		except FileNotFoundError:
			print("Folder not found")
		else:
			break
	#determine if the user would like the files renamed
	gcaFlag = False
	for fileName in os.listdir(targetFolder):
		if fileName.startswith("GCA"):
			gcaFlag = True
	if gcaFlag == True:
		print("It is reccomened that you rename the files first")
		print("Resart the program and select 'R) Rename genome files using name chart' ")
	return(targetFolder)

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
def geneTree(genomeFileList, targetFolder):
	#list to hold all the possible types
	allTypesList = list()
	#make new folder and navigate into it
	os.mkdir(targetFolder)
	os.chdir(targetFolder) #IN 1 <------
	#find all possible types first
	for entry in genomeFileList:
		for geneType in entry.getGeneTypes():
			if geneType not in allTypesList:
				allTypesList.append(geneType)

	#create and populate a file for each gene type in allTypesList
	for geneType in allTypesList:
		#open new file named after the type of gene that will go into it
		newFile = open(geneType + ".genetree.fasta", "w")
		#write every gene of that type from every genome in genomeFileList
		for entry in genomeFileList:
			#check if file have been renamed
			if entry.getFileName().startswith("GCA"):
				gcaFlag = False
			else:
				gcaFlag = True
			#parse accession number out of name of file
			#temporary variable to hold accession number
			accessNum = entry.getFileName()
			accessNum = accessNum.split(".")
			accessNum = accessNum[0] + "." + accessNum[1]
			accessNum = accessNum.split("_GCA_")
			accessNum = "GCA_" + accessNum[1]
			#parse species name out of name of file
			#temporary variable to hold species name
			specName = entry.getFileName()
			specName = specName.split("_")
			specName = specName[0] + "_" + specName[1]
			#go through every gene associated with that genomeFile
			for gene in entry.getGenes():
				#temporary variable to hold the type and status in the same format as in the geneType list
				tempGeneType = gene[0] + "_" + gene[1]
				#determine if the gene is of the type whose file is being written
				if tempGeneType == geneType:
					#write header
					newFile.write(">" + specName + "_" + accessNum + "_" + tempGeneType)
					newFile.write("\n")
					#write sequence
					newFile.write(gene[2])
					newFile.write("\n")

		#close file
		newFile.close()
	for geneType in allTypesList:
		print(geneType)

	#return to starting folder
	os.chdir(os.path.dirname(os.getcwd())) #OUT 1 <------


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

	def printGeneCounts(self):
		#check if geneCounts is empty
		if len(self.geneCounts) == 0:
			print("geneCounts in empty")
		else:
			#print all enties
			for geneCount in self.geneCounts:
				print(geneCount[0] + ": " + str(geneCount[1]))

	#class method that returns all the cleaned genes
	def getGenes(self):
		return(self.cleanedGenes)

	#class method for retruning the name of the file
	def getFileName(self):
		return(self.fileName)

	#class method for retruning the fasta entries
	def getFastaEntries(self):
		return(self.fastaEntries)

	#class method for retruning gene types list
	def getGeneTypes(self):
		return(self.geneTypes)

	#class method for returning gene counts list
	def getGeneCounts(self):
		return(self.geneCounts)

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

	#class method for filling the geneCounts list
	def findGeneCounts(self):
		#get a count for each geneType
		for geneType in self.geneTypes:
			#temparary variable to count the genes
			counter = 0
			#go through each gene and tally up ho many belong to each type
			for gene in self.cleanedGenes:
				if (gene[0] + "_" + gene[1]) == geneType:
					counter += 1
			#add each count and genetype to the counts list
			self.geneCounts.append(tuple([geneType, counter]))








if __name__ == '__main__':
	main()


