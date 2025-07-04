# FastFood Menu API Task Description
## Objective
### Create an application that:

- Collects information about all menu items (e.g., McDonald's).

- Saves the collected data locally in a JSON file.

- Provides a REST API to access this data.

## Data Fields to Collect
### For each product, collect the following fields:

name — product name

description — product description

calories

fats

carbs

proteins

unsaturated_fats

sugar

salt

portion — portion size (weight/volume)

## Data Storage Format
Save data locally in a JSON file named mcDonaldsMenu.json.

The data structure can be either:

A list of dictionaries (each representing a product), or

A dictionary where keys are product names and values are their details.

## API Requirements
Use FastAPI or Flask to implement the API with the following endpoints:

GET /all_products/
Returns complete information about all products.

GET /products/{product_name}
Returns detailed information about a single product by its name.

GET /products/{product_name}/{product_field}
Returns the value of a specific field for the given product.
For example, /products/Big_Mac/calories returns the calories of "Big Mac".

![image](https://github.com/user-attachments/assets/8d117dd3-b360-41b3-827b-addadaee0479)
![image](https://github.com/user-attachments/assets/2040141a-1416-4799-add0-c19dd527a5b7)
![image](https://github.com/user-attachments/assets/8ffc9a91-80ef-40ec-bdc3-2a1c5ca5be9f)
![image](https://github.com/user-attachments/assets/5aff4aa9-aa6e-4557-8b4a-e33d0ee2f2d1)



