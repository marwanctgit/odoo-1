from odoo import fields, models, api

class SaleModulelines (models.Model):
    _name = "sale.module.lines"
    _description = "sale module"


    sale_id = fields.Many2one('sale.module', string = "sale")
    product_id = fields.Many2one('product.product', string = "Product")
    description = fields.Char(string = "Description")
    quantity = fields.Integer(string = "Quantity")
    unit_price = fields.Float(string = "Unit Price")
    example = fields.Char(string="Examples")
    currency_id = fields.Many2one('res.currency', related = 'sale_id.currency_id')
    subtotal = fields.Monetary(compute='_compute_amount', string = "subtotal")
    @api.onchange('product_id')
    def onchange_product_id(self):
        if self .product_id:
            self.write({"description" : self.product_id.display_name})

    @api.depends('unit_price', 'quantity')
    def _compute_amount(self):
        for rec in self:
            rec.subtotal = rec.unit_price * rec.quantity





 