from ProductCategory import ProductCategory

class Product:
    def __init__(self,product_id,product_name,product_category:ProductCategory,product_price,product_description):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_category = product_category
        self.product_price = product_price
