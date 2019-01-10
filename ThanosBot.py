import random
import math
import discord
import asyncio
from discord.ext import commands
from itertools import cycle

file = open("Bot Token", "r")
TOKEN = file.read()
file.close()
QUOTES = ["Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.",
              "When I’m done, half of humanity will still exist. Perfectly balanced, as all things should be. I hope they remember you.",
              "You’re strong. But I could snap my fingers, and you’d all cease to exist.", "The end is near.",
              "Stark… you have my respect. I hope the people of Earth will remember you.", "You should have gone for the head.",
              "I know what it’s like to lose. To feel so desperately that you’re right, yet to fail nonetheless. Dread it. Run from it. Destiny still arrives. Or should I say, I have.",
              "You’re a great fighter, Gamora. Come. Let me help you.", "You should choose your words wisely",
              "Going to bed hungry. Scrounging for scraps. Your planet was on the brink of collapse. I was the one who stopped that. " +
              "You know what’s happened since then? The children born have known nothing but full bellies and clear skies. It’s a paradise.",
              "I’m the only one who knows that. At least I’m the only who has the will to act on it. For a time, you had that same will. As you fought by my side, daughter.",
              "I ignored my destiny once, I can not do that again. Even for you. I’m sorry Little one.",
              "With all six stones, I can simply snap my fingers, they would all cease to exist. I call that mercy.",
              "Thanos: “Daughter.”\nGamora: “Did you do it ?”\nThanos: “Yes.”\nGamora: “What did it cost?”\nThanos: “Everything.”",
              "Your optimism is misplaced, Asgardian.", "The hardest choices require the strongest wills.",
              "You’re strong. Me… You’re generous. Me… But I never taught you to lie. That’s why you’re so bad at it. Where is the Soul Stone?",
              "The Tesseract… or your brother’s head. I assume you have a preference?"]
STATUS = ["Obtaining The Infinity Gauntlet", "Taking Over Xandar", "Obtaining The Power Stone", "Capturing The Asgardians",
              "Obtaining The Space Stone", "Sending The Black Order To Earth", "Destroying Knowhere", "Obtaining The Reality Stone",
              "Talking To Gamora", "Arriving At Vormir", "Sacrificing Gamora", "Obtaining The Soul Stone", "Arriving At Titan",
              "Battling The Avengers", "Obtaining The Time Stone", "Arriving At Earth", "Reversing Time", "Obtaining The Mind Stone",
              "Stopped By Thor", "Snapping", "Balancing The Universe", "Watching The Sun Set On A Grateful Universe",
              "Watching The Sun Set On A Grateful Universe", "Watching The Sun Set On A Grateful Universe"]
PHIL = ["My Inspiration!", "My Mentor.", "Sensei Swift ._.", "A Worthy Rival.", "My Second In Command"]
catching = None
client = commands.Bot(command_prefix = "=")
client.remove_command("help")

async def change_status():
    await client.wait_until_ready()
    message = cycle(STATUS)
    while not client.is_closed:
        current_status = next(message)
        await asyncio.sleep(60)
        await client.change_presence(game=discord.Game(name=current_status))

@client.event
async def on_ready():
    await client.change_presence(game = discord.Game(name = "Balancing The Universe"))
    print("Thanos Bot Is Ready")

@client.event
async def on_message(message):
    global catching
    author = message.author
    content = message.content
    channel = message.channel
    print("{} said '{}' in the {} channel".format(author, content, channel))
    text = ""
    for i in content.lower():
        if i != " " and i != "\n":
            text += i
    balance = text.find("perfectlybalanced")
    phil = text.find("phil")
    swift = text.find("swift")
    fun = text.find("fun")
    thanos = text.find("thanos")
    gnome = text.find("gnome")
    catch = text.find("<:tha:470422784137232384>")
    if catching != None and catching == channel:
        await client.send_message(catching, "<:NOS:470422818262220800>")
        catching = None
        asyncio.sleep(1)
    if str(author) != "Thanos Bot#5469":
        if balance != -1:
            await client.send_message(channel, "As all things should be.")
        if phil != -1 or swift != -1:
            await client.send_message(channel, random.choice(PHIL))
        elif fun != -1:
            await client.send_message(channel, "Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.")
        elif thanos != -1:
            await client.send_message(channel, "<:Thanos:469571615370248213> <:Thanos:469571615370248213> <:Thanos:469571615370248213>")
        elif gnome != -1:
            await client.send_message(channel, "<:Gnome:501183728622764042> <:Gnome:501183728622764042> <:Gnome:501183728622764042>")
        elif catch != -1:
            catching = channel
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    print("The message '{}' from {} was deleted in the {} channel".format(content, author, channel))

@client.event
async def on_member_join(member):
    name = "Waluigi"
    role = discord.utils.get(member.server.roles, name)
    await client.add_roles(member, role)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    print("{} has added a(n) {} emote to the message '{}' by {}".format(user.name, reaction.emoji, reaction.message.content, reaction.message.author))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    print("{} has deleted a(n) {} emote from the message '{}' by {}".format(user.name, reaction.emoji, reaction.message.content, reaction.message.author))

@client.command()
async def quote(args = 0):
    if args != 0:
        await client.say(QUOTES[(int(args) - 1) % 18])
    else:
        await client.say(random.choice(QUOTES))

@client.command(pass_context = True)
async def logout(ctx):
    author = ctx.message.author
    if str(author) == "Flaming87#6416":
        await client.say("Logout Successful")
        await client.logout()
    else:
        await client.say("Logout failed. You do not have access to this command. If there is a problem with this bot please contact <@413712168022835201>")

@client.command()
async def test():
    embed = discord.Embed(
        title = "Title",
        description = "Description",
        color = discord.Color.dark_purple()
    )

    embed.set_footer(text = "Footer")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/428036558726365184/504759456651804673/image0.png")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/428036558726365184/504759456651804673/image0.png")
    embed.set_author(name = "Name")
    icon_url = "https://cdn.discordapp.com/attachments/428036558726365184/504759456651804673/image0.png"
    embed.add_field(name = "Name", value = "Value", inline = False)
    embed.add_field(name = "Name", value = "Value", inline = True)
    embed.add_field(name = "Name", value = "Value", inline = True)

    await client.say(embed = embed)

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    channel = ctx.message.channel

    embed = discord.Embed(
        color=discord.Color.dark_purple()
    )

    embed.set_author(name="Help")
    embed.add_field(name="=quote",
                    value="Generates a random quote from thanos. Add a number after the command to specify the quote",
                    inline=False)
    embed.add_field(name="=logout",
                    value="Logs out Thanos Bot, but can only be used by the owner",
                    inline=False)
    embed.add_field(name="=help",
                    value="A list of commands for Thanos Bot",
                    inline=False)

    await client.send_message(channel, "Check your DM for a list of commands")
    await client.send_message(author, embed = embed)

client.loop.create_task(change_status())
client.run(TOKEN)
