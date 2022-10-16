import discord
import brawlstars as bs

client = bs.Client("token")

intents = discord.Intents().default()
bot = discord.ext.commands.Bot(intents = intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name = "profile", description = "Fetches a Brawl Stars player's profile.")
async def profile(interaction, tag: str):
    player = client.get_player(tag)
    embed = discord.Embed(
        title = f"{player.name} ({player.tag})",
        description = f"Trophies: 🏆 {player.trophies}\nTeam Victories: {player.team_victories}\nDuo Victories: {player.duo_victories}\nSolo Victories: {player.solo_victories}",
        color = player.name_color
        )
    embed.set_thumbnail(url = f"https://cdn.brawlify.com/profile/{player.icon.id}.png")
    await interaction.response.send_message(embed = embed)
