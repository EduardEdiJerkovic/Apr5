import numbers
import copy
import math

class Matrix:
	def __init__(self, value=[]):
		self.value = []
		for r in value:
			self.value.append([float(x) for x in r])

	def rows_count(self):
		'''
		Returns number of rows in matrix.
		'''
		return len(self.value)

	def columns_count(self):
		'''
		Returns number of colums in matrix.
		'''
		if (self.value.count != 0): 
			return len(self.value[0]) 
		else:
			return 0
	
	def create_from_file(self, file):
		'''
		Import matrix from file.
		'''
		self.value = []
		f = open(file, "r")
		if f.mode == 'r': 
			fl = f.readlines()

		for l in fl:
			self.value.append([int(x) for x in l.split()])

		f.close
	
	def write_to_file(self, file):
		'''
		Export matrix to file.
		'''
		f = open(file, "w+")
		for row in self.value:
			line = " ".join(str(el) for el in row) + "\n"
			f.write(line)

		f.close()

	def transpose(self):
		'''
		Returns transpose matrix.
		'''
		result = []
		for i in range(0, self.columns_count()):
			result.append([x[i] for x in self.value])
		return Matrix(result)

	def front_substitucion(self, b):
		'''
		TODO: Finish this.
		'''
		if (b.rows_count() != 1):
			raise ValueError("B paramter must be vector.")
		if (self.columns_count() != self.rows_count()):
			raise ValueError("Matrix must be sqared for front substitucion.")

		for i in range(self.rows_count() - 1):
			for j in range(i+1, self.rows_count()):
				b[0, j] -= self[j, i] * b[0, i]

	def backward_substitucion(self, b=[]):
		'''
		TODO: Finish this.
		'''
		if (b.rows_count() != 1):
			raise ValueError("B paramter must be vector.")
		if (b.columns_count() != self.rows_count()):
			raise ValueError("B vactor don't have same dimension as matrix.")

		for i in range(self.rows_count() - 1, -1, -1):
			if (self[i, i] == 0 or abs(self[i, i]) <= 0.000001):
				raise ValueError("You can't devide with 0.")
			b[0, i] /= self[i, i]
			for j in range(i):
				b[0, j] -= self[j, i] * b[0, i]
	
	def lu_decomposition(self):
		'''
		LU algorithm implementation.
		Returns L and U of matix. Result is combined in one matrix.
		'''
		if (self.rows_count() != self.columns_count()):
			raise ValueError("Matrix needs to me square for LU decomposition.")
		for i in range(self.rows_count() - 1):
			for j in range(i+1, self.rows_count()):
				if (self[i, i] == 0): #or abs(self[i, i]) <= 0.000001):
					raise ValueError("Can't divide by 0")
				self[j, i] = self[j, i] / self[i, i]
				for k in range(i+1, self.rows_count()):
					self[j, k] -= self[j, i] * self[i, k]

	def lup_decomposition(self):
		'''
		LUP algorithm implementation.
		Returns L and U of matix. Result is combined in one matrix.
		'''
		p = [i for i in range(self.rows_count())]
		for i in range(self.rows_count()-1):
			pivot = i
			for j in range(i+1, self.rows_count()):
				if (abs(self[p[j], i]) > abs(self[p[pivot], i])):
					pivot = j
			p[pivot], p[i] = p[i], p[pivot]
			for j in range(i+1, self.rows_count()):
				if (abs(self[p[i], i]) < math.pow(10, -6)):
					raise ValueError("Can't divide by 0")
				self[p[j], i] /= self[p[i], i]
				for k in range(i+1, self.rows_count()):
					self[p[j], k] -= self[p[j], i] * self[p[i], k]
		lst = []
		for i in p:
			lst.append(self.value[i])
		return p, Matrix(lst)

	@staticmethod
	def solve(a, b, pivot=False):
		aa = a.__copy__()
		bb = b.__copy__()
		if (pivot):
			p, a = aa.lup_decomposition()
			bb = Matrix([[bb[pi] for pi in p]])
			a.front_substitucion(bb)
			a.backward_substitucion(bb)
		else:
			aa.lu_decomposition()
			aa.front_substitucion(bb)
			aa.backward_substitucion(bb)

		return bb

	@staticmethod
	def inverz(a):
		aa = a.__copy__()

		p, aa = aa.lup_decomposition()
		"""tmp = []
		for i in range(a.columns_count()):
			x = [0] * a.columns_count()
			x[i] = 1
			tmp.append(x)
		#print(p, tmp)
		tmp = [tmp[pi] for pi in p]
		tmp[]"""
		tmp = Matrix.getI(a.columns_count()).toList()
		tmp = [tmp[pi] for pi in p]

		b = []
		for j in range(len(tmp[0])):
			l = []
			for i in range(len(tmp)):
				l.append(tmp[i][j])
			b.append(l)
			
		result = []
		for i in range(a.columns_count()):
			aaa = aa.__copy__()
			bb = Matrix([b[i]])
			aaa.front_substitucion(bb)
			aaa.backward_substitucion(bb)
			result.append(bb.toList()[0])

		result2 = copy.deepcopy(result)
		for i in range(len(result)):
			for j in range(len(result[0])):
				result2[j][i] = result[i][j]

		return Matrix(result2)

	
	@staticmethod
	def getI(n):
		tmp = []
		for i in range(n):
			x = [0] * n
			x[i] = 1
			tmp.append(x)
		return Matrix(tmp)
	

	def toList(self):
		return copy.deepcopy(self.value)

	def __str__(self):
		return(str(self.value))

	def __getitem__(self, pos):
		if (isinstance(pos, numbers.Number)):
			pos = (0, pos)
		if (isinstance(pos, tuple)):
			x, y = pos
			if (isinstance(x, numbers.Number) and isinstance(x, numbers.Number)):
				if (x not in range(self.rows_count()) or y not in range(self.columns_count())):
					raise ValueError("Index out of bound.")
				return self.value[x][y]
			else:
				raise ValueError("Wrong type of index values.")
		else:
			raise ValueError("Wrong type of index values.")

	def __setitem__(self, pos, value):
		if (isinstance(pos, numbers.Number)):
			x, y = 0, pos
		elif (isinstance(pos, tuple)):
			x, y = pos
			if (isinstance(x, numbers.Number) and isinstance(x, numbers.Number)):
				if (x not in range(self.rows_count()) or y not in range(self.columns_count())):
					raise ValueError("Index out of bound.")
				if (isinstance(value, numbers.Number)):
					self.value[x][y] = float(value)
				else:
					raise ValueError("Value type must bu number.")
			else:
				raise ValueError("Wrong type of index values.")
		else:
			raise ValueError("Wrong type of index values.")

	def __neg__(self):
		return (-1) * self

	def __add__(self, other):
		if not isinstance(other, Matrix):
			raise ValueError("Matrix value is required.")
		elif len(self.value) != len(other.value) or len(self.value[0]) != len(other.value[0]):
			raise ValueError("Matrix have different dimensions.")
		result = []
		for i in range(0, self.rows_count()):
			result.append([el1 + el2 for el1, el2 in zip(self.value[i], other.value[i])])
		return Matrix(result)

	def __radd__(self, other):
		return self.__add__(other)

	def __iadd__(self, other):
		self = self.__add__(other)
		return self
	
	def __sub__(self, other):
		if not isinstance(other, Matrix):
			raise ValueError("Matrix value is required.")
		elif len(self.value) != len(other.value) or len(self.value[0]) != len(other.value[0]):
			raise ValueError("Matrix have different dimensions.")
		return self + (-other)
	
	def __isub__(self, other):
		self = self.__sub__(other)
		return self

	def __mul__(self, other):
		result = []
		if isinstance(other, numbers.Number):
			for r in self.value:
				result.append([x * other for x in r])
			return Matrix(result)
		elif isinstance(other, Matrix):
			if (self.columns_count() != other.rows_count()):
				raise ValueError("Matrix doesn't have appropriate dimensions.")
			for r in self.value:
				tmp = []
				for i in range(0, other.columns_count()):
					tmp.append(sum([a*b[i] for a, b in zip(r, other.value)]))
				result.append(tmp)
			return Matrix(result)
		else:
			raise ValueError("This type can't be used as multiplier.")

	def __rmul__(self, other):
		if isinstance(other, Matrix):
			return self.__mul__(other)
		elif isinstance(other, numbers.Number):
			return self.__mul__(other)
		else:
			raise ValueError("This type can't be used as multiplier.")
	
	def __imul__(self, other):
		self = self.__mul__(other)
		return self

	def __copy__(self):
		value = copy.deepcopy(self.value)
		return Matrix(value)
	
	def __eq__(self, other):
		if (isinstance(other, Matrix)):
			return self.value == other.value
		else:
			return False
	'''
	def __div__(self, other):
		result = []
		if isinstance(other, numbers.Number):
			for r in self.value:
				result.append([x / other for x in r])
			return Matrix(result)
		else:
			raise ValueError("This type can't be used as division.")

	def __rdiv__(self, other):
		if isinstance(other, numbers.Number):
			return self.__mul__(other)
		else:
			raise ValueError("This type can't be used as division.")
	'''

	def __truediv__(self, other):
		result = []
		if isinstance(other, numbers.Number):
			for r in self.value:
				result.append([x / other for x in r])
			return Matrix(result)
		else:
			raise ValueError("This type can't be used as division.")

	def __itruediv__(self, other):
		self = self.__truediv__(other)
		return self
