
```
cd jmgdo-microservices/CRUD
```

Install the packages that are required:
```
python3 -m pip install flask flask_cors
```

### Run and test the server with cURL
```
python3 products.py
```

Open another Terminal:
```
curl http://localhost:5010/products
```
It is by default a `GET` request

 This should return a JSON with the products that have been preloaded.

<br>

Add new product with `POST` request:

```
curl -X POST -H "Content-Type: application/json" -d '{"id": 145, "name": "Pen", "price": 2.5}' http://localhost:5010/products
```

### Using POSTMAN to test the REST API endpoints

Select `HTTP Request`, then `POST`
To send input as JSON choose `Body`-> `raw` ->`JSON`:

Enter the JSON object and click 'Send':
```
{
    "id":146,
    "name":"Laptop Bag",
    "price":45.00
}
```
This will add the product to your previous list of products.


<br>

Verify the list of products to ensure that the request has gone through and the product is added. Change the request type to `GET` and remove the JSON object from the request body. Click `Send` and observe the output in the response window.

Test the `PUT` endpoint to update product details by changing the price of the item with id 143 to 13.34.S

Set the request type to `PUT` and add the product id to the end of the URL and add the value to be changed as a JSON body and click Send.

```
{
"price":13.33
}
```

```
PUT http://IP_ADDRESS:5000/products/143
```

Verify the product with id 143 to ensure that the request has gone through and the product is updated.
Change the request type to `GET` and remove the JSON object from the request body. Click `Send` and observe the output.

Delete the product with id=144:
```
DELETE http://IP_ADDRESS:5000/products/144
```

Verify with GET method that product was deleted.



