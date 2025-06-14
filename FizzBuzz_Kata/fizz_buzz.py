class FizzBuzz:

    @staticmethod
    def run(number: int) -> str:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

if __name__ == "__main__":
    for i in range(1, 101):
        print(FizzBuzz.run(i))