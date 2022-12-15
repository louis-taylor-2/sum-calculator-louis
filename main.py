number = int(input("enter a positive integer: "))
counter = 0
while(counter <= number):
  answer = counter + number
  print(str(number) + "+" + str(counter) + "=" + str(answer))
  counter = counter + 1