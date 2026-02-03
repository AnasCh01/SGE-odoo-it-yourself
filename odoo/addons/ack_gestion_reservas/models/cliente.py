from odoo import models, fields


class AckCliente(models.Model):
    _name = "ack.cliente"
    _description = "Cliente"

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Teléfono")
    image_1920 = fields.Image(string="Imagen")

    reserva_ids = fields.One2many(
        comodel_name="ack.reserva",
        inverse_name="cliente_id",
        string="Reservas",
    )
