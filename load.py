# MLB Hall of Fame Analysis - Players

class Player:
	pass

# Construct Player Class
CFs = []

# Load Data for all CFs
f = open("cfs.txt")
lines = f.readlines()

for ln in lines[1:len(lines)]:
	plyr = Player()
	layer = ln.strip().split()
	#print(type(player[1])) - Check type, is a string

	# Assign Player Attributes
	plyr.name = layer[0] + " " + layer[1]
	plyr.avg  = layer[2]
	plyr.obp  = layer[3]
	plyr.slg  = layer[4]
	plyr.hr   = layer[5]
	plyr.rbi  = layer[6]
	plyr.runs = layer[7]
	plyr.sb   = layer[8] 

	CFs.append(plyr)

for num in CFs:
	print num.name

f.close()

