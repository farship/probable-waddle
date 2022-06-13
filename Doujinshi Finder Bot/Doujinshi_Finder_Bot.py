import doujinshi_filter as df
import discord_youtubedl as ydl

import random
import time
import datetime
import discord
from discord.ext import commands

bot_token = ''
client = commands.Bot(command_prefix="d. ")
server_id = client.get_guild(bot_token)
propaganda = ""

@client.event
async def on_ready():
    print("Online!")

def adminCheck(ctx):
    adminIDs = [448199717810339861, 368098621930864652]
    if ctx.author.id in adminIDs:
        return True

client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.check(adminCheck)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

# @client.command()
# @commands.check(adminCheck)
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await ctx.send(member.display_name + " has been deemed as undersirable. Gulag_Population++;")
#     await member.ban(reason=reason, delete_message_days=0)

# @client.command()
# @commands.check(adminCheck)
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split('#')
#     for ban_entry in banned_users:
#         user = ban_entry.user
#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'{user.mention} has been deemed desireable.')
#             return


@client.event
async def on_message(message):
    global tags
    print(str(message.author) + ": " + (message.content))
    if ("d! hello") in (message.content):
        await message.channel.send("Hi!")

    if ("d! random") in (message.content):
        df.tries = 0
        tags = []
        df.find_random()
        if df.tries >= 30:
            await message.channel.send("Sorry, but I couldn't find that after " + str(df.tries) + " tries.")
        else:
            await message.channel.send("Here you go: " + df.random_link)

    if ("d! lots ") in (message.content):
        number_lots = message.content.split("d! lots ")[-1]
        if (int(number_lots) <= 10):
            for n in range (0, int(number_lots)):
                df.tries = 0
                tags = []
                df.find_random()
                if df.tries >= 30:
                    await message.channel.send("Sorry, but I couldn't find that after " + str(df.tries) + " tries.")
                else:
                    await message.channel.send("Here you go: " + df.random_link)

    if ("d! tag ") in (message.content):
        tag_split = message.content.split("d! tag ")[1]
        tags = tag_split.split()
        df.tries = 0
        df.find_random()
        if df.tries >= 24:
            await message.channel.send("Sorry, but I couldn't find that after " + str(df.tries) + " tries.")
        else:
            await message.channel.send("Here you go: " + df.random_link)
    if ("d! wholesome") in (message.content):
        df.find_wholesome()
        await message.channel.send("Here you go: " + df.splitafter)

    if ("d!i ") in (message.content):
        image_list = ["horny", "grek", "grk", "no", "padura", "suns", "women bad", "pools closed", "nay", "maggie", "boris", "tim", "him", "cringe"]
        image = message.content.split("d!i ")[-1]
        if image in image_list:
            image_file = (str(image) + ".png")
            await message.channel.send(file=discord.File("C:/Users/Peter/Downloads/stuff/botimages/"+image_file))
        else:
            #not_image_message = []
            await message.channel.send("wtf are you talking about? I only have these: " + str(image_list))

    

#   ----------RESTRICTED COMMANDS----------    #
    valid_users = ["Nyrrha Pikos#3583", "peterhendryalt#5657"]
    uwu_lines = ["*nuzzles you bulgie wulgie*", "hewwo Senpai...", "Nyah!", "OwO"]


    if str(message.author) in valid_users:
        if ("d! uwu") in (message.content):
            await message.channel.send(random.choice(uwu_lines))

        if ("d! tadaima") in (message.content):
            await message.channel.send("Okaerinasai, anata!")
            time.sleep(0.3)
            await message.channel.send("Gohan wo taberu?")
            time.sleep(0.3)
            await message.channel.send("Ofuro ni suru?")
            time.sleep(0.3)
            await message.channel.send("Soretomo, wa. ta. shi?")
        
        if ("d! input") in (message.content):
            if str(message.channel) == 'bot-command-centre':
                msg = message.content
                textToSend = msg.replace('d! input', '')
                channel = client.get_channel(623184025602883646)#heil=623184025602883646    spams=623595427123429392
                await channel.send(textToSend)
            else:
                msg = message.content
                await message.delete()
                textToSend = msg.replace('d! input', '')
                await message.channel.send(textToSend)    
#youtube dl
        if ("d! md") in (message.content):
            download_split = message.content.split("d! md ")[1]
            ydl.discord_default_music(download_split)
            await message.channel.send(file=discord.File("/home/peter/Documents/Code/Doujinshi Finder Bot/tempfiles/1.mp3"))
#spam command
        if ("d! delSpam ") in (message.content): # d! deletePropaganda limit: 100 msg: I <3 VALO # deletes messages with "I <3 VALO" in the last 100 messages in the channel
            historyLimit = int((message.content.split("limit: ")[1]).split(" msg:")[0])
            if historyLimit > 100:
                historyLimit = 100
            propaganda = message.content.split("msg: ")[1]
            scanned_messages = await message.channel.history(limit=historyLimit).flatten()
            await message.delete()
            for text in scanned_messages:
                if propaganda in text.content:
                    # print(text)
                    f = open("deleted.txt", "a")
                    f.write("\%BOT SPAM DELETED\%")
                    f.close()
                    print(text.content)# + " //// " + text.message_id)
                    #await client.http.delete_message(text.channel_id, text.message_id)
                    #await text.channel.purge(limit=historyLimit, check= (propaganda in text.content)
                    # await text.id.delete()
                    await text.delete()
                    #msg = await text.channel.fetch_message(text.id)
                    #await msg.delete()

    #BANNED
    bannedWords = []
    bFR = open("bannedStrings.txt","r")
    bFA = open("bannedStrings.txt","a")
    fileBanned = bFR.read()
    bFR.close()
    for strings in fileBanned:
        bannedWords.append(strings)
    if "d! updateFilter " in message.content:
        addedBannedString = message.content.split("d! updateFilter ", 2)[1]
        bFA.write(addedBannedString)
        bFA.close()
        fileBanned = bFR.readlines()#bFR.read()
        bFR.close()
        for lines in fileBanned:
            bannedWords.append(lines)
    for bW in bannedWords:
        if bW in str(message.content):
            await message.delete()
            break
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    print (str(message.author) + ": " + str(message.content) + " -----DELETED")
    if "d! " in str(message.content) or "cube!" in str(message.content):
        pass
    elif str(message.content) == "":
            pass
    else:
        DaT = datetime.datetime.now()
        f = open("deleted.txt", "a")
        f.write(DaT.strftime("%x") + " " + DaT.strftime("%X") + " " + str(message.author) + ": " + str(message.content) + "\n")
        f.close()

def spamMessageChecker(m):
    return propaganda in m.content

def join():
    client.run(bot_token)
