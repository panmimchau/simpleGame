#! /usr/bin/python3
#a simple game created using a class object

class Game():


    def __init__(self,game_list):
        self.game_list = game_list
        

    def display_game(self,game_list):
        print('Here is the current list: ')
        print(game_list)


    

    def position_choice(self):

        choice = 'wrong'

        while choice not in ['0','1','2']:

            choice = input("Pick a position (0,1,2): ")

            if choice not in ['0','1','2']:
                print('Sorry, invalid choice!')

        return int(choice)

    

    def replacemnt_choice(self,game_list,position):

        user_placement = input('Type a string to place at position: ')

        game_list[position] = user_placement

        return game_list

    

    def gameon_choice(self):

        choice = 'wrong'

        while choice not in ['Y','N']:

            choice = input('Keep playing (Y or N): ')

            if choice not in ['Y','N']:
                print("Sorry, I don't understand, please choose Y or N")

        if choice == 'Y':
            return True
        else:
            return False

game_list = [0,1,2]

my_game = Game(game_list)

game_on = True

game_list = [0,1,2]

while game_on:

    my_game.display_game(game_list)

    position = my_game.position_choice()
    
    game_list = my_game.replacemnt_choice(game_list, position)

    my_game.display_game(game_list)

    game_on = my_game.gameon_choice()







