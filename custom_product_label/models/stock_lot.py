from odoo import models


class StockLot(models.Model):
    _name = "stock.lot"
    _inherit = ["abstract.stock.label", "stock.lot"]
