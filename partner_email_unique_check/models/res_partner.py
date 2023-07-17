from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    email = fields.Char(
        index=True,
    )

    @api.constrains('email')
    def _check_unique_email(self):
        for partner in self:
            if partner.email:
                partner_with_same_email = self.search([
                    ('email', '=', partner.email),
                    ('id', '!=', partner.id),
                ], limit=1)
                if partner_with_same_email:
                    raise ValidationError(_("Email must be unique for"
                                          " each partner."))
