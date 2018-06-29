

##########################################################
##########################################################
# description: example that gets the value from numbers on Pd dynamically
# autor: jeraman
# date: 26/04/2010
##########################################################
##########################################################


from time import sleep
from Pd import Pd
from basics_classes.connection import connect
from basic_classes.number import Number
from basic_classes.object import Object
from basic_classes.message import Message


# mains method
if __name__ == '__main__':

    # creates an instance of Pd
    pd = Pd()

    # initializes Pyata
    pd.init()

    # creates a bang
    bang = Message(300, 100, "bang")
    # creates a random object
    rand = Object(300, 200, "random 100")
    # creates a number
    n = Number(300, 300)

    # connects the bang to the random
    connect(bang, 0, rand, 0)
    # connects the outlet from radom to a number
    connect(rand, 0, n, 0)

    # repeat 20 times
    for i in range(1, 20):
        # bangs
        bang.click()
        # gets the updated value form number
        print(n.get_value())
        # sleeps a second
        sleep(1)

    # finishes Pyata
    pd.quit()
