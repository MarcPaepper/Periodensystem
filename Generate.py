# create output folder if not exists
import math
import copy
import json
import matplotlib.pyplot as plt
import os
if not os.path.exists("Output"):
	os.makedirs("Output")
from Constants import *

englishNamesRev = {v: k for k, v in englishNames.items()}

with open("Output/Wikiviews.json", "r") as f:
	wViews = json.load(f)

def getNeighbor(i, j, direction, xtra):
	refTable = symbolsXtra if xtra else symbolsMn
	symbol = refTable[i][j]
	index = sanl.index(symbol)

	if direction == "up":
		if i > 0:
			upperNeighborSymbol = refTable[i - 1][j]
			if upperNeighborSymbol != "" and upperNeighborSymbol != "-":
				return upperNeighborSymbol
		return ""
	
	if direction == "down":
		maxI = len(refTable)
		if i < maxI - 1:
			lowerNeighborSymbol = refTable[i + 1][j]
			if lowerNeighborSymbol != "" and lowerNeighborSymbol != "-":
				return lowerNeighborSymbol
		return ""
	
	if direction == "left":
		if index > 0:
			return sanl[index - 1]
		return ""
	
	if direction == "right":
		if index < len(sanl) - 1:
			return sanl[index + 1]
		return ""

# calculate score for each element, which is given by the number of views on wikipedia
# + the average of neighboring elements (up and down + left and right (also if in the next period or at the lanthanides/actinides boundaries))
scores = copy.deepcopy(wViews)

for name in scores:
	symbol = englishNamesRev[name.lower()]
	
	# find index in symbolsMn or symbolsXtra
	xtra = True
	i = 0
	j = 0
	for i in range(len(symbolsMn)):
		if symbol in symbolsMn[i]:
			j = symbolsMn[i].index(symbol)
			xtra = False
			break
	if xtra:
		for i in range(len(symbolsXtra)):
			if symbol in symbolsXtra[i]:
				j = symbolsXtra[i].index(symbol)
				break
	
	numberOfNeighbors = 0
	neighborSum = 0
	
	directions = ["up", "down", "left", "right"]
	for dir in directions:
		neighborSymbol = getNeighbor(i, j, dir, xtra)
		if neighborSymbol != "":
			numberOfNeighbors += 1
			nameN = englishNames[neighborSymbol]
			nameN = nameN[0].upper() + nameN[1:]
			neighborSum += wViews[nameN]
	
	index = sanl.index(symbol)
	avg = neighborSum / numberOfNeighbors
	scores[name] = int((avg + wViews[name])/2) / ((index + 1) ** (1/2) + 5)

color_map = plt.get_cmap("magma")
colorsMagma = [color_map(i) for i in range(256)]
# scale the first three values of each tuple by 255
colorsMagma = [(int(r*255), int(g*255), int(b*255)) for r, g, b, a in colorsMagma]

# log the values
wViewsLog = {}
scoresLog = {}
for key in wViews:
	wViewsLog[key] = math.log(wViews[key])
	scoresLog[key] = math.log(scores[key])

# normalize wLengths to min(wLengths) - max(wLengths) to 0-255 in a new dictionary
wViews256 = {}
maxV = max(wViewsLog.values())
minV = min(wViewsLog.values())
diff = maxV - minV

for key in wViewsLog:
	wViews256[key] = int((wViewsLog[key] - minV) / diff * 255)
	
scores256 = {}
maxV = max(scoresLog.values())
minV = min(scoresLog.values())
diff = maxV - minV

for key in wViewsLog:
	scores256[key] = int((scoresLog[key] - minV) / diff * 255)

# create a list of symbols in descending order of their score
sortedNames = [k for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)]
length = len(sortedNames)
for i, name in enumerate(sortedNames):
	scores256[name] = int((length - i) / length * 255)
	scores[name] = i * 1000

types = ["gLoc", "gName", "visWiki", "scores"]
outputFiles = ["gLocTable", "gNameTable", "wikiViews", "scores"]

