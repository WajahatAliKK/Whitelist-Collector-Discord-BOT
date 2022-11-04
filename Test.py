import csv
import json
from avro.codecs import NullCodec
# from avro.datafile import DataFileReader, DataFileWriter
# from avro.io import DatumReader, DatumWriter
#
# # read the Avro file and deserialization
# reader = DataFileReader(open("userdata1.avro", "rb"), DatumReader())
# for employee in reader:
#     print(employee)
# reader.close
#
# # print the Avro schema
# reader = avro.datafile.DataFileReader(open('user.avro', "rb"), avro.io.DatumReader())
# records = [r for r in reader]
# schema = reader.meta
# print(schema)

# import dateutil.parser
# from datetime import datetime
# time_str = ['Tue, 01 Mar 2016 21:17:00 +0800', '2016/03/01 21:17:00', '21:17:00 2016/03/01', '01/03/2016 21:17:00']
# for t in time_str:
#     d = dateutil.parser.parse(t)
#     print(type(d))
#     print(d.strftime('%d/%m/%Y'))
# import pandas as pd
# data = pd.read_csv("Whitelist.csv")
# print(data.shape[0])
# # import csv
# from web3.auto import w3
# from web3 import Web3
#
# w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/75b18ca4eac342e19386ca121d13eda8'))
# print(w3.isConnected())
# wei = w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
# Ether = w3.fromWei(wei, 'ether')
# print(Ether)
# from solana.rpc.api import Client
#
# # http_client = Client("https://api.devnet.solana.com")
# http_client = Client("https://api.mainnet-beta.solana.com")
# print(http_client.is_connected())
# sol = http_client.get_balance("83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri")
# sol = sol['result']['value']
# print(sol*0.000000001)
# from discord.ui import Button, View
# from discord.ext import commands
#
#
#
# TOKEN = ''
#
# client = discord.Client(intents=discord.Intents.default())
#
# # bot = commands.Bot(intents=discord.Intents.default(),command_prefix='..')
#
# # @client.command()
# # async def on_message(ctx):
#
#
# #     button = Button(label='Click me!', style=discord.ButtonStyle.green, emoji='🙂')
# #     view = View()
# #     view.add_item(button)
# #     await ctx.send("Hi!", view=view)
#
# wallet = bin(10)
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
#
#
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content).split('>>>')[1]
#     channel = str(message.channel.name)
#     print(message.content)
#     print(f'{username}: {user_message} ({channel})')
#     print(user_message)
#     print(message)
#     if message.channel.name == 'general':
#       if message.content.startswith(">>>"):
#         if user_message.lower() == 'hello':
#             await message.channel.send(f'Hello {username}!')
#             return
#         elif user_message.lower() == 'bye':
#             await message.channel.send(f'See you later {username}!')
#             return
#
#
# client.run(TOKEN)
# header = ['UserName', 'Wallet_Address', 'User_ID']
# data = [
#     ['Russia', '0x12373789ffh', 123781927382164],
# ]
# with open('Whitelist.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#
#     writer.writerow(header)
#     # write multiple rows
#     # writer.writerow(data)
#
#     f.close()

# def button2_callback():
#     Updated = list()
#     with open('Whitelist.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for line in csv_reader:
#             if line[2] != '0xF276Afa12353F2343532asd1':
#                 Updated.append(line)
#     with open('Whitelist.csv', 'w', encoding='UTF8', newline='') as writer_file:
#         csv_writer = csv.writer(writer_file)
#         csv_writer.writerows(Updated)
#
#         # for line in csv_reader:
#         #     if line[2] == str():
#         #         embed.add_field(name="Wallet Address", value=f"{line[1]}", inline=False)
#         #         await interaction.response.send_message(embeds=[embed])
#
#
# button2_callback()
# import discord
# from discord.ext import commands
#
# client = commands.Bot(command_prefix='.')
#
#
# @client.event
# async def on_ready():
#     print('Bot is ready')
#
#
# @client.command()
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit=amount)
#
#
# client.run('')


# filename = "Whitelist.csv"
# # opening the file with w+ mode truncates the file
# f = open(filename, "w")
# f.truncate()
# f.close()
import pandas as pd

# import csv
# df = pd.read_csv('Whitelist.csv')
# if df.shape[0] != 0:
#     df = df.truncate(df.shape[0])
# print(df)
# with open('Whitelist.csv', 'w', encoding='UTF8') as writer_file:
#     csv_writer = csv.writer(writer_file)
#     csv_writer.writerow(df)
# import os
# if os.stat("9123123193851176.csv").st_size == 0:
# #note: file has to be in same directory as python script#
#   print('empty')
# if not os.path.exists('996682296293851176.csv'):
#     print('empty')
# df = pd.read_csv('968473991155179520.csv')
# if df.shape[0]:
#     print(df.shape)
# import csv
# in_file = open("License.csv", "rb")
# reader = csv.reader(in_file)
# out_file = open("License.csv", "wb")
# writer = csv.writer(out_file)
# for row in reader:
#     row[3] = 4
#     writer.writerow(row)
# in_file.close()
# out_file.close()
# df = pd.read_csv('License.csv')
#
# print(df.shape)
# print(df)
