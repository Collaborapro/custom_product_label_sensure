from odoo import models, api

class CustomProductLabel(models.AbstractModel):
    _name = "report.custom_product_label.template"
    _description = "Custom Product Label with Receipt Details"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        labels = []
        for picking in docs:
            for line in picking.move_lines:
                qty = int(line.quantity_done or 1)
                for _ in range(qty):
                    labels.append({
                        'product_name': line.product_id.name,
                        'product_code': line.product_id.default_code or 'N/A',
                        'supplier': picking.partner_id.name or 'N/A',
                        'receipt_date': picking.scheduled_date.strftime('%d/%m/%Y') if picking.scheduled_date else 'N/A',
                        'receipt_name': picking.name,
                    })
        return {
            'docs': docs,
            'labels': labels,
        }
