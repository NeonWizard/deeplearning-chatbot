import discord
import logging
import time
import os

import config

class MyClient(discord.Client):
    async def on_ready(self):
        # -- logging
        timestamp = time.strftime("%Y_%m_%d-%I_%M_%S_%p")

        os.makedirs('logs/', exist_ok=True)
        handler = logging.FileHandler(filename='logs/{}.log'.format(timestamp), encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

        self.logger = logging.getLogger('discord')
        # self.logger.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        logonText = 'Logged on as {0}!'.format(self.user)
        self.logger.info("App started!.")
        self.logger.info(logonText)
        print(logonText)

    async def on_message(self, message):
        if message.author == client.user:
            return
        if str(message.channel.id) != config.CHANNEL_ID:
            return

        message = 'Message from {0.author}: {0.content}'.format(message)
        self.self.logger.info(message)
        print(message)

        if message.content.startswith('hi skromp'):
            await message.channel.send('hi {0.author}'.format(message))


client = MyClient()
client.run(config.TOKEN)