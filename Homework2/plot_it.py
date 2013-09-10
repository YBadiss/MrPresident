import pylab as pl
import glob

files = [
	("results.csv", "List"),
	("results_array_stride_0.csv", "Normal array"),
	("results_array_stride_2.csv", "2-strided array"),
	("results_array_stride_4.csv", "4-strided array"),
	("results_array_stride_8.csv", "8-strided array")
]

for filename, title in files:
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
	        pow, rel_time)
	pl.xlabel('Node count')
	pl.ylabel('Time (s)')
	pl.xscale('log',basex=2)
	pl.title(title)

	# pl.savefig(filename + '.png')
pl.clf()

