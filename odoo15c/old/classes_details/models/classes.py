from odoo import api, fields, models,_
from odoo.exceptions import UserError

class ClassesDetails(models.Model):
    _name="classes.details"
    _description="ClassesDetails"

    name= fields.Char(string="Class")
    language = fields.Selection([('malayalam', 'Malayalam'), ('hindi', 'Hindi')], string="language")
    donation_line_ids = fields.One2many('class.donations.lines', 'donation_id', string='Donation Lines')
    state = fields.Selection([
        ('draft', 'Draft' ),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')], default='draft', string="Status")
    amount_total = fields.Float("Total", compute="_get_amount_total")
    subject=fields.Char("Subject")
    is_malayalam=fields.Boolean("is malayalam")
    ref = fields.Char(string = "ref")
    

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence']. next_by_code('classes.details')
        return super(ClassesDetails, self).create(vals)


     
    @api.onchange('language')
    def _onchange_language(self):
        if self.language == "malayalam":
            self.is_malayalam = True
        else:
            self.is_malayalam = False

    
    def action_test(self):
        self.write({'state': 'waiting'})

    def unlink(self):
        for each in self:
            if each.state != 'draft':
                raise UserError(_("You cannot delete this record"))
        return super(ClassesDetails, self).unlink()



class ClassesDonationsLines(models.Model):
    _name = "class.donations.lines"
    _description="ClassesDonations"

    
    payment = fields.Char(string='payment method')
    amount = fields.Integer(string='amount')
    donation_id = fields.Many2one('classes.details', string='Donation')
