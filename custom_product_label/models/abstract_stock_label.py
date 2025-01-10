from odoo import models


class AbstractStockLabel(models.Model):
    _name = "abstract.stock.label"
    _description = "Abstract Stock Label"
    
    def action_open_label_layout(self):
        view = self.env.ref("stock.product_label_layout_form_picking", False)
        product_ids = self.filtered("product_id").mapped("product_id")
        move_line_ids = self.env["stock.move.line"].browse()

        if self._name == "stock.move.line":
            move_line_ids |= self

        return {
            "name": "Scegli il layout delle etichette",
            "type": "ir.actions.act_window",
            "res_model": "product.label.layout",
            "views": [(view.id, "form")],
            "target": "new",
            "context": {
                "default_product_ids": product_ids.ids,
                "default_move_line_ids": move_line_ids.ids,
                "default_picking_quantity": "picking"
            }
        }

    def action_print_labels(self):
        lot_ids = self.env["stock.lot"].browse()
        
        if self._name in ("stock.quant", "stock.move.line"):
            lot_ids |= self.filtered("lot_id").mapped("lot_id")
        
        elif self._name == "stock.lot":
            lot_ids |= self
        
        if self.user_has_groups("stock.group_production_lot") and lot_ids:
            view = self.env.ref("stock.picking_label_type_form", False)
            
            return {
                "name": "Scegli il layout delle etichette",
                "type": "ir.actions.act_window",
                "res_model": "picking.label.type",
                "views": [(view.id, "form")],
                "target": "new"
            }

        return self.action_open_label_layout()
