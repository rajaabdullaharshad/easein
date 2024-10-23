frappe.ui.form.on('Sales Invoice', {
   custom_brand: function(frm) {
        console.log("hello");
        
        frm.set_query('item_code', 'items', () => {
            return {
                filters: {
                    'brand': frm.doc.custom_brand  // Brand filter
                }
            };
        });
    }
});
