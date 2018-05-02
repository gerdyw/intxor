from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def main():
	fig = plt.figure()
	ax = fig.gca(projection='3d')

	X = np.arange(-32, 32, 1)
	Y = np.arange(-32, 32, 1)
	X, Y = np.meshgrid(X, Y)
	Z = arrayXor(X, Y)
	
	surf = ax.scatter(X, Y, Z)

	ax.set_zlim(-32, 32)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%d'))
	
		ax.view_init(elev=25, azim = i)
		plt.savefig('this' + str(i) + '.png')
		print(i)
	
	
	

def arrayXor(X, Y):
	_array = []
	for i in range(len(X)):
		line = []
		for j in range(len(X[i])):
			_res = X[i][j] ^ Y[i][j]
			line.append(_res)
		_array.append(line)
	return np.array(_array)
main()
