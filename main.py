from replit import clear
auction={}
from art import logo
print(logo)
print("Welcome to the secret auction program!")
c=""
max=0
kmax=""
while(c!="no"):
  k=input("What is your name?: ")
  b=(int)(input("What's your bid? $"))
  auction[k]=b
  if b>max:
    max=b
    kmax=k
  c=input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
print(f"The winner is {kmax} with a bid of ${max}.")

  
