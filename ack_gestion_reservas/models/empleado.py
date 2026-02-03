from odoo import models, fields


class AckEmpleado(models.Model):
    _name = "ack_gestion_reservas.empleado"
    _description = "Empleado"

    name = fields.Char(string="Nombre", required=True)
    role = fields.Char(string="Rol")

    service_ids = fields.Many2many(
        comodel_name="ack_gestion_reservas.servicio",
        string="Servicios que puede realizar",
    )

    reserva_ids = fields.One2many(
        comodel_name="ack_gestion_reservas.reserva",
        inverse_name="empleado_id",
        string="Reservas",
    )
