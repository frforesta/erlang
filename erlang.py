#!/usr/bin/python3

'''
This is an Erlang formulas calculator, brought to you by Francesco Foresta (fr.foresta@gmail.com, francesco.foresta@studio.unibo.it)

The actual version of this program is the 1.2
Version 1.2 - Nov 23rd, 2015 - Added the support to python 3.x
Version 1.1 - Nov 20th, 2015 - Added A and C formulas
Version 1.0 - Nov 1st, 2015

This code is not to be intended for profit, it is just a didactic instrument that can be used by students or by professors in their loooong days of study on the exciting world of teletraffic.
 
This code is also open source and everybody can take and modify it, but I kindly ask you to let me know when this happens as well as I will be happy to be cited in the resulting project :)
'''

from math import factorial
from math import exp
import sys

# Erlang A formula
# This is applied with an infinite service capability

def erlangA(a0,m):
  e = exp(-a0)
  p = 0
  for i in range(0,m-1):
    p += (a0**i/factorial(i))
  return (1 - (p*e))

# Erlang B formula
# This is applied to a pure loss system M/M/m/0

def erlangB(a0,m):
  b = 1
  for j in range(1,m+1):
    prod = a0*b
    b = prod/(prod+j)
  return b

# Erlang C formula
# This is applied to a pure waiting system M/M/m/inf

def erlangC(a0, m):
    num = (a0**m/factorial(m)) * ( m/(m-a0) )
    sum_ = 0
    for i in range(m-1):
        sum_ += (a0**i)/factorial(i)
    den = sum_ + num
    p = num/den
    return p

def main():
  if len(sys.argv) != 4:
    print("usage: ./erlang.py {A|B|C} #servers offeredTraffic")
    sys.exit(1)

  a0 = float(sys.argv[3])
  m = int(sys.argv[2])
  erl = sys.argv[1].lower()
  
  if erl == ('a'):
    a = erlangA(a0,m)
    print("The service degradation probability for A("+str(m)+","+str(a0)+") is equal to: " + str(a))
  elif erl == ('b'):
    b = erlangB(a0,m)
    print("The blocking probability for B("+str(m)+","+str(a0)+") is equal to: " + str(b))
  elif erl == ('c'):
    if m < a0:
      print("WARNING! The formula will not be corrected as well as you choose a number of servers lower than the offered traffic")
    elif m == a0:
      print("DIVISION BY ZERO! Seriously, are you trying to break everything? :D Nevertheless, guess what? The formula cannot be calculated!")
      sys.exit(1)
    c = erlangC(a0,m)
    print("The waiting probability for C("+str(m)+","+str(a0)+") is equal to: " + str(c))

if __name__ == '__main__':
  main()
