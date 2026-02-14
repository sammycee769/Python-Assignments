from CardType import CardType

class CreditCardInformation:
    def __init__(self,card_number,name_on_card,cvv,card_type:CardType,expiry_month,expiry_year):
        self.card_number = card_number
        self.name_on_card = name_on_card
        self.cvv = cvv
        self.card_type = card_type
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year

