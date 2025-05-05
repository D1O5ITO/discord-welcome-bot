import discord
from discord import File
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')

@client.event
async def on_member_join(member):
    canal_bienvenida = discord.utils.get(member.guild.text_channels, name='bienvenida')
    if canal_bienvenida:
        archivo_imagen = File("img.png", filename="img.png")
        await canal_bienvenida.send(
            content=f"👋 ¡Bienvenido {member.mention} al servidor! Pásala bien 🍻",
            file=archivo_imagen
        )
    else:
        print("⚠️ No se encontró un canal llamado 'bienvenida'.")

# Token sacado de variable de entorno
client.run(os.getenv("TOKEN"))




