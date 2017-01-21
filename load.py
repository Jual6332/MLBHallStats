# MLB Hall of Fame Analysis - Players

class Player:
	pass

# Construct Player Class
val = 0
CFs = []
maxValues = [0.0] * 7
maxNames = [0] * 7

# Load Data for all CFs
f = open("cfs.txt")
lines = f.readlines()

for ln in lines[1:len(lines)]:
	plyr = Player() # Initialize
	layer = ln.strip().split()
	#print(type(player[1])) - Check type, is a string

	# Assign Player Attributes
	plyr.name = layer[0] + " " + layer[1]
	plyr.avg  = float(layer[2])
	plyr.obp  = float(layer[3])
	plyr.slg  = float(layer[4])
	plyr.hr   = int(layer[5])
	plyr.rbi  = int(layer[6])
	plyr.runs = int(layer[7])
	plyr.sb   = int(layer[8]) 

	CFs.append(plyr) # Add to array

f.close()

for player in CFs:
	if player.avg > maxValues[0]:
		maxValues[0] = player.avg
		maxNames[0] = player.name
	if player.obp > maxValues[1]:
		maxValues[1] = player.obp
		maxNames[1] = player.name
	if player.slg > maxValues[2]:
		maxValues[2] = player.slg
		maxNames[2] = player.name
	if player.hr > maxValues[3]:
		maxValues[3] = player.hr
		maxNames[3] = player.name
	if player.rbi > maxValues[4]:
		maxValues[4] = player.rbi
		maxNames[4] = player.name
	if player.runs > maxValues[5]:
		maxValues[5] = player.runs
		maxNames[5] = player.name
	if player.sb > maxValues[6]:
		maxValues[6] = player.sb
		maxNames[6] = player.name

# Print Results to the User
print "Leading HOF Center Fielders in each Offensive Category"
print "Max AVG:  ", maxValues[0], " by ", maxNames[0]
print "Max OBP:  ", maxValues[1], " by ", maxNames[1]
print "Max SLG:  ", maxValues[2], " by ", maxNames[2]
print "Max HR:     ", maxValues[3], " by ", maxNames[3]
print "Max RBI:   ", maxValues[4], " by ", maxNames[4]
print "Max RUNS:  ", maxValues[5], " by ", maxNames[5]
print "Max SB:     ", maxValues[6], " by ", maxNames[6]


