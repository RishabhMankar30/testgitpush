import logging
logging.basicConfig(filename="assi_5.log",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
logging.info("we are solving python programming assignment_5")
class calculator:
    logging.info("We are into class: calculator, where we are solving 4 basic operation")
    def add(self):
        try:
            logging.info("We are performing addition operation")
            num1 = float(input("enter a 1st number to perform addition: "))
            logging.info("1st no. is-->%s", num1)
            num2 = float(input("enter a 2nd number to perform addition: "))
            logging.info("2nd no. is-->%s", num2)
            addition = num1 + num2
            logging.info("The addition of two no. is=%s", addition)
            print("{} + {} = {}".format(num1, num2, addition) )
        except Exception as e:
            logging.exception(e)

    def subtract(self):
        try:
            logging.info("We are performing subtraction operation")
            num1 = float(input("enter a 1st number to perform subtraction: "))
            logging.info("1st no. is-->%s", num1)
            num2 = float(input("enter a 2nd number to perform subtraction: "))
            logging.info("2nd no. is-->%s", num2)
            Subtraction = num1 - num2
            logging.info("The Suntraction of two no. is = %s", Subtraction)
            print("{}  -  {} = {}".format(num1, num2, Subtraction))
        except Exception as e:
            logging.exception(e)

    def multi(self):
        try:
            logging.info("We are performing multiplication operation")
            num1 = float(input("enter a 1st number to perform Multiplication: "))
            logging.info("1st no. is-->%s", num1)
            num2 = float(input("Enter a 2nd number to perform Multiplication: "))
            logging.info("2nd no. is-->%s", num2)
            Multiplication = num1 * num2
            logging.info("The Subtraction of two no. is = %s", Multiplication)
            print("{} * {} = {}".format(num1, num2, Multiplication))
        except Exception as e:
            logging.exception(e)

    def divid(self):
        try:
            logging.info("We are performing division operation")
            num1 = float(input("Enter a 1st number to perform division: "))
            logging.info("The 1st number is--> %s", num1)
            num2 = float(input("Enter a 2nd number to perform division: "))
            logging.info("The 2nd number is--> %s", num2)
            Division = num1 / num2
            logging.info("The Division of two no. is = %s", ans)
            print("{} / {} = {}".format(num1, num2, Division))
        except Exception as e:
            logging.exception(e)
c=calculator()
print("1.Addition\n","2.Subtraction\n","3.Multiplication\n","4.Division\n")

while(True):
    select = int(input("Select the number to perform operation: "))
    if select == 1:
        c.add()
        conti = input("Do you want to continue for next operation yes! or no!: ")
        if conti=="yes!":
            pass
        else:
            break

    elif select == 2:
        c.subtract()
        conti = input("Do you want to continue for next operation yes! or not!")
        if conti=="yes!":
            pass
        else:
            break


    elif select == 3:
        c.multi()
        conti = input("Do you want to continue for next operation yes! or not!")
        if conti=="yes!":
            pass
        else:
            break


    elif select == 4:
        c.divid()
        conti = input("Do you want to continue for next operation yes! or not!")
        if conti=="yes!":
            pass
        else:
            break
    else:
        print("Oh! error occor. You have selected a wrong number.")







