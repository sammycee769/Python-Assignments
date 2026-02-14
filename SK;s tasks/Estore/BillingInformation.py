from CreditcardInformation import CreditCardInformation

class BillingInformation:
    def __init__(self,receiver_phone,receiver_name,delivery_address,credit_card:CreditCardInformation):
        self.receiver_phone = receiver_phone
        self.receiver_name = receiver_name
        self.delivery_address = delivery_address
        self.credit_card = credit_card
