import random
import time


def list_print(list_1: list):
    for i in list_1:
        print(i)


def list_print_2(list_1: list, list_2: list, space=20, symbol=''):
    line_before = '-'*(space+10)
    print(line_before)
    for i in list_1:
        real_space = (space-len(i)) * ' '
        print(f'--> {i}{real_space}{list_2[list_1.index(i)]}{symbol}')
    print(line_before)


def ask(text: str):
    asked = input(f'Enter {text} : ')
    return asked


class Main:
    def __init__(self, username: str, password='Test') -> None:
        self.username = username
        self.password = password
        self.money = 20
        self.chests = []
        self.inv = []
        self.shop = ['Bronze Crate', 'Silver Crate',
                     'Gold Crate', 'Diamond Crate']
        self.shop_price = ['10', '30', '60', '100']
        self.cars = {
            'Bronze Crate': ['Old Sedan', 'Rusty Truck', 'Mini Van'],
            'Silver Crate': ['Sports Car', 'Jeep', 'Muscle Car'],
            'Gold Crate': ['Luxury Sedan', 'Drift Car', 'Supercar'],
            'Diamond Crate': ['Hypercar', 'Formula 1', 'Batmobile']
        }

    def profile(self):
        print(f'''
        Username : {self.username}
        Password : {self.password}

        Chests Owned : {len(self.chests)}
        Cars Owned : {len(self.inv)}

        Money : {self.money} $
        ''')

    def show_shop(self):
        list_print_2(self.shop, self.shop_price, symbol=' $')

    def show_inventory(self):
        print('--- Cars ---')
        list_print(self.inv)
        print('--- Chests ---')
        list_print(self.chests)

    def buy(self):
        self.show_shop()
        while True:
            buying = int(ask('which crate you want to buy ans in 1,2,3,4 : '))
            if buying > 0 and buying <= len(self.shop):
                item = self.shop[buying-1]
                price_item = int(self.shop_price[buying-1])
                if self.money >= price_item:
                    print(f'Bought {item} for {price_item} $')
                    self.money -= price_item
                    self.chests.append(item)
                    break
                else:
                    print('Not enough money')
                    break
            else:
                break

    def open_chest(self):
        if len(self.chests) > 0:
            for idx, c in enumerate(self.chests):
                print(f'{idx+1}. {c}')
            choice = int(ask('which chest to open : '))
            if choice > 0 and choice <= len(self.chests):
                chest = self.chests.pop(choice-1)
                print(f'Opening {chest}...')
                time.sleep(1)
                reward = random.choice(self.cars[chest])
                print(f'You got a {reward}!')
                self.inv.append(reward)
        else:
            print('No chests to open')

    def work(self):
        print('Working...')
        time.sleep(1)
        earned = random.randint(5, 15)
        self.money += earned
        print(f'You earned {earned} $')

    def drive(self):
        if len(self.inv) > 0:
            car = random.choice(self.inv)
            print(f'Driving your {car} in a race...')
            time.sleep(2)
            earned = random.randint(20, 50)
            self.money += earned
            print(f'You won the race and earned {earned} $!')
        else:
            print('You need a car to drive. Open a crate first!')


Game = Main('tycoon')

on = True
print('Commands: profile, shop, buy, inv, open, work, drive, quit')
while on:
    inp = ask('command')
    if inp == 'profile':
        Game.profile()
    elif inp == 'buy':
        Game.buy()
    elif inp == 'inv':
        Game.show_inventory()
    elif inp == 'shop':
        Game.show_shop()
    elif inp == 'open':
        Game.open_chest()
    elif inp == 'work':
        Game.work()
    elif inp == 'drive':
        Game.drive()
    elif inp == 'quit':
        on = False
