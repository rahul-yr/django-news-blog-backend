
from rest_framework.pagination import CursorPagination


class CursorSetPagination(CursorPagination):
    page_size = 6
    # page_size_query_param = 'page_size'
    ordering = '-id'