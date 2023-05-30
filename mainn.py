from abc import ABC, abstractmethod


class CountFreqs(ABC):
    address = ""

    @abstractmethod
    def calculateFreqs(self):
        pass

    def __init__(self, address):
        self.address = address


class ListCount(CountFreqs):
    def calculateFreqs(self):
        listOfFreqs = [0] * 26
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        index = ord(char.lower()) - ord('a')
                        listOfFreqs[index] += 1
        for i, freq in enumerate(listOfFreqs):
            if freq > 0:
                letter = chr(i + ord('a'))
                print(letter,"->", freq)


class DictCount(CountFreqs):
    def calculateFreqs(self):
        dictOfFreqs = {}
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        letter = char.lower()
                        dictOfFreqs[letter] = dictOfFreqs.get(letter, 0) + 1
        for letter, freq in dictOfFreqs.items():
            print(letter,"->", freq)


list_counter = ListCount("weirdWords.txt")

list_counter.calculateFreqs()


dict_counter = DictCount("weirdWords.txt")
dict_counter.calculateFreqs()

