from src.сategory import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Mercedes Bens S600", "Объем двигателя 4.0 литра,"
                                             " цвет черный, полный привод",
                       12500000.0, 10)
    product2 = Product("BMW X6M", "Объем двигателя 4.4 литра,"
                                  " цвет серый, полный привод",
                       10500000.0, 5)
    product3 = Product("AUDI A8", "Объем двигателя 4.0 литра,"
                                  " цвет белый, полный привод",
                       9500000.0, 12)

    category1 = Category("Автомобили", "Автомобили, как средство передвижения",
                         [product1, product2, product3])

    print(category1.products)

    product4 = Product("AUDI Q8", "Объем двигателя 4.0 литра,"
                                  "цвет оранжевый, полный привод",
                       12000000.0, 5)

    category1.add_product(product4)

    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Jaguar F-TYPE", "description": "Объем двигателя 4.4 литра, "
         "цвет красный, задний привод", "price": 6000000.0,
         "quantity": 5})

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
