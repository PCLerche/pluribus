import sys

class BasePlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.chips = 10
        self.actions = {0:'fold', 1:'check', 2:'call', 3:'raise'}

    def get_card(self, card):
        self.card = card

    def bet(self):
        self.chips -= 1

    def win(self, amount):
        self.chips += amount

    def action(self, raised=False, extended=False):
        valid = False
        if raised:
            
            while not valid:
                try:
                    if extended:
                        action = int(input('Player: {} Fold (0) Call (2) or Bet (3) ? '.format(self.player_number)))
                        if action in [0, 2, 3]:
                            valid = True
                        else:
                            raise ValueError
                    else:
                        action = int(input('Player: {} Fold (0) or Call (2)? '.format(self.player_number)))
                        if action in [0, 2]:
                            valid = True
                        else:
                            raise ValueError
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    print('please enter a valid action')

        else: 
            while not valid:
                try:
                    action = int(input("Player: {} Fold (0) Check (1) or Bet (3)? ".format(self.player_number)))
                    if action in [0, 1, 3]:
                            valid = True
                    else:
                        raise ValueError
                except KeyboardInterrupt:
                    sys.exit()
                    
                except:
                    print('please enter a valid action')
        return self.actions[action]

    def __lt__(self, player):
        return self.card < player.card

    def __repr__(self):
        return 'Player: {} Card: {}'.format(self.player_number, self.card)

class Agent(BasePlayer):
    def __init__(self, player_number, num_chips=None, num_actions=2):
        super().__init__(player_number)
        if num_chips is None:
            self.chips = 2
        else:
            self.chips = num_chips

    def bet(self, amount):
        self.betting += amount
        self.chips -= amount

    def end_game(self, amount_won=None):
        if amount_won is not None:
            self.chips += amount_won + self.betting 
            self.betting = 0
        else:
            self.betting = 0