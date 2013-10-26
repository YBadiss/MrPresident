import pylab as pl
import glob

i = 0

for filename in glob.glob("./*.csv"):
	pow = []
	tot_time = []
	rel_time = []
	i += 1
	with open(filename, 'r') as f:
		items = f.readline().split(";")
		# print items[0], items[1], items[2]
		for line in f:
			items = line.split(";")
			pow.append(2 ** int(items[0]))
			tot_time.append(float(items[1]))
			rel_time.append(float(items[2]))

	pl.plot(
	        # tot_time, pow, 'r', 
	        pow, rel_time)
	pl.xlabel('Node count')
	pl.ylabel('Time (s)')
	pl.xscale('log',basex=2)
	# pl.yscale('log')
	# pl.legend(('Total time', 'Time per node'),loc = 'lower right')
	pl.title(filename)
	# pl.show()
	pl.savefig(filename + '.png')
	pl.clf()
