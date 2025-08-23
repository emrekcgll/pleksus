# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class PleksusWebController(http.Controller):
    
    @http.route(['/', '/home'], type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        """Ana sayfa route'u"""
        categories = request.env['pleksus.service.category'].sudo().search([
            ('active', '=', True)
        ], order='sequence, name')
        
        # Her kategori için hizmetleri de getir
        for category in categories:
            category.service_ids = request.env['pleksus.service'].sudo().search([
                ('category_id', '=', category.id),
                ('active', '=', True)
            ], order='sequence, name')
        
        return request.render('pleksus_web.homepage', {
            'categories': categories
        })
    
    @http.route('/contact', type='http', auth='public', website=True, methods=['POST'])
    def contact_form(self, **kwargs):
        """İletişim formu işleme"""
        try:
            # Form verilerini al
            name = kwargs.get('name', '')
            email = kwargs.get('email', '')
            company = kwargs.get('company', '')
            message = kwargs.get('message', '')
            
            # Basit validasyon
            if not name or not email or not message:
                return {'success': False, 'message': 'Lütfen tüm gerekli alanları doldurun.'}
            
            # Burada e-posta gönderme veya veritabanına kaydetme işlemleri yapılabilir
            # Örnek: mail gönderme
            # self._send_contact_email(name, email, company, message)
            
            return {'success': True, 'message': 'Mesajınız başarıyla gönderildi!'}
            
        except Exception as e:
            return {'success': False, 'message': 'Bir hata oluştu. Lütfen tekrar deneyin.'}
    
    def _send_contact_email(self, name, email, company, message):
        """İletişim formu e-postası gönderme (opsiyonel)"""
        # Bu fonksiyon e-posta gönderme işlemi için kullanılabilir
        pass
    

