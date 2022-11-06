#  1a) try except, valueError. When user enter smth that is not an integer

try:
    count = int(input('How many number you want to capture? '))
    numList = []
    for i in range(count):
        msg = 'Enter number #' + str(i+1) + ' '
        num = int(input(msg))
        numList.append(num)
except ValueError:
    print("Enter a valid number")
else:
    print('The lowest number in the list: ', min(numList))
    print('The highest number in the list: ', max(numList))
    print('The total of the numbers in the list: ', sum(numList))
    print('The average of the numbers in the list: ', sum(numList)/len(numList))
