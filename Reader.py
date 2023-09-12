# read in a csv with the following format:
# (name in english)	(name in french)	(name in german)	(name in italian)	(name in portuguese)	(name in spanish)

import csv
import sys
import json
from Constants import englishNames

englishNamesRev = {v: k for k, v in englishNames.items()}
languages = ["en", "fr", "de", "it", "pt", "es"]

# read in the csv
with open("Lango.csv", 'r') as f:
	reader = csv.reader(f, delimiter='\t')
	langos = list(reader)

langosDict = {}

for element_list in langos[1:]:
	element_dict = {}
	for i in range(len(languages)):
		element_dict[languages[i]] = element_list[i]
	symbol = englishNamesRev[element_list[0]]
	langosDict[symbol] = element_dict

# save
with open("Output/languages.json", "w") as f:
	json.dump(langosDict, f, indent=4)