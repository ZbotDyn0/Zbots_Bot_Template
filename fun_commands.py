import discord 
from discord.ext import commands
from asyncio.tasks import sleep
import aiohttp
import random


client = commands.Bot(command_prefix='', help_command=None)

# meme command
async def memecmd():
  @client.command(pass_context=True)
  async def meme(ctx):
    embed = discord.Embed(title="Welcome to r/dankmemes (or r/memes)", description=f"<@{ctx.author.id}>", color = (0x4103fc))
    rng = random.randit(1, 2)
    async with aiohttp.ClientSession() as cs:
      if rng == 1:
        async with cs.get('https://www.reddit.com/r/Memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
      if rng == 2:
        async with cs.get('https://www.reddit.com/r/DankMemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

# pp size command
async def pp_size():
  @client.command(pass_context = True, aliases = ['pp-size'])
  async def pp_size(ctx):
    embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (random.randint(1, 500)), color = (0xFF0000))
    await ctx.send(embed = embed)