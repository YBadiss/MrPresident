from subprocess import call

def getOptions(i, options, cmd):
	if i >= len(options):
		filename = "./results/" + "_".join(cmd) + ".txt"
		print "\t" + filename
		with open(filename, "w") as f:
			call(cmd, stdout=f)
	else:
		key = options.keys()[i]
		for val in options[key]:
			# cmd + "key = val"
			# cmd + "key"
			# cmd
			if val == True:
				appendCmd = [key]
			elif val == False:
				appendCmd = []
			else:
				appendCmd = [key + "=" + val]
			getOptions(i+1, options, cmd + appendCmd)

# options = {
# 	"-ctype" : ["rm","shem"],
# 	"-objtype" : ["cut","vol"],
# 	"-no2hop" : [True,False],
# 	"-contig" : [True,False],
# 	"-minconn" : [True,False]
# }

options = {
	"-ctype" : ["shem"],
	"-objtype" : ["cut"],
	"-no2hop" : [True],
	"-contig" : [False],
	"-minconn" : [False],
	"-ufactor": ["1.04","1.05","1.10"]
}

#graphFiles = ["graphA.gr","graphB.gr","graphC.gr"]
graphFiles = ["graphA.gr"]

for graph in graphFiles:
	print graph + " ... "
	getOptions(0, options, ["gpmetis", graph, "64"])