{
    'name': 'Website MegaMenu [Bootstrap]',
    'description': 'This module will implement MegaMenu functionality to improve on the default built-in Odoo menu for use with both the E-commerce and CMS modules.',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch',
    'website': 'https://github.com/OdooCommunityWidgets',
    'depends': ['website'],
    'data': [
        'views/website_category_extended.xml',
        'views/website_menuitem_extended.xml',
        'views/website_settings_extended.xml',
        'views/website_usermenu_extended.xml'
    ],
    'application': True,
}
