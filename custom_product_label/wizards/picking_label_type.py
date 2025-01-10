from odoo import models


class PickingLabelType(models.TransientModel):
    _inherit = "picking.label.type"

    def process(self):
        action = super().process()
        action["context"].update(self.env.context)
        return action
