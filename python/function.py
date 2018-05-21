import os
import fun
import sys
os.system("clear || cls")
def soma(a,b):
  return a+b

nomes=["a","s"]
ret=soma(5,5)

print ret
if ret >  10 or ret == 10:
  print"dez ou maior:",len(nomes)
print "soma(5,5):%i"%(soma(5,5))

alx=sys.argv[1]
print alx
fun.sms()
print "somando eh:",fun.somando()