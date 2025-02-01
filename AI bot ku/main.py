import discord
from discord.ext import commands
from model import ge_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            file_url = attachments.url
            await attachments.save(f"./{attachments.filename}")
            await ctx.send(ge_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachments.filename}"))
    
    else:
        await ctx.send("kamu belum aploud image :(")
        
bot.run("MTI2NzQ3NTk4NTczODEwNDk2NQ.GaJn4Z.PO8KEtBPJvMCLniwpmuAxCTjSiho-I-VHC-438")