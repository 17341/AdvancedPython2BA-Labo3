from math import *
import scipy.integrate as integrat
from scipy.integrate import quad
import scipy.special as special
def fact(n):
	if type(n) != int:
		raise TypeError
	if n< 0:
		raise  ValueError()
	if n in range(0,2):
		return 1
	else :
		return n*fact(n-1)

def roots(a, b, c):
	delta = (b**2)-(4*a*c)
	if type(a) != int:
		raise TypeError
	if type(b) != int:
		raise TypeError
	if type(c) != int:
		raise TypeError
	if delta>0:
		x1 = (-b+sqrt(delta))/(2*a)
		x2 = (-b-sqrt(delta))/(2*a)
		return x1,x2
	if delta<0:
		return 'No roots'
	if delta==0:
		x = (-b)/2*a
		return x
	pass

def integrate(function, lower, upper):

	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	def f(x):
		return eval(function)

if __name__ == '__main__':
	print(fact('k'))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
#