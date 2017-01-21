# MLB Hall of Fame Analysis - Players

class Player:
	pass

# Construct Player Class
val = 0
CFs = []
maxValues = [0] * 7
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
	plyr.avg  = layer[2]
	plyr.obp  = layer[3]
	plyr.slg  = layer[4]
	plyr.hr   = layer[5]
	plyr.rbi  = layer[6]
	plyr.runs = layer[7]
	plyr.sb   = layer[8] 

	CFs.append(plyr) # Add to array

for player in CFs:
	if player.avg > maxValues[0]:
		maxValues[0] = player.avg
		maxNames[0] = player.name
	if player.obp > maxValues[1]:
		maxValues[1] = player.obp
		maxNames[1] = player.name

print "Max Avg: " + maxValues[0] + " by " + maxNames[0]
print "Max OBP: " + maxValues[1] + " by " + maxNames[1]

f.close()

