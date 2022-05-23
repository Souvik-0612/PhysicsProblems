import numpy as np

g = 9.8
v = float(input("Enter the velocity "))
b = 0
while b<=90:
	b += 0.1
	a =(np.pi/180)*b
	c = 2*(v**2)*(np.cos(a))**2

	x = np.linspace( 0, (v**2*np.sin(2*a)/g), 100)
	y = x*np.tan(a) - (g/c)*x**2

	j = 0
	for i in range(1,len(x)):
		A = x[i] - x[i-1]
		B = y[i] - y[i-1]
		j += np.sqrt(A**2 + B**2)
	print(b,"° --> length of the projectile is", j)