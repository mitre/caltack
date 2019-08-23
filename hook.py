from plugins.caltack.app.attack_api import AttackAPI


name = 'ATT&CK'
description = 'Plugin that serves the ATT&CK website alongside CALDERA.'
address = '/plugin/caltack/gui'


async def initialize(app, services):
    plugin_dir = 'plugins/caltack'
    api = AttackAPI()
    app.router.add_static('/attack', plugin_dir + '/static/attack-website', append_version=True)
    app.router.add_route('GET', address, api.landing)
    app.router.add_route('GET', '/theme' + '{loc:.*}', api.attack_redirector)
    app.router.add_route('GET', '/techniques' + '{loc:.*}', api.attack_redirector_add_index)
    app.router.add_route('GET', '/tactics' + '{loc:.*}', api.attack_redirector_add_index)
    app.router.add_route('GET', '/groups' + '{loc:.*}', api.attack_redirector_add_index)
    app.router.add_route('GET', '/software' + '{loc:.*}', api.attack_redirector_add_index)
    app.router.add_route('GET', '/resources' + '{loc:.*}', api.attack_redirector_add_index)
    app.router.add_route('GET', '/matrices' + '{loc:.*}', api.attack_redirector_add_index)
