from odoo import models, fields


class AckEmpleado(models.Model):
    _name = "ack.empleado"
    _description = "Empleado"

    name = fields.Char(string="Nombre", required=True)
    role = fields.Char(string="Rol")
