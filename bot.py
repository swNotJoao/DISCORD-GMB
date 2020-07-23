# bot.py
import os
import discord
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import asyncio
#from dotenv import load_dotenv

TOKEN = "your token here"

notas = ""
url = "https://fenix.tecnico.ulisboa.pt/disciplinas/ACED251113264/2019-2020/2-semestre/anuncios"
#url = "http://web.tecnico.ulisboa.pt/ist190732/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
notas = str(soup)
print("NOTAS SET TO:", notas)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def checkGrade():
    while(1):
        print("checking")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        if str(soup) == notas:
            #print("NOTAS:", notas)
            print("Nothin new found")
        else:
            await client.wait_until_ready()
            channel = client.get_channel(721397679472771185)
            #await channel.send("do mais um teste")
            await channel.send("@everyone\nDetetei uma mudanca na pagina dos anuncios de ACED\nPossivelmente as notas sairam\n\n\nYEET\n\nVER NOTAS:\nhttps://fenix.tecnico.ulisboa.pt/disciplinas/ACED251113264/2019-2020/2-semestre/notas-das-avaliacoes-b2b")
            await exit(0)
        await asyncio.sleep(60*5)
        #await asyncio.sleep(15)
client.loop.create_task(checkGrade())
client.run(TOKEN)
