# Invoice API

This API allows you to create an invoice, add an item to the Invoice

This API is available at "http://127.0.0.1:5000"

## Endpoints ##

### Create Invoice ###

POST '/create_invoicing_detail_of_item'

Creates the invoice with a new Invoice ID.

#### Example ####
```
POST '/create_invoicing_detail_of_item'

Request Body Sample-

{"invoice_id": 8}
  
```

### Add an item to the invoice ###

POST '/add_invoice_of_created_item/<int:invoice_id>'

Gives the feasibility to add an item to the previously created Invoice ID.

Mandatory Query Parameter:
- id: ID of the created invoice (integer type)

#### Example ####
```
POST '/add_invoice_of_created_item/8'

Request Body Sample-

Body Format: x-www-form-urlencoded

    'units': "78",
    'description': "Sample",
    'amount': 5
  
```

### GET the invoice details ###

GET '/get_list_invoices'

Return the details of the all invoices in a JSON format

#### Example ####

```
GET /get_list_invoices/

Response Body Sample-
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
```

### GET a specific invoice details ###

GET '/<int:invoice_id>/specific_invoice_item'

GET the details of a specific invoice in a JSON return format

#### Example ####

```
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
```
