from colorama import Fore

class Item:
    def __init__(self, name, description=''):
        self.name = name;
        self.description = description or ''
    
    def on_take(self):
        print('You have picked up ' + Fore.RED +f'{self.name}')
        print(Fore.WHITE + '')
    
    def on_drop(self):
        print('You have dropped ' + Fore.RED +f'{self.name}')
        print(Fore.WHITE + '')
