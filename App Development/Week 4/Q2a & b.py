# q2a it just asks for your name height weight to calculate your bmi
# and once it does, it asks if you want to store info in a file
# ,and you can read it afterwards


try:
    while True:
        name = input('Enter name: ')
        weight = float(input('Enter weight (kg): '))
        height = float(input('Enter height (m): '))

        bmi = weight/height**2
        print(bmi)

        command = input('Store your bmi to file? (Y/N): ')
        if command.upper() == 'Y':
            bmi_File = open('bmi.txt', 'a')
            bmi_File.write(name + ',' + str(bmi) + '\n')
            bmi_File.close()

        command = input('Do you want to continue? (Y/N): ')
        if command.upper() == 'N':
            break

    command = input('Do you want to view BMI record in file? (Y/N): ')
    if command.upper() == 'Y':
        bmi_File = open('bmi.txt', 'r')
        contents = bmi_File.read()
        print(contents)
        bmi_File.close()

except ValueError:
    print("Enter a valid input")
except ZeroDivisionError:
    print("Do not enter 0 as input")
except IOError:
    print("Unable to process file")
except:
    print("Error")
finally:
    print("End of program")


