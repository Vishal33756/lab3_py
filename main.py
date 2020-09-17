# Author: Vishal Maradana vvm5237@psu.edu
# Collaborator:Sergio Ulloa siu5033@psu.edu
# Collaborator:Krishi Jain kyj5135@psu.edu
# Collaborator:Sangmin Cho sqc6231@psu.edu
# Section: 012R
# Breakout: 10

def sum_n(n):
  if n==0:
    return 0
  else:
    return n+sum_n(n-1)
def print_n(s,n):
  if n==0:
    return
  else:
    print(s)
    print_n(s,n-1)      
def run():
  inta =int(input("Enter an int: "))
  print(f"sum is {sum_n(inta)}.")
  stringa = input("Enter a string: ")
  print_n(stringa,inta)
if __name__== "__main__":
  run()  