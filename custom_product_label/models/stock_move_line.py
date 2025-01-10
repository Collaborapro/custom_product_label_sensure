from odoo import models


class StockMoveLine(models.Model):
    _name = "stock.move.line"
    _inherit = ["abstract.stock.label", "stock.move.line"]
