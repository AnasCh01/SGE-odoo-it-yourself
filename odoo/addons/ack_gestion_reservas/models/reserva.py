from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AckReserva(models.Model):
    _name = "ack_gestion_reservas.reserva"
    _description = "Reserva"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    date = fields.Datetime(
        string="Fecha y hora",
        required=True,
        tracking=True,
    )

    state = fields.Selection(
        [
            ("draft", "Pendiente"),
            ("confirmed", "Confirmada"),
            ("cancelled", "Cancelada"),
        ],
        string="Estado",
        default="draft",
        tracking=True,
    )

    cliente_id = fields.Many2one(
        comodel_name="ack_gestion_reservas.cliente",
        string="Cliente",
        required=True,
        ondelete="cascade",
        tracking=True,
    )

    servicio_id = fields.Many2one(
        comodel_name="ack_gestion_reservas.servicio",
        string="Servicio",
        required=True,
    )

    empleado_id = fields.Many2one(
        comodel_name="ack_gestion_reservas.empleado",
        string="Empleado",
    )

    price = fields.Float(
        string="Precio",
        compute="_compute_price",
        store=True,
    )

    date_delay = fields.Float(
        string="Duración (horas)",
        compute="_compute_date_delay",
        store=True,
    )

    @api.depends("servicio_id")
    def _compute_price(self):
        for record in self:
            record.price = record.servicio_id.price if record.servicio_id else 0.0

    @api.depends("servicio_id")
    def _compute_date_delay(self):
        for record in self:
            if record.servicio_id and record.servicio_id.duration:
                record.date_delay = record.servicio_id.duration / 60
            else:
                record.date_delay = 0.0

    @api.constrains("date")
    def _check_date_not_in_past(self):
        for record in self:
            if record.date and record.date < fields.Datetime.now():
                raise ValidationError(
                    "No se pueden crear reservas en el pasado."
                )
