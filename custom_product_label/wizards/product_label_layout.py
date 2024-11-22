from odoo import models


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    def _prepare_report_data(self):
        xml_id, data = super()._prepare_report_data()
        picking_id = self.move_line_ids and self.move_line_ids[0].picking_id or False

        if picking_id:
            data["receipt_date"] = (picking_id.date_done or picking_id.scheduled_date).strftime("%d/%m/%Y") or "N/A"
            data["receipt_name"] = picking_id.name

        return xml_id, data

