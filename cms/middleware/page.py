# -*- coding: utf-8 -*-
from cms.appresolver import applications_page_check
from django.utils.functional import SimpleLazyObject


def get_page(request):
    from cms.utils.page_resolver import get_page_from_request

    if not hasattr(request, '_current_page_cache'):
        request._current_page_cache = get_page_from_request(request)
        if not request._current_page_cache:
            # if this is in a apphook
            # find the page the apphook is attached to
            request._current_page_cache = applications_page_check(request)
    return request._current_page_cache


class CurrentPageMiddleware(object):
    def process_request(self, request):
        request.current_page = SimpleLazyObject(lambda: get_page(request))
        return None
