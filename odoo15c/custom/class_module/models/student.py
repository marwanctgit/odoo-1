from odoo import fields, models, api

class StudentName(models.Model):
    _name = "student.name"
    _description = "Student Name"

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")
    student_id = fields.Many2one('class.module')
    

