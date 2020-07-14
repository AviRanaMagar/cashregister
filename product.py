class Product():
    def __init__(self, name, barcode, price, weight):
        self.name = name
        self.barcode = barcode
        self.price = price
        self.weight = weight
        
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        
    def get_barcode(self):
        return self.barcode
    def set_barcode(self, barcode):
        self.barcode = barcode
        
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
        
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight

    def __str__(self):
        return "Product Name: {0}\n Product Barcode: {1}\n Product Price: {2}\n Product Weight: {3}".format(self.get_name(),self.get_barcode(), self.get_price(), self.weight())
    
        
