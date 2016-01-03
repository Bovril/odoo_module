# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Employee(models.Model):
    _name = "employee.employee"

    name = fields.Char(string="Employee name")
