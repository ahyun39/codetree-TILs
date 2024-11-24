class Product:
    def __init__(self, product_name="codetree", product_code=50):
        self.name = product_name
        self.code = product_code
product = Product()
print(f'product {product.code} is {product.name}')

name, code = map(str, input().split())
product = Product(name, code)
print(f'product {product.code} is {product.name}')
