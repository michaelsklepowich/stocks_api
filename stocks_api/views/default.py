from pyramid.response import Response
from pyramid.view import view_config



@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """home route of the application
    """
    message = 'Hello World'
    return Response(body=message, status=200)

@view_config(route_name='portfolio', renderer='json', request_method='GET')
def portfolio_view(request):
    """portfolio route for application
    """
    message = 'portfolio'
    return Response(body=message, status=200)