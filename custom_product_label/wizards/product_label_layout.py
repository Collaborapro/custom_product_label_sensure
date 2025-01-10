from odoo import models
from odoo.exceptions import UserError


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    def _prepare_report_data(self):
        active_model = self.env.context.get("active_model", "stock.picking")

        if active_model in ("stock.lot", "stock.move.line", "stock.quant"):
            active_ids = self.env.context.get("active_ids", [])
            record_ids = self.env[active_model].browse(active_ids)

            if self.custom_quantity <= 0:
                raise UserError("Devi inserire una quantità positiva.")

            if self.print_format == "dymo":
                xml_id = "product.report_product_template_label_dymo"

            elif "x" in self.print_format:
                xml_id = "product.report_product_template_label"

            else:
                xml_id = ""

            product_ids = record_ids.filtered("product_id").mapped("product_id")
            data = {
                "active_model": "product.product",
                "quantity_by_product": {p.id: self.custom_quantity for p in product_ids},
                "layout_wizard": self.id,
                "price_included": "xprice" in self.print_format
            }

            return xml_id, data

        xml_id, data = super()._prepare_report_data()
        picking_id = self.move_line_ids and self.move_line_ids[0].picking_id or False

        if picking_id:
            data["receipt_date"] = (picking_id.date_done or picking_id.scheduled_date).strftime("%d/%m/%Y") or "N/A"
            data["receipt_name"] = picking_id.name

        return xml_id, data

