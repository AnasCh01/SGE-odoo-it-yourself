from odoo import models, fields, api


class AckReserva(models.Model):
    _name = "ack.reserva"
    _description = "Reserva"

    date = fields.Datetime(string="Fecha y hora", required=True)
    state = fields.Selection(
        [
            ("draft", "Pendiente"),
            ("confirmed", "Confirmada"),
            ("cancelled", "Cancelada"),
        ],
        string="Estado",
        default="draft",
    )

    cliente_id = fields.Many2one(
        "ack.cliente",
        string="Cliente",
        required=True,
        ondelete="cascade",
    )

    servicio_id = fields.Many2one(
        "ack.servicio",
        string="Servicio",
        required=True,
    )

    empleado_id = fields.Many2one(
        "ack.empleado",
        string="Empleado",
    )

    price = fields.Float(
        string="Precio",
        compute="_compute_price",
        store=True,
    )

    @api.depends("servicio_id")
    def _compute_price(self):
        for record in self:
            record.price = record.servicio_id.price if record.servicio_id else 0.0
