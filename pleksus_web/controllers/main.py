# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class PleksusWebController(http.Controller):
    
    @http.route('/', type='http', auth='public', website=True)
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
        
        return request.render('pleksus_web.pleksus_homepage', {
            'categories': categories
        })


    @http.route('/application', type='http', auth='public', website=True)
    def application(self, **kwargs):
        """Sağlıkçı başvuru sayfası"""
        return request.render('pleksus_web.pleksus_application')


    @http.route('/service-request', type='http', auth='public', website=True)
    def service_request_form(self, **kwargs):
        """Hasta hizmet talep formu"""
        return request.render('pleksus_web.pleksus_service_request')
    
    @http.route('/service/request', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def service_request_submit(self, **kwargs):
        """Hizmet talep formu işleme"""
        try:
            # Form verilerini al
            city = kwargs.get('city', '')
            district = kwargs.get('district', '')
            service_date = kwargs.get('service_date', '')
            service_time = kwargs.get('service_time', '')
            person_count = kwargs.get('person_count', '')
            
            # Basit validasyon
            if not all([city, district, service_date, service_time, person_count]):
                return request.render('pleksus_web.pleksus_service_request', {
                    'error': 'Lütfen tüm gerekli alanları doldurun.'
                })
            
            # Burada hizmet talep kaydı oluşturulabilir
            # request_vals = {
            #     'city': city,
            #     'district': district,
            #     'service_date': service_date,
            #     'service_time': service_time,
            #     'person_count': person_count,
            #     'state': 'draft',
            # }
            # service_request = request.env['pleksus.service.request'].sudo().create(request_vals)
            
            return request.render('pleksus_web.pleksus_service_request', {
                'success': 'Hizmet talebiniz başarıyla alındı!'
            })
            
        except Exception as e:
            return request.render('pleksus_web.pleksus_service_request', {
                'error': 'Bir hata oluştu. Lütfen tekrar deneyin.'
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
    

