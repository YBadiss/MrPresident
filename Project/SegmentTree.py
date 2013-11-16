from collections import defaultdict

class SegmentTree:
	min_value = 0
	infinite = None

	@staticmethod
	def __includes(int1, int2):
		start1,end1 = int1
		start2,end2 = int2
		return (start1 <= start2) and ((end1 >= end2) or (end1 == SegmentTree.infinite))

	def __init__(self):
		self.__max_value = 1
		self.__nodes = defaultdict(set) # key = (start,end), val = list(element_ids)
		self.__inifinite_elements = {} # key = element_id, val = start

	def insert(self, element_id, interval):
		assert len(interval) == 2
		start,end = interval
		if end != SegmentTree.infinite:
			assert start < end
		assert start >= SegmentTree.min_value

		print "Inserting", element_id, "-", interval

		if end == SegmentTree.infinite:
			self.__inifinite_elements[element_id] = end
			self.__extend(start)
		else:
			self.__extend(end)
		self.__insert(element_id, start, end, SegmentTree.min_value, self.__max_value)

	def __insert(self, element_id, start, end, in_start, in_end):
		key = (in_start, in_end)
		if SegmentTree.__includes((start,end), key):
			print "\tInserting in",key
			self.__nodes[key].add(element_id)
		else:
			mid = int((in_start + in_end)/2)
			if start <= mid:
				self.__insert(element_id, start, end, in_start, mid)
			if (end > mid) or (end == SegmentTree.infinite):
				self.__insert(element_id, start, end, mid + 1, in_end)

	def delete(self, element_id, interval):
		assert len(interval) == 2
		start,end = interval
		if end != SegmentTree.infinite:
			assert start < end
		assert start >= SegmentTree.min_value

		print "Deleting", element_id, "-", interval

		self.__delete(element_id, start, end, SegmentTree.min_value, self.__max_value)
		if element_id in self.__inifinite_elements:
			del self.__inifinite_elements[element_id]

	def __delete(self, element_id, start, end, in_start, in_end):
		key = (in_start, in_end)
		if SegmentTree.__includes((start,end), key):
			self.__nodes[key].remove(element_id)
		else:
			mid = int((in_start + in_end)/2)
			if start <= mid:
				self.__delete(element_id, start, end, in_start, mid)
			if (end > mid) or (end == SegmentTree.infinite):
				self.__delete(element_id, start, end, mid + 1, in_end)

	def query(self, point):
		assert point >= SegmentTree.min_value

		print "Querying", point

		if point <= self.__max_value:
			return set(self.__query(point, SegmentTree.min_value, self.__max_value))
		else:
			return set(self.__inifinite_elements.keys())

	def __query(self, point, in_start, in_end):
		matches = list(self.__nodes[(in_start, in_end)])
		if in_start == in_end:
			return matches
		mid = int((in_start + in_end)/2)
		if point <= mid:
			return matches + self.__query(point, in_start, mid)
		else:
			return matches + self.__query(point, mid + 1, in_end) 

	def __extend(self, new_max_value):
		while new_max_value > self.__max_value:
			print "Extending from", self.__max_value, "to", self.__max_value*2
			self.__nodes[(self.__max_value+1, 2*self.__max_value)] = set(self.__inifinite_elements.keys())
			self.__max_value *= 2