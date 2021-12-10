# -*- coding: utf-8 -*-
{
    'name': "Mahasiswa",
    'summary': "data mahasiswa",
    'description': """
        berisi informasi mahasiswa:
        -data mahasiswa
        -data prodi
        -dst
    """,
    'author': "kelvzxu",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mahasiswa_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
