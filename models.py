from odoo import models, fields,api

class sugerencias(models.Model):
    _name = "sugerencias"

    title = fields.Char("Titulo")
    DeadLine = fields.Date("Fecha Límite")
    details = fields.Char("Detalles")
    employee = fields.Many2one("hr.employee", "Employee")

class sugerencia_voto(models.Model):
    _name="sugerencia.voto"

    employee = fields.Many2one("hr.employee", "Employee")
    vote = fields.Boolean("Agree")

