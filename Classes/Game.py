# Class creation


class Game():
    """
    This method contains the getter and setters, as well as the constructor.
    It also contains the methods that will allow us to check if the prediction
    was right or wrong.
    """

    def __init__(self, word):

        # constructor
        self.word = word

    def showBlanks(self):
        """
        This function will print as many underscores as letter in the given word
        :return:
        """
        length = len(self.word)
        return '_ ' * length

    def Matched(self, guess):
        """
        This function return a True or False flag depending on the param guess.
        If the letter guess is contained in the word it returns true, if not
        the contrary.
        :param guess:
        :return:
        """
        return guess in self.word

    def showGuess(self, guess, blanked):
        """
        This function gets the guess and the blanked string as params, it checks the
        position of the guess in the randomly selected word and then it overwrites
        the blanked string with the letter in the right position returning that to
        the main function.

        :param guess:
        :param blanked:
        :return:
        """
        blanked_list = blanked.split(' ')
        indexes = []

        for pos, letter in enumerate(self.word):
            if letter == guess:
                indexes.append(pos)

        for index in indexes:
            blanked_list[index] = guess

        return " ".join(blanked_list)
