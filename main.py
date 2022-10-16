def get_radius():
        a = input("area of a circle: ")
        r = int(a)/3.14
        sqr = r**.5


        print(round(sqr, 4))
def day_teller():
        userInput = input("give me a number: ")
        result = int(userInput) % 7
        if result == 0:
            print("its sunday")
        if result == 1:
            print("its monday")
        if result == 2:
            print("its tuesday")
        if result == 3:
            print("its wednesday")
        if result == 4:
            print("its thursday")
        if result == 5:
            print("its friday")
        if result == 6:
            print("its saturday")
def prime_or_composite():
        flag = True
        while flag == True:
                num = int(input("enter a number: "))
                for i in range(2, num):
                        if (num % i) == 0:
                                print(num, "is composite number")
                                break
                else:
                        print("prime number")
def leap_year_or_not(self):
        year = input("enter a year: ")

        if int(year)%4 == 0:
                print("its a leap year")
        elif int(year)%100 == 0:
                print("its a leap year")
        elif int(year)%400 == 0:
                print("its a leap year")
        else:
                print("its not a leap year")
def odd_or_even():
        num = input("enter a number: ")
        if int(num)%2 == 0:
                print(f"{num} is even number")
        else:
                print(f"{num} is odd number")

def main():
        list_of_functions = [
                "a. leap year or not", "b. odd or even", "c. prime or composite",
                "d. day teller", "e. find radius"
                ]
        for functions in list_of_functions:
                print(functions)

        choice = input("choose a function: ")
        if choice == "a":
                leap_year_or_not()
        if choice == "b":
                odd_or_even()
        if choice == "c":
                prime_or_composite()
        if choice == "d":
                day_teller()
        if choice == "e":
                get_radius()
      
main()
