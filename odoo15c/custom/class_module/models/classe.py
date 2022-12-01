from odoo import fields, models, api,_

class ClassModule(models.Model):
    _name = "class.module"
    _inherit =  ['mail.thread', 'mail.activity.mixin']
    _description = "Class Module"


    name = fields.Char("Name", default="New")
    student = fields.Char(string="Student")
    division = fields.Char(string="Division")
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft', string="Status")
    student_ids = fields.One2many('student.name', 'student_id', string="Student" )

    @api.model
    def create (self,vals):
        if vals.get('name', _('New')) == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('class.sequence') or _('New')
        return super(ClassModule, self).create(vals)

    def action_done(self):
        self.write({'state':'done'})
