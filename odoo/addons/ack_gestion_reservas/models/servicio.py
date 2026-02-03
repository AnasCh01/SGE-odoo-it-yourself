from odoo import models, fields


class AckServicio(models.Model):
    _name = "ack.servicio"
    _description = "Servicio"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    price = fields.Float(string="Precio", required=True)
    duration = fields.Integer(string="Duración (minutos)")
    active = fields.Boolean(default=True)
    image_1920 = fields.Image(string="Imagen")

    empleado_ids = fields.Many2many(
        comodel_name="ack.empleado",
        string="Empleados que pueden realizar el servicio",
    )
