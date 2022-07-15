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

