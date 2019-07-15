class abstract_robot(object):
    def choice(num, tower):
        '''Returns a boolean indicating whether to choose to use the first card or not. '''
        pass

    def chear_choice(num, tower, ptower, discard_pile, deck):
        '''Decide when knowing all decks. '''
        pass

    def get_normal_move(num, tower):
        '''Returns the number to be replaced when choosing the first card. '''
        pass
    
    def get_question_move(num, tower):
        '''Returns the number to be replaced when choosing the question card, -1 for discard. '''
        pass