from string import Template, ascii_lowercase
import json

class enigma:
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
    '''
    The permutate function permutates the letters.
    '''
    def permutate(self, rotor):
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        return new_alphabet

    '''
    The inverse_permutate function permutates the letters inversely.
    '''
    def inverse_permutate(self, rotor):
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[0])
            new_alphabet.pop(0)
        print(self.alphabet)
        print(new_alphabet)
        return new_alphabet

    '''
    The encrypt function encrypts the text
    '''
    def encrypt_text(self, text):
        encrypted_text = []
        text = text.lower()
        text.split()

        for letter in text:
            if letter in self.steckerbrett:
                encrypted_text.append(self.steckerbrett[letter])
                self.alpha += 1
                if self.alpha % 26 == 0:
                    self.beta += 1
                    self.alpha = 0
                if self.beta % 26 == 0 and self.alpha % 26 != 0 and self.beta >= 25:
                    self.gama += 1
                    self.beta = 1
            else:
                temp_letter = self.permutate(self.alpha)[self.alphabet.index(letter)]
                temp_letter = self.permutate(self.beta)[self.alphabet.index(letter)]
                temp_letter = self.permutate(self.gama)[self.alphabet.index(letter)]
                temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                    
                temp_letter = self.inverse_permutate(self.gama)[self.alphabet.index(temp_letter)]
                print("gama - {}". format(temp_letter))
                temp_letter = self.inverse_permutate(self.beta)[self.alphabet.index(temp_letter)]
                print("beta - {}". format(temp_letter))
                temp_letter = self.inverse_permutate(self.alpha)[self.alphabet.index(temp_letter)]
                print("alpha - {}". format(temp_letter))
                encrypted_text.append(temp_letter)
                print(temp_letter)
        return ''.join(encrypted_text)

Enigma = enigma({"b":'a', ' ':' ', 'e':'z'}, alpha = 5, beta = 17, gama = 24)
print(Enigma.encrypt_text('there is no way'))