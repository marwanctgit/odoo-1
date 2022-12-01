from odoo import api, fields, models,_
from odoo.exceptions import UserError

class StudentDetails(models.Model):
    _name="student.details"
    _description="StudentDetails"
     
    name = fields.Char(string="Student Name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    age = fields.Integer(string= "Age")
    state = fields.Selection([
        ('draft', 'Draft' ),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')], default='draft', string="Status")
    
    def action_test(self):
        self.write({'state': 'cancelled'})

    def unlink(self):
        for each in self:
            if each.state != 'done':
                raise UserError(_("Record cant be deleted"))
        return super(StudentDetails, self).unlink()

