from odoo import fields, models, api, _


class ConstructionWorks(models.Model):
    _name = "construction.works"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Construction Works"

    name = fields.Char("Name", default="New")
    customer_id = fields.Many2one('res.partner', tracking=True)
    expiration_date = fields.Date(string="Expiration")
    quotation = fields.Datetime(string="Quotation")
    payment = fields.Selection([('15 days', '15 Days'), ('30 days', '30 Days')]) 
    state = fields.Selection([('quotation', 'Quotation'), ('quotation sent', 'Quotation Sent'), ('sales order', 'Sales Order')])
    construction_lines_ids = fields.One2many('construction.works.lines', 'construction_id', string="construction")
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
        default=lambda self: self.env.company.currency_id.id)
    amount_total = fields.Monetary(string="Total", compute="get_amount_total")
    ref = fields.Char(string = "ref")
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('construction.sequence') or _('New')
        return super(ConstructionWorks, self).create(vals)


    @api.depends('construction_lines_ids.subtotal')
    def get_amount_total(self):
        for order in self:
            total = 0
            for line in self.construction_lines_ids:
                total = total + line.subtotal
            order.write({'amount_total' : total})
