import discord
import os
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def meme(ctx):
    lista = os.listdir('images')
    imagemselecionada = random.choice(lista)
    with open(f'images/{imagemselecionada}','rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)


@bot.command()
async def recycle_suggestion(ctx):
    lista2 = ['Você pode utilizar garrafas pet como vaso de planta', 'Você pode usar mais energia renovável no dia a dia', "Você pode reciclar itens que estão de sobra em casa", "Você pode comprar menos no supermercado para não desperdiçar comida e itens", 'Se tiver filhos, pode ensiná-los o benefício da reciclagem e o uso de energia limpa, além de ter exemplos práticos']
    sugestaoselecionada = random.choice(lista2)
    await ctx.send(sugestaoselecionada)
