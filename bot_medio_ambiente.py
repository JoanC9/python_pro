import discord
from discord.ext import commands

def operaciones(a, b, operacion):
    
    if operacion == 1:
        return a + b
    elif operacion == 2:
        return a - b
    elif operacion == 3:
        return a * b
    elif operacion == 4:
        
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        else:
            return a / b
    else:
        raise ValueError("Operación no válida")
    

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def enlinea():
    print(f'Bot {bot.user.name} esta listo!')
    
@bot.command()
async def informacion(ctx):
    
    informacion_contaminacion = 'La contanaminacion ambiental se puede controlar con medidas como la reducción de emisiones de gases contaminantes, el uso de energías renovables, la gestión adecuada de residuos y la promoción de prácticas sostenibles en la industria y la agricultura.'
    
    await ctx.send(informacion_contaminacion)
    
@bot.command()
async def calcular(ctx, a: float, b: float, comando: int):
    
    resultado = operaciones(a, b, comando)
    
    await ctx.send(resultado)
    
    

    
token = ''

bot.run(token)