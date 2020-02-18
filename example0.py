team_name = 'We love csp' # Only 10 chars displayed.
strategy_name = 'Collude untill betrayed'
strategy_description = 'our program will collude. Though, if the other program betrays, then it will betray'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if 'b' in their_history: 
       if len(my_history)%2 == 0:
           return 'c'
       else:
           return 'b'
    else: 
       return 'c'
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    