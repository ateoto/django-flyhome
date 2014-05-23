from django.http import HttpResponse
from django.views.generic import View

import json

class default(View):

    def get(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return HttpResponse(json.dumps({ 'ip': ip}), content_type='application/json')