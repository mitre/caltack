from aiohttp import web


class AttackAPI:
    @staticmethod
    async def landing(request):
        return web.HTTPFound('/attack/index.html')

    @staticmethod
    async def attack_redirector(request):
        return web.HTTPFound('/attack{}'.format(request.rel_url.path))

    @staticmethod
    async def attack_redirector_add_index(request):
        return web.HTTPFound('/attack{}/index.html'.format(request.rel_url.path))
