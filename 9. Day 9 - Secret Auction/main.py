from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo 

print(logo)
name = input("What is your name ? ")
bid_price = int(input("Bid price: "))
dictionary = {
  name : bid_price
}
stop = 1
#flag = input("Are there other user want to bid ?").lower()
name_max = ""
max = 0

while stop:
  flag = input("Are there other user want to bid ?").lower()
  if flag == 'yes':
    clear()
    name = input("What is your name ? ")
    bid_price = int(input("Bid price: "))
    dictionary[name] = bid_price
  else:
    for name in dictionary:
      if max < dictionary[name]:
        max = dictionary[name] 
        name_max = name;
    stop = 0
    clear()
if stop == 0:
  print(f"The winner is {name_max} with a bid of ${max}")


