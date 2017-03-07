{
    'name': 'Sistema de Información de Centros de Enseñanza',
    'version': '1.1',
    'author': 'Andrés Jesús Carrillo Martínez',
    'category': 'Accounting & Finance',
    'summary': 'Modulo de gestion de Institutos',
    'sequence': 30,
    'website': 'https://www.iesayala.com',
    'description': """
Es un módulo de ejemplo
======================
Con este modulo haremos nuestra primera aplicación en Odoo.
    """,
    'license' : 'AGPL-3',
    'depends': ['sale','base_setup', 'product', 'analytic', 'report'],
    'data': [
        'views/partner_view.xml',
        'views/instituto_view.xml',
        'views/asignaturas_view.xml',
        'views/consultas_view.xml',
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}