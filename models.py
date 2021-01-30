from odoo import models, fields

class sugerencias(models.Model):
    _name = "sugerencias"

    title = fields.Char("Titulo")
    DeadLine = fields.Date("Fecha Límite")
    details = fields.Char("Detalles")


