import pylab as pl
import glob

for filename in glob.glob("./*.csv"):
	pow = []
	tot_time = []
	rel_time = []
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
	        pow, tot_time, 'g')
	pl.xlabel('Node count')
	pl.ylabel('Time (s)')
	pl.xscale('log')
	pl.yscale('log')
	# pl.legend(('Total time', 'Time per node'),loc = 'lower right')
	pl.title(filename)
	pl.show()

