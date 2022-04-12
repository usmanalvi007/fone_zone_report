from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    serial_number = fields.Char(compute="get_serial_number",store=False)
    # serial_number = fields.Char()

    def get_serial_number(self):
        for rec in self:
            self.env.cr.execute("""select b.name from product_variant_combination a
            inner join product_attribute_value b on b.id = a.product_template_attribute_value_id
            where a.product_product_id = %s limit 1""" % rec.id)
            serial_number = self.env.cr.fetchone()
            rec.serial_number = serial_number[0] if serial_number else False


    def _update_standard_price(self):
        product = self.env['product.product'].search([])
        for pro in product:
            pro.standard_price = pro.lst_price
