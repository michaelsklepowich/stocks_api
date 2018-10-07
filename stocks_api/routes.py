from pyramid_restful.routers import ViewSetRouter
from .views/portfolio.py import StocksAPIView, PortfolioAPIView, CompanyAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('portfolio', '/portfolio')
    router = ViewSetRouter(config)
    router.register('api/v1/stock', StocksAPIView, 'stock')
    router.register('api/v1/company', CompanyAPIView, 'company')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio')