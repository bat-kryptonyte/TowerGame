class player(object):
    def choice(num, tower):
        '''Returns a boolean indicating whether to choose to use the first card or not. '''
        raise NotImplementedError

    def choice(num, tower, ptower, discard_pile, deck):
        '''Decide when knowing all decks. '''
        raise NotImplementedError

    def get_normal_move(num, tower):
        '''Returns the number to be replaced when choosing the first card. '''
        raise NotImplementedError
    
    def get_question_move(num, tower):
        '''Returns the number to be replaced when choosing the question card, -1 for discard. '''
        raise NotImplementedError