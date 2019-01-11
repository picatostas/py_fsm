###
#  FSM Example
#
#
###
from fsm import fsm, fsm_trans
import sys



class button():
    def __init__(self):
        self.state = False
        
light_switch = button()

# Define a Dictionary with the states
states = {
    "OFF": "0",
     "ON": "1"
}
# Condition functions
def is_button_pressed():

    if light_switch.state == True:
        print("Light switch pressed")
        return True
    else:
        return False

        
# Actions performed when condition is validated
def turn_on():
    light_switch.state = False
    print("Light ON")


def turn_off():
    light_switch.state = False
    print("Light OFF")

# FSM Transition table

trans_table = [fsm_trans(states["OFF"],  is_button_pressed,  states["ON"], turn_on),
               fsm_trans(states["ON"],   is_button_pressed, states["OFF"], turn_off)]


def main():
    # Initiate the FSM giving a transition table and the initial state

    light_fsm = fsm(trans_table, states["OFF"])
    while True:
        c = sys.stdin.read(1)
        if c == 'p':
            light_switch.state = True
        # FSM activation
        light_fsm.fsm_fire()

main()