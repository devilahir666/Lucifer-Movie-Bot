from aiohttp import web

async def health_check(request):
    return web.Response(text="Bot is Running!")

async def server_run():
    app = web.Application()
    app.router.add_get("/", health_check)
    return app
