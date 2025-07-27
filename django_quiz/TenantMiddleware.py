
from urllib.parse import urlparse
from django.http import HttpRequest
from quizapp.models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request:HttpRequest):
        
        sub_domain=urlparse(request.META.get('HTTP_REFERER')).hostname.split('.')[0]
        tenant=Tenant.objects.get_or_create(schema_name=sub_domain)
        setattr(request,"tenant",tenant)
        response=self.get_response(request)

        

        return response
    

    