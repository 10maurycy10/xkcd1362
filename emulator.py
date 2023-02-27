#!/bin/env python3
import random

def plotdot(switchboard):
    """
    Convert the switchboard dict into a graphvis graph file
    """
    print("digraph {")
    for state in switchboard["stateDecode"].keys():
        decode = switchboard['stateDecode'][state]
        if decode['table'] == 'ESCAPESTATION':
            continue
        table = switchboard["tables"][decode["table"]]
        statedescription = decode["table"] + ":" + state

        print(f'"{state}" [label="{statedescription}"];')

        if table.get(state):
            for word in table[state].keys():
                for (i,answer) in enumerate(table[state][word]):
                    print(f'"{state}:{word}:{i}";')
                    print(f'"{state}" -> "{state}:{word}:{i}";')
                    print(f'"{state}:{word}:{i}" [label="{answer["stmt"]}"];')
                    print(f'"{state}" -> "{state}:{word}:{i}" [label="{word}"];')
                    if answer["trans"] == '!':
                        pass
                    elif answer["trans"] == '-':
                        print(f'"{state}:{word}:{i}" -> "{state}";')
                    else:
                        print(f'"{state}:{word}:{i}" -> "{answer["trans"]}";')

    print("}")


#        print(statedescription)

#import json
#xkcd = json.loads(open("switchboard.json").read())
#plotdot(xkcd)
#exit()

class XKCD:
    """
    The callback is used to return text
    """
    callback = lambda a: print(a)
    state = None

    def __init__(self, switchboard):
        self.switchboard = switchboard

    def handle_command(self, text):
        """
        Handle a few basic commands, handleCommand() in the xkcd
        """
        if text == "beep":
            self.callback("*sound on*")
        elif text == "mute" or text == "quiet":
            self.callback("*sound off*")
        elif text == "qrs":
            self.callback("*slower code*")
        elif text == "qrq":
            self.callback("*faster code*")

    def lookupResponse(self, text):
        """
        Return a list of avalable responces for a message
        """
        text = text.replace(" ", "")

        # If there is a state and it is not defau;t, look it up, otherwize use an opener.
        if self.state and self.state != self.switchboard["defState"]:
            # Lookup the state and determine what table should be used for the dialog tree
            state = self.switchboard['stateDecode'][self.state]
            # Lookup the current state in the table specified by the stateDecode dictionary
            table = self.switchboard['tables'][state["table"]]
            table_entry = table.get(self.state)
            
            # If the table has an entry for the text
            if table_entry:
                resp = table_entry.get(text)
                if resp:
                    return resp
        
            # Show some help
            if text == "/help":
                return [{
                        "stmt": '|'.join(table_entry.keys()),
                        "trans": '-'
                }]

        if text == "/help":
            return [{
                "stmt": '|'.join(self.switchboard['openers'].keys()),
                "trans": '-'
            }]

        # If still here Print an opener, or a a generic reponse
        opener = self.switchboard['openers'].get(text);
        return opener or self.switchboard['confused']
    
    def chooseResponse(self, options):
        """
        randomly chose an option, using a fallback if no options are passed
        """
        if len(options) == 0:
            return {
                    'stmt': self.switchboard['defResp'],
                    'trans': self.switchboard['defState']
            }
        else:
            return random.choice(options)

    def send_inital(self):
        """
        Starts the simulation
        """
        self.callback("SOS")

    def send(self, text):
        """
        Top level function for handling user input, say() in the xkcd
        """
        self.handle_command(text)
        options = self.lookupResponse(text)
        chosen = self.chooseResponse(options)
        
        # Return chosen option
        self.callback(chosen["stmt"])

        # Update the state
        if chosen['trans'] == '!':
            self.state = self.switchboard['defState']
        elif chosen['trans'] != '-':
            self.state = chosen['trans']

if __name__ == "__main__":
    import json
    import readline
    xkcd = XKCD(json.loads(open("switchboard.json").read()))

    xkcd.callback = lambda text: print(text)

    xkcd.send_inital()

    while True:
        sent = input("> ")
        xkcd.send(sent.lower())


