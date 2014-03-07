#!/usr/bin/python
n=int(raw_input('Introduzca un numero n>0: '))
suma=0.0
for i in range(1,n+1):
  x_i=float(i-1.0/2)/n
  print'El valor de x_i es: %f' % x_i
  print'Subintervalos: ', [(i-1)/float(n),i/float(n) ]
  fx_i= 4.0/(1+x_i**2)
  suma=suma+fx_i
  print'El valor de f(x_i) es: %f' % fx_i
pi = (1.0/n)*suma
print'El valor de pi es:pi=%.35f' %  pi

PI = 3.1415926535897931159979634685441852
print'El valor de pi es:PI=%.35f' %  PI