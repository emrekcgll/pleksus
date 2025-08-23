{
    'name': "Pleksus Web",
    'summary': "Pleksus şirketinin web sitesi ve sayfaları",
    'description': """
        Pleksus şirketinin web sitesi için özel modül.
        
        Özellikler:
        - Ana sayfa tasarımı
        - Hizmetler bölümü
        - Hakkımızda bölümü
        - İletişim formu
        - İstatistikler
    """,
    'author': "Pleksus",
    'website': "https://www.pleksus.com",
    'category': 'Website',
    'version': '1.0.0',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/website_templates.xml',
        'views/service_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'pleksus_web/static/src/css/homepage.css',
            'pleksus_web/static/src/js/homepage.js',
        ],
    },
    'auto_install': False,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'icon': '/pleksus_web/static/description/icon.png',
}

