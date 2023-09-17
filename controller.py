from app.app import app, db
from models.models import Invoice, InvoiceItem
from routers.routers import create_invoicing_detail_of_item,add_invoice_of_created_item,get_list_invoices,specific_invoice_item
from sqlalchemy import create_engine

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port=5000,debug=True)