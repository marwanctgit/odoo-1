from odoo import fields, models, api

class RequiredItemsLines(models.Model):
    _name = "required.items.lines"
    _description = "RequiredItemsLines"

    required_id = fields.Many2one("required.items", string="Required Items")
    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Char(string="description")
    quantity = fields.Integer(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
    currency_id = fields.Many2one('res.currency', related='required_id.currency_id')
    subtotal = fields.Monetary(compute='_compute_amount', string = "SubTotal")
    barcode = fields.Char(related="product_id.barcode", string="Barcode")

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.write({"description" :self.product_id.display_name})

    @api.depends('unit_price', 'quantity')
    def _compute_amount(self):
        for rec in self:
            rec.subtotal = rec.unit_price * rec.quantity