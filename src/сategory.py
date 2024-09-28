from src.product import Product
class Category:
    """
Для класса Category определен следующие свойства:
название (name),
описание (description),
список товаров категории (products).
    """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.sum_count()}'

    def add_product(self, product_num):
        self.__products.append(product_num)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price}. " \
                           f"Остаток: {product.quantity}.\n"
        return product_str

    def sum_count(self):
        sum_count_product = 0
        for product in self.__products:
            sum_count_product += product.quantity
        return sum_count_product

    @property
    def products_list(self):
        return self.__products
