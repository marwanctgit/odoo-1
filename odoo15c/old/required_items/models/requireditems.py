from odoo import api, fields, models,_

class RequiredItems(models.Model):
    _name = "required.items"
    _description = "RequiredItems"


    name = fields.Char("Name", default="New")
    items = fields.Char(string="Items")
    quanity  = fields.Integer(string="quantity")
    state = fields.Selection([('quotation', 'Quotation'), ('quotation sent', 'Quotation Sent'), ('sales order', 'Sales Order')])
    required_lines_ids = fields.One2many('required.items.lines', 'required_id', string="Required")
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
        default=lambda self: self.env.company.currency_id.id)
    amount_total = fields.Monetary(string="Total", compute="get_amount_total")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('required.sequence')
            return super(RequiredItems, self).create(vals)

    @api.depends('required_lines_ids.subtotal')
    def get_amount_total(self):
        for order in self:
            total = 0
            for line in self.required_lines_ids:
                total = total + line.subtotal
            order.write({'amount_total' : total})
