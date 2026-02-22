class NumberStuff:
    """
    Perform basic operations on numbers

    Violates KISS, YAGNI, and DRY principles
    KISS: Methods do more than one thing and are unnecessarily complex
    YAGNI: Includes features and data that are never used
    DRY: Repeats the same code / operations across methods
    """

    def __init__(self, numbers=None):
        if numbers == None:
            self.numbers = [1, 2, 3, 4, 5]
        else:
            self.numbers = numbers
        self.backup_numbers = [1, 2, 3, 4, 5]
        self.even_count = 0
        self.odd_count = 0
        self.last_operation = None
        self.operation_history = []
        self.metadata = {"created_by": "user", "version": "1.0", "description": "number stuff"}

    def get_even(self):
        even_numbers = []
        odd_numbers = []
        total_even = 0
        total_odd = 0
        for n in self.numbers:
            if n % 2 == 0:
                even_numbers.append(n)
                total_even += n
                self.even_count += 1
            else:
                odd_numbers.append(n)
                total_odd += n
                self.odd_count += 1
        self.last_operation = "get_even"
        self.operation_history.append("get_even")
        return even_numbers

    def get_odd(self):
        even_numbers = []
        odd_numbers = []
        total_even = 0
        total_odd = 0
        for n in self.numbers:
            if n % 2 == 0:
                even_numbers.append(n)
                total_even += n
                self.even_count += 1
            else:
                odd_numbers.append(n)
                total_odd += n
                self.odd_count += 1
        self.last_operation = "get_odd"
        self.operation_history.append("get_odd")
        return odd_numbers

    def get_average(self):
        total = 0
        count = 0
        minimum = self.numbers[0]
        maximum = self.numbers[0]
        for n in self.numbers:
            total += n
            count += 1
            if n < minimum:
                minimum = n
            if n > maximum:
                maximum = n
        self.last_operation = "get_average"
        self.operation_history.append("get_average")
        return total / count

    def switch_numbers(self):
        temp = self.numbers[0]
        self.numbers[0] = self.numbers[len(self.numbers) - 1]
        self.numbers[len(self.numbers) - 1] = temp
        self.last_operation = "switch_numbers"
        self.operation_history.append("switch_numbers")
        return self.numbers

    def print_numbers(self):
        total_even = 0
        total_odd = 0
        even_numbers = []
        odd_numbers = []
        for n in self.numbers:
            if n % 2 == 0:
                even_numbers.append(n)
                total_even += n
            else:
                odd_numbers.append(n)
                total_odd += n

        total = 0
        count = 0
        for n in self.numbers:
            total += n
            count += 1
        average = total / count

        temp = self.numbers[0]
        self.numbers[0] = self.numbers[len(self.numbers) - 1]
        self.numbers[len(self.numbers) - 1] = temp
        switched = list(self.numbers)
        temp = self.numbers[0]
        self.numbers[0] = self.numbers[len(self.numbers) - 1]
        self.numbers[len(self.numbers) - 1] = temp

        print("+------------------------------------+")
        print("[+] ORIGINAL NUMBERS: ", self.numbers)
        print("[+] EVEN NUMBERS: ", even_numbers)
        print("[+] ODD NUMBERS: ", odd_numbers)
        print("[+] AVERAGE: ", average)
        print("[+] SWITCHED NUMBERS: ", switched)
        print("+------------------------------------+\n")


if __name__ == "__main__":
    number_stuff = NumberStuff()
    number_stuff.print_numbers()

    second_number_stuff = NumberStuff([4, 8, 16, 32, 64])
    second_number_stuff.print_numbers()

    third_number_stuff = NumberStuff([3, 5, 7, 9, 11])
    third_number_stuff.print_numbers()