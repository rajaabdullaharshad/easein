import frappe

@frappe.whitelist()
def after_insert(doc, method=None):
    if doc.custom_is_supplier:
        try:
            # Create a new Supplier document
            supplier_doc = frappe.new_doc('Supplier')
            supplier_doc.supplier_name = doc.customer_name
            supplier_doc.supplier_group = doc.customer_group
            supplier_doc.supplier_type = doc.customer_type
            
            # Save the new Supplier document
            supplier_doc.insert()
            supplier_doc.save()
            frappe.msgprint(f"Supplier {supplier_doc.supplier_name} created successfully.")
        except Exception as e:
            frappe.log_error(f"Error creating supplier: {str(e)}")
            frappe.msgprint("An error occurred while creating the supplier.")