for type, outputFile in zip(types, outputFiles):
	isGuessLoc = type == "gLoc"
	isGuessName = type == "gName"
	isVis = type == "visWiki" or type == "scores"
	
	lookup = wViews256 if type == "visWiki" else scores256
	lookupD = wViews if type == "visWiki" else scores

	oct =  "onClick=" + ("'flipToBack()'" if isGuessName else "'wrongPick(event)'") # meaning on click text
	# hc  = "" if isGuessName else " hidden" # meaning hidden class
	# ha  = "" if isGuessName else " class='hidden' " # meaning hidden attribute

	output = f"""<table id="Periodensystem" class="{type}">
	<tr class="hauptgr">
		<td class="e"></td>
		<td>I</td>
		<td>II</td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td>III</td>
		<td>IV</td>
		<td>V</td>
		<td>VI</td>
		<td>VII</td>
		<td>VIII</td>
	</tr>
	
	<tr class="nebengr">
		<td class="e"></td>
		<td>1</td>
		<td>2</td>
		<td>3</td>
		<td>4</td>
		<td>5</td>
		<td>6</td>
		<td>7</td>
		<td>8</td>
		<td>9</td>
		<td>10</td>
		<td>11</td>
		<td>12</td>
		<td>13</td>
		<td>14</td>
		<td>15</td>
		<td>16</td>
		<td>17</td>
		<td>18</td>
	</tr>"""

	col = ""
	addTxt = ""
	
	def createCell(symbol, i, j, isXtra, classes, id, attr):
		# add color if in vis mode
		if isVis:
			col = f" style='background-color: rgb{colorsMagma[lookup[englishNamesU[symbol]]]}'"
			addTxt = f"<br><span class='views'>{lookupD[englishNamesU[symbol]] // 1000}k</span>"
		if type == "visWiki":
			addTxt = f"<br><span class='views'>{wViews[englishNamesU[symbol]] // 1000}k</span>"
		
		return f"\n\t\t<td class='{classes}' id='{id}' {attr}{col}>{symbol}{addTxt}</td>"
	
	# add main group
	for i, td in enumerate(symbolsMn):
		output += "\n\t<tr class='main'>\n\t\t<td class=\"p\">" + str(i+1) + "</td>"
		for j, symbol in enumerate(td):
			if symbol == "-":
				output += "\n\t\t<td style='display: none'></td>"
			elif symbol == "": # meaning empty cell
				output += "\n\t\t<td class=\"e\"></td>"
			elif symbol == "NT": # meaning name tag
				output += "\n\t\t<td id='nameTagTD'"
				output += " class='disabled'" if type == "gName" else ""
				output += " colspan='14'>{{name}}</td>"
			elif symbol == "bc": # meaning big cell
				output += "\n\t\t<td id='bigCell' class='e' colspan='2'></td>"
			else:
				# add color if in vis mode
				if isVis:
					col = f" style='background-color: rgb{colorsMagma[lookup[englishNamesU[symbol]]]}'"
					addTxt = f"<br><span class='views'>{lookupD[englishNamesU[symbol]] // 1000}k</span>"
				if type == "visWiki":
					addTxt = f"<br><span class='views'>{wViews[englishNamesU[symbol]] // 1000}k</span>"
				if ((i == 5 or i == 6) and j == 2): # add indicator for actinides and lactinides
					output += f"\n\t\t<td class='l hidden' {oct}{col}>{symbol}{addTxt}</td>"
				elif ((i == 5 or i == 6) and j == 3):
					output += f"\n\t\t<td class='r hidden' {oct}{col}>{symbol}{addTxt}</td>"
				else:
					output += f"\n\t\t<td class='hidden' {oct}{col}>{symbol}{addTxt}</td>"
		output += "\n\t</tr>"

	# empty row
	output += "\n\t<tr id='emptyRow'>\n\t\t<td class=\"e\"></td><td class=\"e\"></td>\n\t</tr>"


	# add lanthanides
	if isVis:
		col = f" style='background-color: rgb{colorsMagma[lookup[englishNamesU[symbolsXtra[0][0]]]]}'"
		addTxt = f"<br><span class='views'>{lookupD[englishNamesU[symbolsXtra[0][0]]] // 1000}k</span>"
	if type == "visWiki":
		addTxt = f"<br><span class='views'>{wViews[englishNamesU[symbolsXtra[0][0]]] // 1000}k</span>"
	output += f"""
	<tr>
		<td class="e"></td>
		<td class="p x" colspan=3>Lanthan.:</td>
		<td class='r hidden'{oct}{col}>{symbolsXtra[0][0]}{addTxt}</td>"""
		
	for i in range(1, len(symbolsXtra[0])):
		symbol = symbolsXtra[0][i]
		
		# add color if in vis mode
		if isVis:
			col = f" style='background-color: rgb{colorsMagma[lookup[englishNamesU[symbol]]]}'"
			addTxt = f"<br><span class='views'>{lookupD[englishNamesU[symbol]] // 1000}k</span>"
		if type == "visWiki":
			addTxt = f"<br><span class='views'>{wViews[englishNamesU[symbol]] // 1000}k</span>"
		output += f"\n\t\t<td class='hidden' {oct}{col}>{symbol}{addTxt}</td>"
	output += "\n\t</tr>"


	# add actinides
	if isVis:
		col = f" style='background-color: rgb{colorsMagma[lookup[englishNamesU[symbolsXtra[1][0]]]]}'"
		addTxt = f"<br><span class='views'>{lookupD[englishNamesU[symbolsXtra[1][0]]] // 1000}k</span>"
	if type == "visWiki":
		addTxt = f"<br><span class='views'>{wViews[englishNamesU[symbolsXtra[1][0]]] // 1000}k</span>"
	output += f"""
	<tr>
		<td class="e"></td>
		<td class="p x" colspan=3>Actin.:</td>
		<td class='r hidden'{oct}{col}>{symbolsXtra[1][0]}{addTxt}</td>"""
		
	for i in range(1, len(symbolsXtra[1])):
		symbol = symbolsXtra[1][i]
		
		# add color if in vis mode
		if isVis:
			col = f" style='background-color: rgb{colorsMagma[lookup[englishNamesU[symbol]]]}'"
			addTxt = f"<br><span class='views'>{lookupD[englishNamesU[symbol]] // 1000}k</span>"
		if type == "visWiki":
			addTxt = f"<br><span class='views'>{wViews[englishNamesU[symbol]] // 1000}k</span>"
		output += f"\n\t\t<td class='hidden' {oct}{col}>{symbol}{addTxt}</td>"
	output += "\n\t</tr>"


	output += "\n</table>"


	# clear file if exists
	if os.path.exists(f"Output/{outputFile}.html"):
		os.remove(f"Output/{outputFile}.html")

	# write to file TableFull.html
	with open(f"Output/{outputFile}.html", "w") as f:
		f.write(output)

