frappe.ui.form.on("Quotation", {
    custom_brand: function(frm) {
       
        
        frm.set_query('item_code', 'items', () => {
            return {
                filters: {
                    'brand': frm.doc.custom_brand  // Brand filter
                }
            };
        });
    }
});