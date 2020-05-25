from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_route('calculator', '/calculator')
    config.add_route('add', '/calculator/add')
    config.add_route('evaluate', '/calculator/evaluate')
    config.scan('.views')
    return config.make_wsgi_app()
