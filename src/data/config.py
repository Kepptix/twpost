from environs import Env

env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")

APP_ID: str = env.str("APP_ID")
APP_SECRET: str = env.str("APP_SECRET")