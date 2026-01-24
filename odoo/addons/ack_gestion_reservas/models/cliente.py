from odoo import models, fields


class AckCliente(models.Model):
    _name = "ack.cliente"
    _description = "Cliente"

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Teléfono")

    reservation_ids = fields.One2many(
        "ack.reserva",
        "cliente_id",
        string="Reservas",
    )
