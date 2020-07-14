from product import Product
from purchasedList import ProductList

#print the welcome line
print("-----Welcome to Feduni Checkout!-----")

#program to print list
a = ["Milk 2ltr - $2",
     "Bread - $3",
     "Coffee - $7",
     "Apple - $3.5",
     "Yoghurt - $5.5",
     "Butter - $5.5",
     "Cheese - $10",
     "Honey - $4.5",
     "Banana - $4",
     "Oats - $6",
     "Coke - $5",
     "Cookies - $6"]

# print in new line
print(*a, sep = "\n")

#show the barcode for the user 
b = ["-----Barcode-----",
     "Milk - 1",
     "Bread - 2",
     "Coffee - 3",
     "Apple - 4",
     "Yoghurt - 5",
     "Butter - 6",
     "Cheese - 7",
     "Honey - 8",
     "Banana - 9",
     "Oats - 10",
     "Coke - 11",
     "Cookies - 12"]

# print in new line
print(*b, sep = "\n")

class main():

    def get_barcode(barcode):
        if(barcode=="1"):
            print(a[0])

        elif(barcode=="2"):
            print(a[1])

        elif(barcode=="3"):
            print(a[2])

        elif(barcode=="4"):
            print(a[3])

        elif(barcode=="5"):
            print(a[4])

        elif(barcode=="6"):
            print(a[5])

        elif(barcode=="7"):
            print(a[6])

        elif(barcode=="8"):
            print(a[7])

        elif(barcode=="9"):
            print(a[8])

        elif(barcode=="10"):
            print(a[9])

        elif(barcode=="11"):
            print(a[10])

        elif(barcode=="12"):
            print(a[11])

        elif(barcode=="999"):
            print("This product does not exist in our inventory")

        else:
            print("This is invalid product item")

    #first get the input 
    barcode = input("Please enter the barcode of your item:")
    get_barcode(barcode)
    
    total_item = ProductList("Milk")
    product1 = Product("Milk",1, 2, 2)
    product2 = Product("Bread", 2, 3, 1)
    product3 = Product("Coffee", 3, 7, 1)
    product4 = Product("Apple", 4, 3.5, 1)
    product5 = Product("Yoghurt", 5, 5.5, 1)
    product6 = Product("Butter", 6, 5.5, 1)
    product7 = Product("Cheese",1, 10, 1)
    product8 = Product("Honey", 8, 4.5, 1)
    product9 = Product("Banana", 9, 4, 1)
    product10 = Product("Oats", 10, 6, 1)
    product11 = Product("Coke", 11, 5, 1)
    product12 = Product("Cookies", 12, 6, 1)
    
    total_item.add_product(product1)
    total_item.add_product(product2)
    total_item.add_product(product3)
    total_item.add_product(product4)
    total_item.add_product(product5)
    total_item.add_product(product6)
    total_item.add_product(product7)
    total_item.add_product(product8)
    total_item.add_product(product9)
    total_item.add_product(product10)
    total_item.add_product(product11)
    total_item.add_product(product12)
    price = total_item.get_the_purchased_product()
    
