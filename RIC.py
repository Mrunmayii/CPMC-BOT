import discord
from discord.ext import commands
from datetime import datetime
import requests

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


URL_codeforces = "https://kontests.net/api/v1/codeforces"
URL_codechef = "https://kontests.net/api/v1/code_chef"
URL_leetcode = "https://kontests.net/api/v1/leet_code"

# sending get request and saving the response as response object
request_codeforces = requests.get(url=URL_codeforces)
request_codechef = requests.get(url=URL_codechef)
request_leetcode = requests.get(url=URL_leetcode)

# extracting data in json format
data_codeforces = request_codeforces.json()
data_codechef = request_codechef.json()
data_leetcode = request_leetcode.json()



def destructure_codeforces_leetcode(contest):
    date = contest['start_time'].split('T')[0]
    time = contest['start_time'].split('T')[1]
    return [contest['name'], str(date.split('-')[2] + "/" + date.split('-')[1] + "/" + date.split('-')[0] + " at " + str(
        int(time[0:2:1]) + 6) + ":05")]

def destructure_codechef(contest):
    date = contest['start_time'].split(' ')[0]
    time = contest['start_time'].split(' ')[1]
    return [contest['name'], str(date.split('-')[2] + "/" + date.split('-')[1] + "/" + date.split('-')[0] + " at " + str(int(time[0:2:1]) + 6) + ":00")]



display_list = list(map(destructure_codeforces_leetcode, data_codeforces))[0:2:] + list(map(destructure_codechef,data_codechef))[0:2:] + list(map(destructure_codeforces_leetcode, data_leetcode))[0:2:]



def display(display_list):
    dis = '\n**Upcoming Contests:**\n\n'
    i = 1
    for contest in display_list:
        dis = dis + \
              f'{i}) **Name**: {contest[0]}\n \t**Date**: {contest[1]}\n\n'
        i = i + 1
    return dis


@client.command(name='contests')
async def contest(ctx):
    await ctx.reply(display(display_list))


client.run('OTc4NzMxNjAwMzc0Mjg0MzIy.G4ygGK.DUuxYU1R6MpX-4Li6Ms38v6FOk7UlYHN0ouHMg')