directions = ["up", "down", "left", "right"]

# Generate cards
languages = ["en", "fr", "de", "it", "pt", "es"]
# import languages.json
with open("Output/languages.json", "r") as f:
	translations = json.load(f)

# Clean or create folder "Cards"
if os.path.exists("Output/Cards"):
	for file in os.listdir("Output/Cards"):
		os.remove(f"Output/Cards/{file}")
else:
	os.makedirs("Output/Cards")

for lang in languages:
	output = ""
	
	for name in sortedNames:
		symbol = englishNamesRev[name.lower()]
		
		xtra = symbol in symbolsXtra[0] or symbol in symbolsXtra[1]
		ref_table = symbolsXtra if xtra else symbolsMn
		
		i, j = 0, 0
		for i in range(len(ref_table)):
			if symbol in ref_table[i]:
				j = ref_table[i].index(symbol)
				break
		
		# engName = englishNames[symbol]
		name = translations[symbol][lang]
		neighbors = [getNeighbor(i, j, dir, xtra) for dir in directions]
		
		if not xtra:
			period = i + 1
		elif j == 0:
			period = "La"
		else:
			period = "Ac"
		
		group = j + 1
		
		output += f"""{period};{group};{name};{neighbors[0]};{neighbors[1]};{neighbors[2]};{neighbors[3]}\n"""
	
	# delete last \n
	output = output[:-1]
	
	# write to file
	with open(f"Output/Cards/{lang}.csv", "w") as f:
		f.write(output)

print("Done!")