from database.core import DataBase
from aiogram import Bot, Dispatcher
from data.config import settings

db = DataBase()
dp = Dispatcher()
bot = Bot(settings.BOT_TOKEN.get_secret_value())