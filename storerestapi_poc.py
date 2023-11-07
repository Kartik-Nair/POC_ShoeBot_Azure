import requests

# Specify the API endpoint URL
api_url = "https://api.storerestapi.com/products"

# Send a GET request to the API
response = requests.get(api_url)
print(response)
# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
    
#     product_data = response.json()

#     for product in product_data:
#         print(product)
        