import aiogram 
from aiogram import Bot, Dispatcher, executor, types, asyncio

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)


# /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет. Для ознакомления с ботом напиши или нажмни на /help")

# /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Я бот крипочка под ником whyzxchurka. Тут есть вся информация о нем. Нажми или напиши /commands")

# /commands
@dp.message_handler(commands=['commands'])
async def commands(message: types.Message):
    await message.reply("Список комманд: \n"
                        "/help - помощь по боту \n"
                        "/info - информация о крипочке \n"
                        "/link - важные ссылки \n"
                        "/support - жалобы и проблемы по боту")

# /info
@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.reply("Имя я тебе не скажу, надо будет крип сам скажет. Возраст тоже не скажу так же сам скажет если надо будет \n"
                        "Ну типо это хуй который пишет таких легких ботов для экспы в голове и все. Так же думает как бы не умереть (ну или умереть О__о)")

# /link
@dp.message_handler(commands=['link'])
async def link(message: types.Message):
    await message.reply(" VK: vk.com/whyzxchurka \n"
                        "TG: t.me/whyzxchurka \n"
                        "TikTok: clck.ru/34LVyW (этА не скам, сократил ссылку тк длинная пиздец) \n"
                        "Twitch: twitch.tv/wtffinka \n"
                        "Steam: clck.ru/34LWEL (Тоже сократил, длинная пиздец) \n"
                        "Discord clck.ru/34LW6T (Да да тоже сократил)")

# /support
@dp.message_handler(commands=['support'])
async def support(message: types.Message):
    await message.reply("По всем жалобам в боте писать @whyzxchurka (не спамьте а то хуй отвечу О__о)")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling())

