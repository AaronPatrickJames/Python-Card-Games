from asyncio.windows_events import NULL


def main():
    pass


class BlackJack:
    
    def __init__(self):
        pass
    
    def PlayableCards(self):
        card_dict = {
            "Ace": [1,11],
            "Two": [2],
            "Three": [3],
            "Four": [4],
            "Five": [5],
            "Six": [6],
            "Seven": [7],
            "Eight": [8],
            "Nine": [9],
            "Ten": [10],
            "Jack": [10],
            "Queen": [10],
            "King": [10]
            }
        
        suit_list = ["Diamond", "Heart", "Spade", "Clover"] 
    
    def OneDeck(self):
        pass
    
    def TwoDeck(self):
        pass
        
    def FourDeck(self):
        pass
    
    def SixDeck(self):
        pass
    
    def EightDeck(self):
        pass
     
        

class Deck:
    
    def __init__(self):
        
        pass

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
      
    def display(self):
        print(str(self.value) + " Of " + str(self.suit))






#Check if program is running in main
if __name__ == "__main__":
    main();