{
    "name": "ACK - Gestión de Reservas",
    "version": "17.0.1.0.0",
    "category": "Services",
    "summary": "Gestión de reservas de un negocio de servicios",
    "description": """
Módulo para la gestión de reservas de un negocio de servicios.
Permite administrar servicios, clientes, empleados y reservas,
con control de permisos según el tipo de usuario.
    """,
    "author": "Anas Ch",
    "depends": ["base", "mail"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",

        "views/servicio_views.xml",
        "views/cliente_views.xml",
        "views/empleado_views.xml",
        "views/reserva_views.xml",

        "views/menu.xml",
    ],
    "demo": [
        "data/demo.xml",
    ],
    "installable": True,
    "application": True,
}
