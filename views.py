from pyramid.compat import escape

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name="home")
def home_view(request):
    return Response('<p>Visit <a href="/howdy?name=lisa">hello</a></p>')


@view_config(route_name='hello', renderer='hello_world.pt')
def hello_world(request):
    return dict(name=request.matchdict['name'])

@view_config(route_name="redirect")
def redirect_view(response):
    return HTTPFound(location='/problem')

@view_config(route_name="exception")
def exception_view(response):
    raise Exception()
