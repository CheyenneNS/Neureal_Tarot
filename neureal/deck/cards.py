import random


# does what it says on the tin
def shuffle_deck(deck):
    random.shuffle(deck)


# pick card(s) - call this method multiple times to  multiple unique cards from the deck
def get_card(deck):
    num = random.randint(0, len(deck) - 1)  # the minus 1 fixes the zero indexed array out-of-range error
    card = deck[num]
    del (deck[num])  # so we don't get the same card twice if we're calling this multiple times for the same hand
    rev = random.randint(-1, 1)  # is card reversed? zero (false) or 1 (true)
    n = (card, rev)  # tuple of card dictionary + 1 or zero for reversal
    return n


# array of dicts for each card
def get_deck():
    deck = [

        {"name": "The Fool", "url": "the_fool", "image": "images/00.png",
         "message": "keep on the move",
         "sequence": 0,
         "cardtype": "major"},

        {"name": "The Conjurer", "url": "the_conjurer", "image": "images/1_1.png",
         "message": "create a new reality",
         "sequence": 1,
         "cardtype": "major"},

         {"name": "The Mage", "url": "the_mage", "image": "images/01.png",
         "message": "create a new reality",
         "sequence": 1,
         "cardtype": "major"},

        {"name": "The Priestess", "url": "the_priestess", "image": "images/02.png",
         "message": "A spiritual mother of intellect and intuition",
         "sequence": 2,
         "cardtype": "major"},

        {"name": "The Empress", "url": "the_empress", "image": "images/03.png",
         "message": "Abundance, growth, protection",
         "sequence": 3,
         "cardtype": "major"},

          {"name": "The Goddess", "url": "the_goddess", "image": "images/3_5.png",
         "message": "Abundance, growth, protection",
         "sequence": 3,
         "cardtype": "major"},

        {"name": "The Emperor", "url": "the_emperor", "image": "images/04.png",
         "message": "show leadership and responsibility",
         "sequence": 4,
         "cardtype": "major"},

         {"name": "The Hedemony", "url": "the_hedemony", "image": "images/4_7.png",
         "message": "show leadership and responsibility",
         "sequence": 4,
         "cardtype": "major"},

        {"name": "The Preacher", "url": "the_preacher", "image": "images/05.png",
         "message": "respect knowledge and education",
         "sequence": 5,
         "cardtype": "major"},

        {"name": "The Prophet", "url": "the_prophet", "image": "images/05_5.png",
         "message": "divine knowledge",
         "sequence": 5,
         "cardtype": "major"},

        {"name": "The Hierophant", "url": "the_hierphant", "image": "images/5_5.png",
         "message": "divine knowledge and foresight",
         "sequence": 5,
         "cardtype": "major"},

        {"name": "The Lovers", "url": "the_lovers", "image": "images/06.png",
         "message": "follow the path of the heart.",
         "sequence": 6,
         "cardtype": "major"},

        {"name": "The Chariot", "url": "the_chariot", "image": "images/7_5.png",
         "message": "race, reach, and win",
         "sequence": 7,
         "cardtype": "major"},

        {"name": "The Vehicle", "url": "the_vehicle", "image": "images/07.png",
         "message": "dare and win",
         "sequence": 7,
         "cardtype": "major"},

        {"name": "Lust", "url": "lust", "image": "images/08.png",
         "message": "Getting it on to get it off",
         "sequence": 8,
         "cardtype": "major"},

        {"name": "Strength", "url": "strength", "image": "images/8_5.png",
         "message": "Growth, courage, and taming lions of time",
         "sequence": 8,
         "cardtype": "major"},

        {"name": "The Hermit", "url": "the_hermit", "image": "images/9_5.png",
         "message": "look for the essence of things",
         "sequence": 9,
         "cardtype": "major"},

        {"name": "The Time-Keeper", "url": "the_time_keeper", "image": "images/09.png",
         "message": "The essence of all timely bound things",
         "sequence": 9,
         "cardtype": "major"},

        {"name": "Wheel of Fortune", "url": "the_wheel_of_fortune", "image": "images/10.png",
         "sequence": 10,
         "message": "accept life’s ups and downs",
         "cardtype": "major"},

        {"name": "Contingency", "url": "the_contingency_1", "image": "images/10_9.png",
         "sequence": 10,
         "message": "To live is to play",
         "cardtype": "major"},
        
        {"name": "Contingency", "url": "the_contingency_2", "image": "images/10_7.png",
         "sequence": 10,
         "message": "To live is to play",
         "cardtype": "major"},
        
        {"name": "Twist of Fates", "url": "twist_of_fates", "image": "images/10_5.png",
         "sequence": 10,
         "message": "accept life’s ups and downs",
         "cardtype": "major"},

        {"name": "Justice", "url": "justice_1", "image": "images/11.png",
         "message": "judge and be judged in kind",
         "sequence": 11,
         "cardtype": "major"},

        {"name": "Justice", "url": "justice_2", "image": "images/11_5.png",
         "message": "judge and be judged in kind",
         "sequence": 11,
         "cardtype": "major"},

        {"name": "The Translator", "url": "the_translator", "image": "images/12.png",
         "message": "Translating perspectives from the here and now to the there and then and back again",
         "sequence": 12,
         "cardtype": "major"},

        {"name": "Death", "url": "death", "image": "images/13.png",
         "message": "give up what is over and start anew",
         "sequence": 13,
         "cardtype": "major"},

        {"name": "Temperance", "url": "temperance", "image": "images/14.png",
         "message": "find the golden mean",
         "sequence": 14,
         "cardtype": "major"},

        {"name": "Temperance", "url": "temperance", "image": "images/14_5.png",
         "message": "find the golden mean",
         "sequence": 14,
         "cardtype": "major"},
        
        {"name": "Art", "url": "art", "image": "images/14_7.png",
         "message": "find the golden ratio",
         "sequence": 14,
         "cardtype": "major"},
        
        {"name": "Reconciliation", "url": "reconciliation", "image": "images/14_9.png",
         "message": "balance the scales",
         "sequence": 14,
         "cardtype": "major"},

        {"name": "The Devil", "url": "the_devil", "image": "images/15.png",
         "message": "express passion and desire.",
         "sequence": 15,
         "cardtype": "major"},
        
        {"name": "Lucifer", "url": "lucifer", "image": "images/15_5.png",
         "message": "passion and desire to excess.",
         "sequence": 15,
         "cardtype": "major"},


        {"name": "The Tower", "url": "the_tower", "image": "images/16.png",
         "message": "falling to the solid ground of reality",
         "sequence": 16,
         "cardtype": "major"},

        {"name": "The Star", "url": "the_star", "image": "images/17.png",
         "message": "flow from a pure source",
         "sequence": 17,
         "cardtype": "major"},

        {"name": "Hope", "url": "hope", "image": "images/17_5.png",
         "message": "hope is a thing with feathers",
         "sequence": 17,
         "cardtype": "major"},

        {"name": "Projections", "url": "projections_1", "image": "images/18.png",
         "message": "don’t be afraid to scratch the surface",
         "sequence": 18,
         "cardtype": "major"},

        {"name": "Projections", "url": "projections_2", "image": "images/18_7.png",
         "message": "don’t be afraid to scratch the surface",
         "sequence": 18,
         "cardtype": "major"},
        
        {"name": "Transference", "url": "projections_3", "image": "images/18_5.png",
         "message": "refractions from across the multiverse",
         "sequence": 18,
         "cardtype": "major"},

        {"name": "The Sun", "url": "the_sun", "image": "images/19_9.png",
         "message": "giver of life and vitality",
         "sequence": 19,
         "cardtype": "major"},

        {"name": "Luminance", "url": "luminance_1", "image": "images/19_5.png",
         "message": "strong force of insight and vitality",
         "sequence": 19,
         "cardtype": "major"},

        {"name": "Luminance", "url": "luminance_2", "image": "images/19_7.png",
         "message": "strong force of insight and vitality",
         "sequence": 19,
         "cardtype": "major"},
        
        {"name": "Luminance", "url": "luminance_3", "image": "images/19_9_1.png",
         "message": "strong force of insight and vitality",
         "sequence": 19,
         "cardtype": "major"},

        {"name": "Luminance", "url": "luminance_4", "image": "images/19_9_1.png",
         "message": "strong force of insight and vitality",
         "sequence": 19,
         "cardtype": "major"},

        {"name": "Aeon", "url": "aeon", "image": "images/20.png",
         "message": "Unknown novelty awaits",
         "sequence": 20,
         "cardtype": "major"},

        {"name": "The World", "url": "the_world_1", "image": "images/21_7.png",
         "message": "everything is perfect as it is",
         "sequence": 21,
         "cardtype": "major"},
        
        {"name": "The World", "url": "the_world_2", "image": "images/21_9.png",
         "message": "everything is perfect as it is",
         "sequence": 21,
         "cardtype": "major"},
        
        {"name": "The World", "url": "the_world_3", "image": "images/21.png",
         "message": "everything is perfect as it is",
         "sequence": 21,
         "cardtype": "major"},

        {"name": "Sublimation", "url": "sublimation", "image": "images/21_5.png",
         "message": "Parallel processed overcoming",
         "sequence": 21,
         "cardtype": "major"},
        
        {"name": "Macrocosm", "url": "macrocosm", "image": "images/22.png",
         "message": "ValueError: Multiverse value not found",
         "sequence": 21,
         "cardtype": "major"},

        {"name": "Ace of Coins", "url": "ace_of_coins", "image": "images/pe01.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 22,
         "cardtype": "ace"},

        {"name": "Two of Coins", "url": "two_of_coins", "image": "images/pe02.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 23,
         "cardtype": "minor"},

        {"name": "Three of Coins", "url": "three_of_coins", "image": "images/pe03.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 24,
         "cardtype": "minor"},

        {"name": "Four of Coins", "url": "four_of_coins", "image": "images/pe04.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 25,
         "cardtype": "minor"},

        {"name": "Five of Coins", "url": "five_of_coins", "image": "images/pe05.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 26,
         "cardtype": "minor"},

        {"name": "Six of Coins", "url": "six_of_coins", "image": "images/pe06.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 27,
         "cardtype": "minor"},

        {"name": "Seven of Coins", "url": "seven_of_coins", "image": "images/pe07.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 28,
         "cardtype": "minor"},

        {"name": "Eight of Coins", "url": "eight_of_coins", "image": "images/pe08.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 29,
         "cardtype": "minor"},

        {"name": "Nine of Coins", "url": "nine_of_coins", "image": "images/pe09.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 30,
         "cardtype": "minor"},

        {"name": "Ten of Coins", "url": "ten_of_coins", "image": "images/pe10.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 31,
         "cardtype": "minor"},

        {"name": "Princess of Coins", "url": "princess_of_coins", "image": "images/pe_p.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 32,
         "cardtype": "court"},

        {"name": "Knight of Coins", "url": "knight_of_coins", "image": "images/pe_kn.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 33,
         "cardtype": "court"},

        {"name": "Queen of Coins", "url": "queen_of_coins", "image": "images/pe_q.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 34,
         "cardtype": "court"},

        {"name": "King of Coins", "url": "king_of_coins", "image": "images/pe_k.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 35,
         "cardtype": "court"},

        {"name": "Ace of Wands", "url": "ace_of_wands", "image": "images/wa01.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 36,
         "cardtype": "ace"},

        {"name": "Two of Wands", "url": "two_of_wands", "image": "images/wa02.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 37,
         "cardtype": "minor"},

        {"name": "Three of Wands", "url": "three_of_wands", "image": "images/wa03.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 38,
         "cardtype": "minor"},

        {"name": "Four of Wands", "url": "four_of_wands", "image": "images/wa04.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 39,
         "cardtype": "minor"},

        {"name": "Five of Wands", "url": "five_of_wands", "image": "images/wa05.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 40,
         "cardtype": "minor"},

        {"name": "Six of Wands", "url": "six_of_wands", "image": "images/wa06.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 41,
         "cardtype": "minor"},

        {"name": "Seven of Wands", "url": "seven_of_wands", "image": "images/wa07.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 42,
         "cardtype": "minor"},

        {"name": "Eight of Wands", "url": "eight_of_wands", "image": "images/wa08.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 43,
         "cardtype": "minor"},

        {"name": "Nine of Wands", "url": "nine_of_wands", "image": "images/wa09.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 44,
         "cardtype": "minor"},

        {"name": "Ten of Wands", "url": "ten_of_wands", "image": "images/wa10.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 45,
         "cardtype": "minor"},

        {"name": "Princess of Wands", "url": "princess_of_wands", "image": "images/wa_p.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 46,
         "cardtype": "court"},

        {"name": "Knight of Wands", "url": "knight_of_wands", "image": "images/wa_kn.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 47,
         "cardtype": "court"},

        {"name": "Queen of Wands", "url": "queen_of_wands", "image": "images/wa_q.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 48,
         "cardtype": "court"},

        {"name": "King of Wands", "url": "king_of_wands", "image": "images/wa_k.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 49,
         "cardtype": "court"},

        {"name": "Ace of Cups", "url": "ace_of_cups", "image": "images/cu01.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 50,
         "cardtype": "ace"},

        {"name": "Two of Cups", "url": "two_of_cups", "image": "images/cu02.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "rdesc": "A crisis in a couple relationship, disappointment with someone close to you.",
         "sequence": 51,
         "cardtype": "minor"},

        {"name": "Three of Cups", "url": "three_of_cups", "image": "images/cu03.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 52,
         "cardtype": "minor"},

        {"name": "Four of Cups", "url": "four_of_cups", "image": "images/cu04.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 53,
         "cardtype": "minor"},

        {"name": "Five of Cups", "url": "five_of_cups", "image": "images/cu05.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 54,
         "cardtype": "minor"},

        {"name": "Six of Cups", "url": "six_of_cups", "image": "images/cu06.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 55,
         "cardtype": "minor"},

        {"name": "Seven of Cups", "url": "seven_of_cups", "image": "images/cu07.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 56,
         "cardtype": "minor"},

        {"name": "Eight of Cups", "url": "eight_of_cups", "image": "images/cu08.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 57,
         "cardtype": "minor"},

        {"name": "Nine of Cups", "url": "nine_of_cups", "image": "images/cu09.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 58,
         "cardtype": "minor"},

        {"name": "Ten of Cups", "url": "ten_of_cups", "image": "images/cu10.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 59,
         "cardtype": "minor"},

        {"name": "Princess of Cups", "url": "princess_of_cups", "image": "images/cu_p.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 60,
         "cardtype": "court"},

        {"name": "Knight of Cups", "url": "knight_of_cups", "image": "images/cu_kn.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 61,
         "cardtype": "court"},

        {"name": "Queen of Cups", "url": "queen_of_cups", "image": "images/cu_q.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 62,
         "cardtype": "court"},

        {"name": "King of Cups", "url": "king_of_cups", "image": "images/cu_k.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 63,
         "cardtype": "court"},

        {"name": "Ace of Swords", "url": "ace_of_swords", "image": "images/sw01.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 64,
         "cardtype": "ace"},

        {"name": "Two of Swords", "url": "two_of_swords", "image": "images/sw02.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 65,
         "cardtype": "minor"},

        {"name": "Three of Swords", "url": "three_of_swords", "image": "images/sw03.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 66,
         "cardtype": "minor"},

        {"name": "Four of Swords", "url": "four_of_swords", "image": "images/sw04.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 67,
         "cardtype": "minor"},

        {"name": "Five of Swords", "url": "five_of_swords", "image": "images/sw05.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 68,
         "cardtype": "minor"},

        {"name": "Six of Swords", "url": "six_of_swords", "image": "images/sw06.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 69,
         "cardtype": "minor"},

        {"name": "Seven of Swords", "url": "seven_of_swords", "image": "images/sw07.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 70,
         "cardtype": "minor"},

        {"name": "Eight of Swords", "url": "eight_of_swords", "image": "images/sw08.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 71,
         "cardtype": "minor"},

        {"name": "Nine of Swords", "url": "nine_of_swords", "image": "images/sw09.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 72,
         "cardtype": "minor"},

        {"name": "Ten of Swords", "url": "ten_of_swords", "image": "images/sw10.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 73,
         "cardtype": "minor"},

        {"name": "Princess of Swords", "url": "princess_of_swords", "image": "images/sw_p.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 74,
         "cardtype": "court"},

        {"name": "Knight of Swords", "url": "knight_of_swords", "image": "images/sw_kn.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 75,
         "cardtype": "court"},

        {"name": "Queen of Swords", "url": "queen_of_swords", "image": "images/sw_q.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 76,
         "cardtype": "court"},

        {"name": "King of Swords", "url": "king_of_swords", "image": "images/sw_k.png",
         "message": "404 Error Meaning Value Not Found. Please use organic firmware to embue meaning",
         "sequence": 77,
         "cardtype": "court"}

    ]
    return deck
