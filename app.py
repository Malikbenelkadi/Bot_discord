import discord
from discord.ext import commands, tasks
from datetime import datetime
import random

# Intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Date prévue de l'accouchement
due_date = datetime(2024, 4, 24)

# Citations inspirantes
parenting_quotes = [
    "La parentalité, c'est comme construire un avion en plein vol.",
    "Le meilleur héritage qu'un parent puisse donner à son enfant est un peu de son temps chaque jour.",
    "L'aventure de la parentalité : où chaque jour est une leçon d'humilité."
]


@bot.command()
async def countdown(ctx):
    print(ctx.channel)  # Ajout de la ligne pour afficher le canal

    # Vérifie si la commande est exécutée dans un serveur
    if ctx.guild:
        # Trouver le canal 'general'
        general_channel = discord.utils.get(ctx.guild.channels, name='général')

        today = datetime.now()
        remaining_time = due_date - today

        # Envoyer le message dans le canal 'general'
        if general_channel:
            await general_channel.send(f"Temps restant jusqu'à la naissance : {remaining_time.days} jours!")
        else:
            await ctx.send("Canal 'general' non trouvé.")
    else:
        await ctx.send("Cette commande doit être exécutée dans un serveur.")


# Commande de citation
@bot.command()
async def quote(ctx):
    await ctx.send(random.choice(parenting_quotes))

# Commande du créateur
@bot.command()
async def creator(ctx):
    await ctx.send("Je suis créé par Malik Benelkadi, un jeune passionné de Python qui aime faire des bots.")

# Tâche de mise à jour hebdomadaire
@tasks.loop(hours=168)
async def weekly_update():
    channel_id = 1150591013006622743  # Remplacez YOUR_CHANNEL_ID par l'ID du canal spécifique
    channel = bot.get_channel(channel_id)
    if channel:
        today = datetime.now()
        remaining_time = due_date - today
        await channel.send(f"Mise à jour hebdomadaire: {remaining_time.days} jours restants jusqu'à l'arrivée du bébé!")
    else:
        print(f"Canal avec l'ID {channel_id} non trouvé.")

# Événement de démarrage
@bot.event
async def on_ready():
    print("Bot is ready.")
    weekly_update.start()

# Lance le bot
bot.run('*******************************')
