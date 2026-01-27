from odoo import models, fields


class AckServicio(models.Model):
    _name = "ack_gestion_reservas.servicio"
    _description = "Servicio"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    price = fields.Float(string="Precio", required=True)
    duration = fields.Integer(string="Duración (minutos)")
    active = fields.Boolean(string="Activo", default=True)
    image_1920 = fields.Image(string="Imagen")
