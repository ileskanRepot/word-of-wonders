import xml.etree.ElementTree as ET

def checkIfWordOk(curWord, curKnown, curAlph):
	alphs = curAlph
	if len(curKnown) != len(curWord):
		return
	
	for alphKnown, alphCur in zip(curKnown,curWord):
		if not alphCur in alphs:
			return

		if alphKnown == ".":
			alphs.replace(alphKnown, "", 1)
			continue

		if alphKnown != alphCur:
			return

		if alphKnown != alphCur:
			return
		alphs.replace(alphKnown, "", 1)

	print(curWord)

tree = ET.parse('kotus-sanalista_v1/kotus-sanalista_v1.xml')
root = tree.getroot()

curAlph =  input("Put current letters:               ").lower()
curKnown = input("Put current word('.' for unknown): ").lower()


for child in root:
	curWord = child[0].text.lower()
	checkIfWordOk(curWord, curKnown, curAlph)
