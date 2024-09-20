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

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Автомобили", "Автомобили, как средство передвижения",
                         [product1, product2, product3])

    print(category1.name == "Автомобили")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("YAMAHA R1", "Объем двигателя 998 куб.см, "
                                    "цвет синий, задний привод",
                       2890000.0, 14)
    category2 = Category("Мотоциклы", "Мотоциклы, "
                                      "как средство передвижения",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
