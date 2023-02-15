from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    """
    page_size is the number of contents to watch
    page_size_query_param is the name of the query parameter for the page size
    page_query_param is the name of the query parameter for the current page
    """
    page_size = 7
    page_size_query_param = 'size'
    max_page_size = 100
    last_page_strings = ('end',)


class WatchListLOPagination(LimitOffsetPagination):
    """
    default_limit is the number of items to be returned in the list on default
    max_limit is the maximum number of items to be returned
    """
    default_limit = 5
    max_limit = 100
    limit_query_param = 'limit'
    offset_query_param = 'start'


class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = '-created_at'
