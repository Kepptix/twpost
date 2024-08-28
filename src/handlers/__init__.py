from .twitch import *
from .settings import *

from aiogram import Router

def register_routers(router: Router):
    router.include_routers(
        twitch.router,
        settings.router,
    )
    return router