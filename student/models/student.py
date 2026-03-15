from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'

    name = fields.Char("Name")
    age = fields.Integer("Age")
    email = fields.Char("Email")
    phone = fields.Char("Phone")