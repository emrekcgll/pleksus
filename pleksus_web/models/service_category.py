from odoo import models, fields, api

class ServiceCategory(models.Model):
    _name = 'pleksus.service.category'
    _description = 'Pleksus Service Category'
    _order = 'sequence, name'

    name = fields.Char(string='Kategori Adı', required=True)
    sequence = fields.Integer(string='Sıra', default=10)
    active = fields.Boolean(string='Aktif', default=True)
    service_ids = fields.One2many('pleksus.service', 'category_id', string='Hizmetler')

class Service(models.Model):
    _name = 'pleksus.service'
    _description = 'Pleksus Service'
    _order = 'sequence, name'

    name = fields.Char(string='Hizmet Adı', required=True)
    description = fields.Text(string='Açıklama')
    image = fields.Binary(string='Resim')
    image_url = fields.Char(string='Resim URL', compute='_compute_image_url', store=True)
    is_popular = fields.Boolean(string='Popüler Hizmet', default=False)
    sequence = fields.Integer(string='Sıra', default=10)
    active = fields.Boolean(string='Aktif', default=True)
    category_id = fields.Many2one('pleksus.service.category', string='Kategori', required=True)
    
    @api.depends('image')
    def _compute_image_url(self):
        for record in self:
            if record.image:
                record.image_url = f'/web/image/pleksus.service/{record.id}/image'
            else:
                record.image_url = '/pleksus_web/static/src/images/200x130.png'
