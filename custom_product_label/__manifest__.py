# -*- coding: utf-8 -*-
{
    "name": "Custom Product Labels for Receipts",
    "version": "1.0",
    "category": "Warehouse",
     "author": "Necte Eloisa Montevecchi",
    "version": "16.0.0.4",
    "website": "https://www.necte.it",
    "summary": "Custom labels for products in receipts",
    "description": "Generate product labels with receipt details.",
    "depends": ["stock", "product", "stock_inventory"],
    "data": [
        "views/stock_lot_views.xml",
        "views/stock_move_line_views.xml",
        "views/stock_quant_views.xml",
        "report/report_productlabel.xml",
    ],
    "installable": True,
    "application": False,
}





