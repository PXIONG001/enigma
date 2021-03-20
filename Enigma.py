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

    # If the setting file is not empty
    if settings_file != None:
        # Open the file
        try:
            self.settings = json.load(open(settings_file, 'r'))[0]
        
        # There is no setting file
        except IOError as e:
            print("Enigma Error 1: There is no setting file")

        # Intialize the variables: steckerbrett, alpha, beta, gama
        finally:
            self.steckerbrett = self.settings['steckerbrett']
            self.alpha = self.settings['alpha']
            self.beta = self.settings['beta']
            self.gama = self.settings['gama']
            
    # If the variables are not empty
    elif alpha != None and beta != None and gama != None and steckerbrett != None:
        # If the steckerbrett is not a dictionary, then initialize it to a dictionary
        if type(steckerbrett) is not dict:
            self.steckerbrett = {" " : " "}
        self.alpha = alpha
        self.beta = beta
        self.gama = gama
    
    # Intialize the rotors
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

def permutate(self, rotor):
    new_alphabet = ''.join(self.alphabet)
    new_alphabet = list(new_alphabet)
    for iter in range(rotor):
        new_alphabet.insert(0, new_alphabet[-1])
        new_alphabet.pop(-1)
    return new_alphabet

def inverse_permutate(self, rotor):
    new_alphabet = ''.join(self.alphabet)
    new_alphabet = list(new_alphabet)
    for iter in range(rotor):
        new_alphabet.insert(0, new_alphabet[0])
        new_alphabet.pop(0)
    print(self.alphabet)
    print(new_alphabet)
    return new_alphabet

