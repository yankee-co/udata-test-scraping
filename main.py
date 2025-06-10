from fastapi import FastAPI
import json

app = FastAPI()

@app.get('/all_products')
def all_products():
    products = "No products found"
    with open('mcDonaldsMenu.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    return products

@app.get("/product/{product_name}")
def get_product(product_name: str):
    with open('mcDonaldsMenu.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
        product = next(
            (item[product_name] for item in products if product_name in item),
            None
        )
    if product:
        return {"name": product_name, **product}
    return {"error": "Продукт не знайдено"}

@app.get("/product/{product_name}/{field_name}")
def get_product_field(product_name: str, field_name: str):
    with open('mcDonaldsMenu.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
        product = next(
            (item[product_name] for item in products if product_name in item),
            None
        )
    if product and field_name in product:
        return {field_name: product[field_name]}
    return {"error": "Поле не знайдено або продукт не знайдено"}