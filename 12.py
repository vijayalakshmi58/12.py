# 12.py
n = int(input())
temp=n
rev=0
while(n>0):
  digit=n%10
  rev=rev*10+digit
  n=n//10
if(temp==rev):
  print("yes")
else:
  print("yes")
