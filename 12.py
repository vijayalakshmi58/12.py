# 12.py
m = int(input())
temp=m
rev=0
while(m>0):
  digit=m%10
  rev=rev*10+digit
  m=m//10
if(temp==rev):
  print("yes")
else:
  print("yes")
