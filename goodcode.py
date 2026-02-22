class NumberStuff:
    """
    Perform basic operations on numbers
    """

    def __init__(self, numbers=None):
        if numbers == None:
            self.numbers = [1, 2, 3, 4, 5]
        else:
            self.numbers = numbers

    def get_even(self):
        """
        Returns a list of even numbers given a list of numbers
        """
        return [n for n in self.numbers if n % 2 == 0]

    def get_odd(self):
        """
        Returns a list of odd numbers given a list of numbers
        """
        return [n for n in self.numbers if n % 2 != 0]

    def get_average(self):
        """
        Returns average of all numbers
        """
        total = 0
        for n in self.numbers:
            total += n
        return total / len(self.numbers)

    def switch_numbers(self):
        """
        Returns list of numbers with the first and last element switched
        """
        self.numbers[0], self.numbers[-1] = self.numbers[-1], self.numbers[0]
        return self.numbers

    def print_numbers(self):
        print("[+] ORIGINAL NUMBERS: ", self.numbers)
        print("[+] EVEN NUMBERS: ", self.get_even())
        print("[+] ODD NUMBERS: ", self.get_odd())
        print("[+] AVERAGE: ", self.get_average())
        print("[+] SWITCHED NUMBERS: ", self.switch_numbers())


if __name__ == "__main__":
    number_stuff = NumberStuff()
    number_stuff.print_numbers()