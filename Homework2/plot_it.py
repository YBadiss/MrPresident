import pylab as pl
import glob

files = [
	("results_list.csv", "List"),
	("results_array_stride_1.csv", "Normal array"),
	("results_array_stride_16.csv", "16-strided array"),
	("results_array_stride_32.csv", "32-strided array"),
	("results_array_stride_64.csv", "64-strided array"),
	("results_array_rand.csv", "Random array")
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

pl.title("Evolution of the average access time")

pl.legend([title for filename,title in files], loc="upper left")
pl.savefig('plot.png')
pl.clf()

