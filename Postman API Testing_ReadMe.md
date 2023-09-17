# Testing of the API through Postman


# Testing the API using Postman

Access the API at "http://127.0.0.1:5000".

## API Endpoints ##

### Creating an Invoice ###

**Endpoint:** POST '/create_invoicing_detail_of_item'

#### Steps to Test the 'create_invoicing_detail_of_item' Route using Postman:

1. Open Postman.
2. Select the request you want to send, like the POST request to '/create_invoicing_detail_of_item'.
3. Add a Content-Type header with the value 'application/json' in the request headers section.
   - Example:
     - Header: Content-Type
     - Value: application/json
4. Ensure the request body contains valid and properly formatted JSON data as a JSON object.
   - Example:
     - Method: POST
     - URL: http://127.0.0.1:5000/create_invoicing_detail_of_item
     - Headers:
       - Content-Type: application/json
     - Body (raw JSON data): {"invoice_id": 3}

#### Example ####
POST '/create_invoicing_detail_of_item'

Request Body Sample:
{"invoice_id": 3}

Response Body Sample:
Now, the invoice has been created successfully in the system.

### Adding an Item to the Invoice ###

**Endpoint:** POST '/add_invoice_of_created_item/<int:invoice_id>'

Allows adding an item to a previously created invoice.

Mandatory Query Parameter:
- `id`: ID of the created invoice (integer type)

#### Steps to Test the 'add_invoice_of_created_item' Route using Postman:

1. Open Postman.
2. Create a new request in Postman and select the POST method.
3. Set the Request URL by replacing {{ invoice_id }} with the actual invoice ID.
   - Example: http://127.0.0.1:5000/add_invoice_of_created_item/3
4. In the request body section, select the "x-www-form-urlencoded" option to provide form data for the invoice item.
5. Add the necessary form data for the invoice item (units, description, and amount).
6. Click the "Send" button to submit the POST request to the add_invoice_of_created_item route.

#### Example ####

POST '/add_invoice_of_created_item/3'

Request Body Sample:
Body Format: x-www-form-urlencoded
'units': "55",
'description': "Demo",
'amount': 5

Response Body Sample:
Invoice item has been added successfully in the system now.


### Getting Invoice Details ###

**Endpoint:** GET '/get_list_invoices'

Returns details of all invoices in JSON format.

#### Steps to Test the 'get_list_invoices' Route using Postman:

1. Open Postman.
2. Create a new request.
3. Set the request type to GET.
4. Enter the URL for the get_list_invoices route, e.g., http://127.0.0.1:5000/get_list_invoices.
5. Click the "Send" button to send the GET request to the Flask app.

#### Example ####

GET /get_list_invoices/

Response Body Sample:
[
{
"date": "2023-09-17",
"id": 1
},
{
"date": "2023-09-17",
"id": 2
},
{
"date": "2023-09-17",
"id": 3
},
{
"date": "2023-09-17",
"id": 4
},
{
"date": "2023-09-17",
"id": 5
}
]



### Getting Specific Invoice Details ###

**Endpoint:** GET '/<int:invoice_id>/specific_invoice_item'

Returns details of a specific invoice in JSON format.

#### Steps to Test the 'specific_invoice_item' Route using Postman:

1. Open Postman.
2. Create a new request.
3. Set the request type to GET and enter the URL for the specific_invoice_item route, replacing {{ invoice_id }} with the actual invoice ID.
   - Example: http://127.0.0.1:5000/api/invoice/1/specific_invoice_item
4. Click the "Send" button to send the GET request to the specified URL.

#### Example ####

GET /1/specific_invoice_item

Response Body Sample:
[
{
"amount": "55",
"description": "Demo",
"id": 1,
"units": 5
},
{
"amount": "66",
"description": "Tham_Prod",
"id": 1,
"units": 7
}
]
