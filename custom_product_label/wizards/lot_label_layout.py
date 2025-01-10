from odoo import models


class LotLabelLayout(models.TransientModel):
    _inherit = "lot.label.layout"

    def process(self):
        self.ensure_one()

        active_model = self.env.context.get("active_model", "stock.picking")

        if active_model in ("stock.lot", "stock.move.line", "stock.quant") and self.label_quantity == "lots":
            active_ids = self.env.context.get("active_ids", [])
            docids = (
                active_model == "stock.lot" and self.ids
                or self.env[active_model].browse(active_ids).mapped("lot_id").ids
            )
            xml_id = self.print_format == "zpl" and "stock.label_lot_template" or "stock.action_report_lot_label"
            report_action = self.env.ref(xml_id).report_action(docids)
            report_action.update({"close_on_report_download": True})

            return report_action

        return super().process()
