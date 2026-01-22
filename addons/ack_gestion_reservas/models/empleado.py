from odoo import models, fields


class AckEmpleado(models.Model):
    _name = "ack.empleado"
    _description = "Empleado"

    name = fields.Char(string="Nombre", required=True)
    role = fields.Char(string="Rol")

    service_ids = fields.Many2many(
        "ack.servicio",
        string="Servicios que puede realizar",
    )

    reservation_ids = fields.One2many(
        "ack.reserva",
        "empleado_id",
        string="Reservas",
    )
