
"""
In a tail recursive function the recursive call is the last thing.
there is nothing to be done after the call
This does not necessarily utilise the stack return value properly
"""

""" 
in a non tail recursive function the recursive call is not the last 
there is something to be done after the recursive call 
"""

"""
do note
return 1+func(n-1)
this is not tail recursive as the addition will appen after the return from 
recursive call
"""