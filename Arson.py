
import discord
from discord.ext import commands
import asyncio
import os



class myBot(commands.Bot):

    def __init__(self):
        super().__init__(
        command_prefix =commands.when_mentioned_or('Arson'),case_insensitive=True,activity = discord.Streaming(name='@Arson info', url='https://www.twitch.tv/your_channel_here'),
            intents=discord.Intents.all(),
            application_id = 965765799182733312)

   # async def startup(self):
      #  await bot.wait_until_ready()
       # await bot.tree.sync()  # If you want to define specific guilds, pass a discord object with id (Currently, this is global)
       # print('Sucessfully synced applications commands')
        #print(f'Connected as {bot.user}')

    
    
  
    

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded {filename}")
                except Exception as e:
                    print(f"Failed to load {filename}")
                    print(f"[ERROR] {e}")

           # await bot.tree.sync()
           # self.loop.create_task(self.startup())
        

           

        
 
    async def on_ready(self):
       print(f'{self.user} has connected to discord!')


bot = myBot()
async def main():
    async with bot:
        await bot.start(os.environ["Bot_token"])

asyncio.run(main())


        
