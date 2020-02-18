####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'We_love_csp'
strategy_name = 'collude until betrayed then betray'
strategy_description = 'our program will collude. Though, if the other program betrays, then it will betray'
    def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if 'b' in their_history: 
       return 'b'
    else:
       return 'c'