from odoo import fields, models, api, _

class SaleModule(models.Model):
    _name = "sale.module"
    _description = "Sale Module"

    name = fields.Char("Name", default="New")
    partner_id = fields.Many2one('res.partner', string="costumer")
    number = fields.Integer(string = "Mobile Number")
    address = fields.Char(string = "Address")
    state = fields.Selection([
        ('draft', 'Draft' ),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')])
    sale_lines_ids = fields.One2many('sale.module.lines', 'sale_id', string = 'sale')
    currency_id = fields.Many2one('res.currency', 'Currency', required = True,
        default = lambda self: self.env.company.currency_id.id )
    amount_total = fields.Monetary(string="Total", compute="get_amount_total")

    @api.depends('sale_lines_ids.subtotal')
    def get_amount_total(self):
        for order in self:
            total = 0
            for line in self.sale_lines_ids:
                total = total + line.subtotal
            order.write({'amount_total' : total})

    @api.model
    def create (self,vals):
        if vals.get('name', _('New')) == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.sequence') or _('New')
            return super(SaleModule,self).create(vals)

    def action_done(self):
        self.write({'state':'done'})




    


