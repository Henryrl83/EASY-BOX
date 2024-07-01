# -*- coding: utf-8 -*-
{
    'name': "Easy Box",

    'summary': "App que lanza avisos de incompatibilidad",

    'description': """
Este módulo proporciona un sistema de alertas para detectar y notificar
        datos introducidos que no cumplen con la normativa vigente. Es una herramienta
        diseñada para identificar posibles conflictos, errores o problemas en los datos
        ingresados en el sistema que podrían violar las regulaciones establecidas.
        Cuando se detecta un dato no conforme, el sistema emite una alerta clara y
        concisa para que los usuarios puedan abordar y resolver el problema adecuadamente.
    """,

    'author': "Enrique Raposo López",
    'website': "https://www.Misitioweboficial.com.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    #Para tener nuestro modulo como una aplicacion
    'application' : True,
    'instalable' : True,
}

