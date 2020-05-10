import pickle
from functools import reduce


class TransactionManager:

    def __init__(self, user_name=None) -> None:
        if not user_name:
            self.user_name = input("Enter your name: ")
            self.transactions = {}
        else:
            self.user_name = user_name
            with open(user_name + '.pkl', 'rb') as file:
                self.transactions = pickle.load(file)
        super().__init__()

    def calculate_transactions(self):
        while True:
            inp = input('Enter transaction or type "quit" to stop: ')
            if inp == 'quit':
                self.show_transactions(self.user_name)
                break
            if inp.lower().split(' ')[0] in self.transactions:
                self.transactions[inp.lower().split(' ')[0]] += int(inp.lower().split(' ')[1]),
            else:
                self.transactions[inp.lower().split(' ')[0]] = (int(inp.lower().split(' ')[1]),)
        with open(self.user_name + '.pkl', 'wb') as file:
            pickle.dump(self, file)

    def show_transactions(self, user_name=None):
        if not user_name:
            with open(str(input()) + '.pkl', 'rb') as file:
                trans = pickle.load(file).transactions
        else:
            trans = self.transactions
        for key in trans:
            print(f'{key}: {reduce(lambda x, y: x + y, tuple(trans[key]))}')
        print('Total: ', sum((reduce(lambda x, y: x + y, trans.values()))))
