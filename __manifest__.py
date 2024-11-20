{
    'name': 'Custom Product Labels for Receipts',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Custom labels for products in receipts',
    'description': 'Generate product labels with receipt details.',
    'depends': ['stock', 'product'],
    'data': [
        'report/custom_product_label_template.xml',
        'report/custom_product_label_report.xml',
    ],
    'installable': True,
    'application': False,
}
