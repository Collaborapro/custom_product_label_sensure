from collections import defaultdict

from odoo import models


class LotLabelLayout(models.TransientModel):
    _inherit = "lot.label.layout"

    def process(self):
        self.ensure_one()

        active_model = self.env.context.get("active_model", "stock.picking")

        if active_model in ("stock.lot", "stock.move.line", "stock.quant"):
            active_ids = self.env.context.get("active_ids", [])
            record_ids = self.env[active_model].browse(active_ids)
            lot_ids = active_model == "stock.lot" and self or record_ids.mapped("lot_id")

            if self.label_quantity == "lots":
                docids = lot_ids.ids

            else:
                quantity_by_lot = defaultdict(int)

                for record in record_ids:
                    if active_model == "stock.lot":
                        quantity_by_lot[record.id] += 1

                    else:
                        if record.product_uom_id.category_id.id == self.env.ref("uom.product_uom_categ_unit", False).id:
                            qty = active_model == "stock.quant" and record.inventory_quantity or record.qty_done
                            quantity_by_lot[record.lot_id.id] += int(qty)

                        else:
                            quantity_by_lot[record.lot_id.id] += 1


                docids = []

                for lot_id, qty in quantity_by_lot.items():
                    docids.extend([lot_id] * qty)

            xml_id = self.print_format == "zpl" and "stock.label_lot_template" or "stock.action_report_lot_label"
            report_action = self.env.ref(xml_id).report_action(docids)
            report_action.update({"close_on_report_download": True})

            return report_action

        return super().process()
