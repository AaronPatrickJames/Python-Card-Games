from asyncio.windows_events import NULL
import random


def main():
    PlayBlackJack()
   
    
def PlayBlackJack():
    current_game = BlackJack()
    current_game.TwoDeck()
    current_game.my_deck.ShowDeck()
    x = len(current_game.my_deck.deck)
    print(str(x))
   
   

#Game Object
class BlackJack:
    
    def __init__(self):
        self.card_dict = {
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
        
        self.suit_list = ["Diamond", "Heart", "Spade", "Clover"] 
    
    def ShuffleMyDeck(self):
        #Shuffle a bunch to ensure randomness
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        self.my_deck.ShuffleDeck()
        

    def OneDeck(self):
        #Deck Object
        self.my_deck = Deck()

        #one deck
        for name in self.card_dict:
            for suit in self.suit_list:
                pass
                #Card Object
                card = Card(suit, self.card_dict[name], name)
                #Insert Card into Deck
                self.my_deck.AddToDeck(card)
        
        #Shuffle the deck
        self.ShuffleMyDeck()     
            

    def TwoDeck(self):
        #Deck Object
        self.my_deck = Deck()
        #two decks
        for i in range(2):
            for name in self.card_dict:
                for suit in self.suit_list:
                    pass
                    #Card Object
                    card = Card(suit, self.card_dict[name], name)
                    #Insert Card into Deck
                    self.my_deck.AddToDeck(card)
                    
        #Shuffle the deck
        self.ShuffleMyDeck()    
        
    def FourDeck(self):
        pass
    
    def SixDeck(self):
        pass
    
    def EightDeck(self):
        pass
     
        
#Deck Object
class Deck:
    
    def __init__(self):
        self.deck = []
       
    def AddToDeck(self, my_card):
        self.deck.append(my_card)
        
    def ShuffleDeck(self):
        random.shuffle(self.deck)
    
    def ShowDeck(self):
        for card in self.deck:
            print( str(card.name) + " of " + str(card.suit) + " " + str(card.value) )
        

#Card Object
class Card:
    
    def __init__(self, suit, value, name):
        self.suit = suit
        self.value = value
        self.name = name
      
    def display(self):
        print(str(self.value) + " Of " + str(self.suit))






#Check if program is running in main
if __name__ == "__main__":
    main();