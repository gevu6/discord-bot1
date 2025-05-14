import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive  # імпорт Flask-сервера

# Запускаємо вебсервер для 24/7
keep_alive()

# Завантаження .env змінних
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

TARGET_CHANNEL_ID = 1370494607661727794  # Замінити на ID твого каналу

@bot.event
async def on_ready():
    print(f"✅ Бот запущено як {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id != TARGET_CHANNEL_ID or message.author.bot:
        return

    if message.attachments:
        try:
            await message.add_reaction("<:win:1370773118767075531>")
            await message.add_reaction("<:lose:1370737479090700408>")
            await message.add_reaction("<:kakashka:1370736094638772234>")
        except Exception as e:
            print(f"❌ Помилка при додаванні реакцій: {e}")

    await bot.process_commands(message)

# Запуск бота
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN не знайдено в .env файлі!")

bot.run(TOKEN)
