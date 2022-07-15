class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0
        self.description = ""

    def deposit(self, amount, description=""):
        self.amount = self.amount + amount
        self.description = description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.amount = self.amount - amount
            self.descripton = description
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        return self.amount >= amount

    def __repr__(self):
        cat_len = len(self.category)
        left = int(cat_len / 2) if cat_len % 2 == 0 else int(cat_len / 2 + 1)
        right = int(cat_len / 2)

        output = (
            f'{"*" * (15 - left)}'
            f'{self.category[0:left]}'
            f'{self.category[left:]}'
            f'{"*" * (15 - right)}\n'
        )

        total = 0
        for ledger  in self.ledger:
            amt = f'{ledger["amount"]:0.2f}'
            output += f'{ledger["description"][:23]:<23}{" " * (7 - len(amt))}{amt}\n'
            total += ledger["amount"]
        output += f'Total: {total:>5.2f}'
        return output


def create_spend_chart(categories):
    chart = "Percentage spent by category\n" # title
    totals = {}
    sum_total = 0

    for category in categories:
        ledger = category.ledger
        total = 0
        for withdraw in ledger:
            if withdraw["amount"] < 0:
                total -= withdraw["amount"]
        totals[category.category] = total
        sum_total += total

    percents = {}
    for cat, tot in totals.items():
        percents[cat] = int(tot/sum_total * 10) * 10

    for pct in range(100, -1, -10):
        chart += f'{pct:>3}| '
        for cat, percent in percents.items():
            if percent == pct:
                chart += "o  "
                percents[cat] = percent - 10
            else:
                chart += "   "
        chart += '\n'

    # dashes at bottom
    chart += f'    {"-" * (len(totals) * 3 + 1)}\n'

    # categories printed vertically
    longest = max(len(x.category) for x in categories)
    for index in range(0, longest):
        chart += f'    '
        for category in percents.keys():
            if len(category) > index:
                chart += f' {category[index] } '
            else:
                chart += f'   '
        if index == longest - 1:
            chart += " "
        else:
            chart += " \n"
    # print(chart.__repr__())
    return chart




if __name__ == "__main__":

    dept_a = Category("services")
    dept_a.deposit(20.00, "Initial deposit for services rendered")
    dept_b = Category("household")
    dept_b.deposit(21500.50, "Initial deposit for household items")

    print()
    dept_fmt = 10
    desc_fmt = 15
    print(f'{dept_a.category:<{dept_fmt}} {"get balance":<{desc_fmt}}: {dept_a.get_balance()}')
    print(f'{dept_b.category:<{dept_fmt}} {"get balance":<{desc_fmt}}: {dept_b.get_balance()}')
    print()

    print(f'{dept_b.category:<{dept_fmt}} {"transfer":<{desc_fmt}}: {dept_b.transfer(50.00, dept_a)}')
    print(f'{dept_b.category:<{dept_fmt}} {"ledger":<{desc_fmt}}: {dept_b.ledger}')
    print(f'{dept_a.category:<{dept_fmt}} {"ledger":<{desc_fmt}}: {dept_a.ledger}')
    print()

    print(f'{dept_a.category:<{dept_fmt}} {"amount":<{desc_fmt}}: {dept_a.amount}')
    print(f'{dept_a.category:<{dept_fmt}} {"description":<{desc_fmt}}: {dept_a.description}')
    print(f'{dept_b.category:<{dept_fmt}} {"amount":<{desc_fmt}}: {dept_b.amount}')
    print(f'{dept_b.category:<{dept_fmt}} {"description":<{desc_fmt}}: {dept_b.description}')

    print(dept_a)
    print()
    print(dept_b)

    # from main.py
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    clothing = Category("Clothing")
    auto = Category("Auto")

    # food.deposit(1000, "initial deposit")
    # food.withdraw(10.15, "groceries")
    # food.withdraw(15.89, "restaurant and more food for dessert")
    # print(food.get_balance())

    # food.transfer(50, clothing)
    # clothing.withdraw(25.55)
    # clothing.withdraw(100)

    # auto.deposit(1000, "initial deposit")
    # auto.withdraw(15)

    # from test_module.py: test_create_spend_chart(self):
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    # from main.py
    actual = create_spend_chart([business, food, entertainment])
    expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    print(actual)
    print(expected)
