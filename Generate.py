# create output folder if not exists
import os
if not os.path.exists("Output"):
	os.makedirs("Output")

symbolsMn   = [[ "H", "NT",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-",   "", "He"],
		       ["Li", "Be",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "",  "B",  "C",  "N",  "O",  "F", "Ne"],
		       ["Na", "Mg",   "",   "",   "",   "",   "",   "",   "",   "",   "",   "", "Al", "Si",  "P",  "S", "Cl", "Ar"],
		       ["K",  "Ca", "Sc", "Ti",  "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
		       ["Rb", "Sr",  "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te",  "I", "Xe"],
		       ["Cs", "Ba", "La", "Hf", "Ta",  "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
			   ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]]

symbolsXtra = [["Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
			   ["Th", "Pa",  "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]]

englishNames = {
	"H": "Hydrogen",
	"He": "Helium",
	"Li": "Lithium",
	"Be": "Beryllium",
	"B" : "Boron",
	"C" : "Carbon",
	"N" : "Nitrogen",
	"O" : "Oxygen",
	"F" : "Fluorine",
	"Ne": "Neon",
	"Na": "Sodium",
	"Mg": "Magnesium",
	"Al": "Aluminium",
	"Si": "Silicon",
	"P" : "Phosphorus",
	"S" : "Sulfur",
	"Cl": "Chlorine",
	"Ar": "Argon",
	"K" : "Potassium",
	"Ca": "Calcium",
	"Sc": "Scandium",
	"Ti": "Titanium",
	"V" : "Vanadium",
	"Cr": "Chromium",
	"Mn": "Manganese",
	"Fe": "Iron",
	"Co": "Cobalt",
	"Ni": "Nickel",
	"Cu": "Copper",
	"Zn": "Zinc",
	"Ga": "Gallium",
	"Ge": "Germanium",
	"As": "Arsenic",
	"Se": "Selenium",
	"Br": "Bromine",
	"Kr": "Krypton",
	"Rb": "Rubidium",
	"Sr": "Strontium",
	"Y" : "Yttrium",
	"Zr": "Zirconium",
	"Nb": "Niobium",
	"Mo": "Molybdenum",
	"Tc": "Technetium",
	"Ru": "Ruthenium",
	"Rh": "Rhodium",
	"Pd": "Palladium",
	"Ag": "Silver",
	"Cd": "Cadmium",
	"In": "Indium",
	"Sn": "Tin",
	"Sb": "Antimony",
	"Te": "Tellurium",
	"I" : "Iodine",
	"Xe": "Xenon",
	"Cs": "Caesium",
	"Ba": "Barium",
	"La": "Lanthanum",
	"Ce": "Cerium",
	"Pr": "Praseodymium",
	"Nd": "Neodymium",
	"Pm": "Promethium",
	"Sm": "Samarium",
	"Eu": "Europium",
	"Gd": "Gadolinium",
	"Tb": "Terbium",
	"Dy": "Dysprosium",
	"Ho": "Holmium",
	"Er": "Erbium",
	"Tm": "Thulium",
	"Yb": "Ytterbium",
	"Lu": "Lutetium",
	"Hf": "Hafnium",
	"Ta": "Tantalum",
	"W" : "Tungsten",
	"Re": "Rhenium",
	"Os": "Osmium",
	"Ir": "Iridium",
	"Pt": "Platinum",
	"Au": "Gold",
	"Hg": "Mercury",
	"Tl": "Thallium",
	"Pb": "Lead",
	"Bi": "Bismuth",
	"Po": "Polonium",
	"At": "Astatine",
	"Rn": "Radon",
	"Fr": "Francium",
	"Ra": "Radium",
	"Ac": "Actinium",
	"Th": "Thorium",
	"Pa": "Protactinium",
	"U" : "Uranium",
	"Np": "Neptunium",
	"Pu": "Plutonium",
	"Am": "Americium",
	"Cm": "Curium",
	"Bk": "Berkelium",
	"Cf": "Californium",
	"Es": "Einsteinium",
	"Fm": "Fermium",
	"Md": "Mendelevium",
	"No": "Nobelium",
	"Lr": "Lawrencium",
	"Rf": "Rutherfordium",
	"Db": "Dubnium",
	"Sg": "Seaborgium",
	"Bh": "Bohrium",
	"Hs": "Hassium",
	"Mt": "Meitnerium",
	"Ds": "Darmstadtium",
	"Rg": "Roentgenium",
	"Cn": "Copernicium",
	"Nh": "Nihonium",
	"Fl": "Flerovium",
	"Mc": "Moscovium",
	"Lv": "Livermorium",
	"Ts": "Tennessine",
	"Og": "Oganesson"
}

types = ["gLoc", "gName"]
outputFiles = ["gLocTable", "gNameTable"]

for type, outputFile in zip(types, outputFiles):
	isGuessLoc = type == "gLoc"
	isGuessName = type == "gName"

	oct =  "onClick=" + "'flipToBack()'" if isGuessName else "'wrongPick(event)'" # meaning on click text
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

	# add main group
	for i, td in enumerate(symbolsMn):
		output += "\n\t<tr class='main'>\n\t\t<td class=\"p\">" + str(i+1) + "</td>"
		for j, symbol in enumerate(td):
			if symbol == "-":
				continue
			elif symbol == "":
				output += "\n\t\t<td class=\"e\"></td>"
			elif symbol == "NT":
				output += "\n\t\t<td id='nameTagTD'"
				output += " class='disabled'" if type == "gName" else ""
				output += " colspan='15'>{{Name}}</td>"
			else:
				if ((i == 5 or i == 6) and j == 2): # add indicator for actinides and lactinides
					output += f"\n\t\t<td class='l hidden' {oct}>" + symbol + "</td>"
				elif ((i == 5 or i == 6) and j == 3):
					output += f"\n\t\t<td class='r hidden' {oct}>" + symbol + "</td>"
				else:
					output += f"\n\t\t<td class='hidden' {oct}>" + symbol + "</td>"
		output += "\n\t</tr>"

	# empty row
	output += "\n\t<tr>\n\t\t<td class=\"e\"></td>\n\t</tr>"

	# add lanthanides
	output += f"""
	<tr>
		<td class="e"></td>
		<td class="p x" colspan=3>Lanthan.:</td>
		<td class='r hidden'{oct}>{symbolsXtra[0][0]}</td>"""
	for i in range(1, len(symbolsXtra[0])):
		output += f"\n\t\t<td class='hidden' {oct}>{symbolsXtra[0][i]}</td>"
	output += "\n\t</tr>"

	# add actinides
	output += f"""
	<tr>
		<td class="e"></td>
		<td class="p x" colspan=3>Actin.:</td>
		<td class='r hidden'{oct}>{symbolsXtra[1][0]}</td>"""
	for i in range(1, len(symbolsXtra[1])):
		output += f"\n\t\t<td class='hidden' {oct}>{symbolsXtra[1][i]}</td>"
	output += "\n\t</tr>"

	output += "\n</table>"

	# clear file if exists
	if os.path.exists(f"Output/{outputFile}.html"):
		os.remove(f"Output/{outputFile}.html")

	# write to file TableFull.html
	with open(f"Output/{outputFile}.html", "w") as f:
		f.write(output)

print("Done!")