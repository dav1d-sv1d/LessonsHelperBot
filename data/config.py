from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
PORT = env.str("PORT")
host = 'localhost'
