from odoo import models, fields


class AckEmpleado(models.Model):
    _name = "ack.empleado"
    _description = "Empleado"

    name = fields.Char(string="Nombre", required=True)
    role = fields.Char(string="Rol")

    service_ids = fields.Many2many(
        comodel_name="ack.servicio",
        string="Servicios que puede realizar",
    )

    reserva_ids = fields.One2many(
        comodel_name="ack.reserva",
        inverse_name="empleado_id",
        string="Reservas",
    )
