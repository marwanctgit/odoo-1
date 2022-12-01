from odoo import api, fields, models,_
from odoo.exceptions import UserError

class SchoolDetails(models.Model):
    _name="school.details"
    _inherit=['mail.thread', 'mail.activity.mixin']
    _description="SchoolDetails"
    _rec_name = "subjects"

    subjects = fields.Char(string="Course")
    fee = fields.Selection([('half_term', 'Half Term'), ('full_term', 'Full Term')], string="fee")
    donation_line_ids = fields.One2many('school.donations.lines', 'donation_id', string='Donation Lines')
    state = fields.Selection([
        ('draft', 'Draft' ),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')], default='done', string="Status")
    amount_total = fields.Float("Total", compute="_get_amount_total")
    semester = fields.Char("Semester")
    is_half_term = fields.Boolean("Is half term")

    @api.onchange('fee')
    def _onchange_fee(self):
        if self.fee == 'half_term':
            self.is_half_term = True
        else:
            self.is_half_term = False

    @api.depends("donation_line_ids.amount")
    def _get_amount_total(self):
        for each in self:
            total = 0
            for line in self.donation_line_ids:
                total = total + line.amount
            each.write({'amount_total': total})




    def action_test(self):
        self.write({'state': 'done'})

    def unlink(self):
        for each in self:
            if each.state != 'cancelled':
                raise UserError(_("You cannot delete this record"))
        return super(SchoolDetails, self).unlink()
