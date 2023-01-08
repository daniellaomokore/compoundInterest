# This program shows the user their saving account compound interest after x amount of years.

# "{:.2f}".format() <<<< used to format value to 2d.p

class compound_interest:

    def __init__(self, principle, interest_rate,time):
        self.interest_rate = interest_rate
        self.principle = principle
        self.time = time


    def balance_after_compound_interest(self):
        self.principle = 0
        self.interest_rate = 0
        self.time = 0

        while True:
            principle = float(input("Enter the principle amount: "))
            if principle < 0:
                print("Principle can't be less than zero")
            else:
                break

        while True:
            rate = float(input("Enter the interest rate: "))
            if rate < 0:
                print("Interest rate can't be less than zero")
            else:
                break

        while True:
            time = int(input("Enter the time in years: "))
            if time < 0:
                print("Time can't be less than zero")
            else:
                break

        total = principle * pow((1 + rate / 100), time)
        return f"Balance after {time} year/s: £{total:.2f}"


User = compound_interest(1000,0.04,1)
print(User.balance_after_compound_interest())