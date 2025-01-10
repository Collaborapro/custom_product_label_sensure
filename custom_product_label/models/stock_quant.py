from odoo import models


class StockQuant(models.Model):
    _name = "stock.quant"
    _inherit = ["abstract.stock.label", "stock.quant"]
