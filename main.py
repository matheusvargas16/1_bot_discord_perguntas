import discord
from discord.ext import commands
from discord import app_commands
import random
import requests

bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())
token = 'seu token'

@bot.event
async def on_ready():
    print('Bot está online.')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)    
    
@bot.tree.command(name="vargaspergunta", description="Pergunte ao vargas e receba uma resposta.",)
@app_commands.describe(thing_to_say = "Faça sua Pergunta")
async def vargas(interaction: discord.Interaction, thing_to_say: str):
    respostas = [
        "É certo.",
        "Sem dúvida.",
        "Definitivamente sim.",
        "Você pode contar com isso.",
        "Como eu vejo, sim.",
        "Provavelmente.",
        "Parece bom.",
        "Sim.",
        "Todos os sinais apontam para sim.",
        "Melhor não te dizer agora.",
        "Não é possível prever agora.",
        "Não conte com isso.",
        "Minha resposta é não.",
        "Minhas fontes dizem não.",
        "Não é tão bom.",
        "Não.",
        "Muito duvidoso."
    ]
    resposta = random.choice(respostas)
    await interaction.response.send_message(f"{interaction.user.mention} perguntou: {thing_to_say}\n \n{resposta}")

@bot.tree.command(name="vargasescolha", description="O vargas escolhe entre duas opções.")
@app_commands.describe(opcao1= "Primeira opção", opcao2 = "Segunda opção")
async def escolher(interaction: discord.Interaction, opcao1: str, opcao2: str):
    opcoes = [opcao1, opcao2]
    escolha = random.choice(opcoes)
    await interaction.response.send_message(f"entre {opcao1} e {opcao2}, escolho {escolha}")

bot.run(token)
