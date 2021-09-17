
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!폭파'):
        if message.author.guild_permissions.ban_members:
            aposition = message.channel.position
            new = await message.channel.clone()
            await message.channel.delete()
            await new.edit(position=aposition)

            embed = discord.Embed(title='채널 폭파됨', colour=discord.Colour.red())
            embed.set_image(url='https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif')
            await new.send(embed=embed)
        else:
            await message.channel.send('``명령어 사용권한이 없습니다.``')

client.run('★TOKEN★')
