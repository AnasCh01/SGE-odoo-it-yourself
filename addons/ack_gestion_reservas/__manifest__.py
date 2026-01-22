{
    "name": "Gestión de Reservas",
    "version": "1.0.0",
    "category": "Services",
    "summary": "Gestión de reservas de un negocio de servicios",
    "description": """
Módulo para la gestión de reservas de un negocio de servicios.
Permite administrar servicios, clientes, empleados y reservas,
con control de permisos según el tipo de usuario.
    """,
    "author": "Anas Ch",
    "website": "",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/servicio_views.xml",
    ],
    "demo": [
        "data/demo.xml",
    ],
    "installable": True,
    "application": True,
}
