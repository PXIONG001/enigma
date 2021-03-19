from string import ascii_lowercase
import json

''' Initalizing varaibales '''
def __init__(self, steckerbrett = {" ":" "}, settings_file = None, alpha = None, beta = None, gama = None):
    ''' Intializing the enigma '''
    # Creating a list of the alphabet with ascii_lowercase
    self.alphabet = list(ascii_lowercase)

    ''' 
    The steckerbrett is the part of the enigma machine where the encryptor
    would connect each letter in the socket.
    '''
    self.steckerbrett = steckerbrett

    if settings_file != None:
        try:
            self.settings = json.load(open(settings_file, 'r'))[0]
        except IOError as e:
            print("Enigma Error 1: There is no setting file")
        finally:
            self.steckerbrett = self.settings['steckerbrett']
            self.alpha = self.settings['alpha']
            self.beta = self.settings['beta']
            self.gama = self.settings['gama']

    elif alpha != None and beta != None and gama != None and steckerbrett != None:
        if type(steckerbrett) is not dict:
            self.steckerbrett = {" " : " "}
        self.alpha = alpha
        self.beta = beta
        self.gama = gama

    else:
        if type(steckerbrett) is not dict:
            self.steckerbrett = {" " : " "}
        rotors = [self.alpha, self.beta, self.gama]

        for rotor in rotors:
            if rotor == None or type(rotor) is not int or type(rotor) is not float:
                rotor = 0
            else:
                rotor = rotor % 26
            self.alpha = rotors[0]
            self.beta = rotors[1]
            self.gama = rotors[2]

    for letter in list(self.steckerbrett.keys()):
        if letter in self.alphabet:
            self.alphabet.remove(letter)
            self.alphabet.remove(self.steckerbrett[letter])
    self.steckerbrett.update({self.steckerbrett[letter]:letter})
    self.reflector = [letter for letter in reversed(self.alphabet)]

