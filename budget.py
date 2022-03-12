class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    output = [self.name.center(30, '*')]
    for item in self.ledger:
      p1 = item['description'][:23]
      p3 = format(item['amount'], '.2f')
      p2 = ' ' * (30 - (len(p1) + len(p3)))
      output.append(f"{p1}{p2}{p3}")
    output.append(f"Total: {format(self.get_balance(), '.2f')}")
    return '\n'.join(output)

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, withdrawl, description=''):
    if self.check_funds(withdrawl):
      self.ledger.append({'amount': -withdrawl,
                          'description': description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for items in self.ledger:
      balance += items.get('amount', 0)
    return balance

  def transfer(self, transfer_amount, destination):
    if self.check_funds(transfer_amount):
      self.ledger.append({'amount': -transfer_amount,
                          'description': f"Transfer to {destination.name}"})
      destination.ledger.append({'amount': transfer_amount,
                                 'description': f"Transfer from {self.name}"})
      return True
    else:
      return False

  def check_funds(self, amount):
    return True if self.get_balance() >= amount else False

  @property
  def spending(self):
    return round(sum([-x['amount'] for x in self.ledger if x['amount'] < 0]), 2)


def create_spend_chart(categories):
  x = sum([i.spending for i in categories])
  p = []
  for category in categories:
    p.append(('o' * int(category.spending / x * 100 // 10 + 1)).rjust(11))
  s = {0: '100| ', 1: ' 90| ', 2: ' 80| ', 3: ' 70| ', 4: ' 60| ',
       5: ' 50| ', 6: ' 40| ', 7: ' 30| ', 8: ' 20| ', 9: ' 10| ', 10: '  0| '}
  for item in p:
    for i, v in enumerate(item):
      s[i] += f'{v}  '
  s = [x[1] for x in sorted(s.items())]
  s.insert(0, 'Percentage spent by category')
  s.append('    ' + '-' * (2 * len(p) + 4))
  m = max([len(x.name) for x in categories])
  a = [n.name.ljust(m) for n in categories]
  k = {}
  for item in a:
    for i, v in enumerate(item):
      k[i] = k.get(i, ' ' * 5) + f'{v}  '
  k = [x[1] for x in sorted(k.items())]
  s += k
  return '\n'.join(s)


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing.spending)
print(clothing)
print(create_spend_chart([food, clothing, auto]))
