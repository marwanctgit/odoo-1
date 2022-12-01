from odoo import api, fields, models

class SchoolDonationsLines(models.Model):
    _name="school.donations.lines"
    _description="SchoolDonations"

    
    payment_ref = fields.Char(string='payment method')
    amount = fields.Integer(string='amount')
    donation_id = fields.Many2one('school.details', string='Donation')