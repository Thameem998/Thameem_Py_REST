from app.app import app,db,date
from models.models import Invoice, InvoiceItem
from settings.settings import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from app.app import jsonify,request

    
@app.route('/create_invoicing_detail_of_item', methods=['POST'])
def create_invoicing_detail_of_item():
    new_invoice = Invoice(date=date.today())
    db.session.add(new_invoice)
    db.session.commit()
    return "Hey there, Welcome. Now your invoice has been created successfully. Congratulations!"


@app.route('/api/invoice/<int:invoice_id>/add_invoice_of_created_item', methods=['POST'])
def add_invoice_of_created_item(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return "Invoice not found", 404
    
    if request.method == 'POST':
        data = request.form
        item = InvoiceItem(
            units=data['units'],
            description=data['description'],
            amount=data['amount'],
            invoice=invoice
        )
        db.session.add(item)
        db.session.commit()
        
        return "Hey there, Welcome. Now your nnvoice item has been added successfully. Congratulations!", 201 
    
    return "Oops! It is an invalid request", 400


@app.route('/get_list_invoices', methods=['GET'])
def get_list_invoices():
    invoices = Invoice.query.all()
    invoice_list = []
    for invoice in invoices:
        invoice_data = {
            'id': invoice.id,
            'date': invoice.date.strftime('%Y-%m-%d'),
            'items': []
        }
        for item in invoice.items:
            item_data = {
                'id': item.id,
                'units': item.units,
                'description': item.description,
                'amount': str(item.amount)
            }
            invoice_data['items'].append(item_data)
        invoice_list.append(invoice_data)
    return jsonify(invoice_list)


@app.route('/api/invoice/<int:invoice_id>/specific_invoice_item', methods=['GET'])
def specific_invoice_item(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return "Oops! Crashed -> Actually the invoice was not found"
    
    items = invoice.items
    item_list = []
    for item in items:
        item_list.append({
            'Please find the id alongside here ': item.id,
            'Please find the units alongside here': item.units,
            'Please find the description alongside here': item.description,
            'Please find the amount alongside here': str(item.amount)
        })
    return jsonify(item_list)
