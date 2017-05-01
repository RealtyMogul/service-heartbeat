from .views import heartbeat_view


def includeme(config):
    config.add_view(heartbeat_view, route_name='heartbeat_view', renderer='json')
    config.add_route('heartbeat_view', '/heartbeat')
