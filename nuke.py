
import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user)


@client.event
async def on_message(message):
    if message.content.startswith('!폭파'):
        if message.author.guild_permissions.manage_messages:
            aposition = message.channel.position
            new = await message.channel.clone()
            await message.channel.delete()
            await new.edit(position=aposition)

            embed = discord.Embed(title='채널 폭파됨', colour=discord.Colour.red())
            embed.set_image(url='https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif')
            await new.send(embed=embed)

client.run('★TOKEN★')
