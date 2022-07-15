import discord
import os
import pandas as pd
import csv
from solana.rpc.api import Client
from discord.ui import Button, View, Modal, InputText
import Modal_test
from discord.ext import commands
from web3 import Web3
from discord.commands import Option

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/75b18ca4eac342e19386ca121d13eda8'))
# TOKEN = 'OTczOTIxNjE5ODI1Mjc5MDE3.GRWJzL.eOvClJNIu7WiBjD2ALpbD3oMNwlytCdjAIF9SI'
TOKEN = 'OTY4NDY3OTkwNTQwNTk1MjMw.GEbbW0.rryf7tQC7OCD6t_WH6LECBob7OU23LiV57_MIQ'
http_client = Client("https://api.mainnet-beta.solana.com")
sol = http_client.get_balance("83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri")
sol = sol['result']['value']
print(sol * 0.000000001)
# DTOKEN = 'Z4-JXA6cFJpjFS0EFp4BQSnmoEa_HuqY'
bot = commands.Bot(
    command_prefix='>>>',
    intents=discord.Intents(messages=True, guilds=True)
)


@commands.has_permissions(administrator=True)
@bot.slash_command(
    name="reset-wallet-count",
    description="Erases all data of successfully submitted wallets. BE VERY CAREFUL WHEN USING THIS COMMAND",
    guild_ids=[968473991155179520, 996682296293851176,997393143081226251]
)
async def _clearCount(ctx):
    if Modal_test.licenseKey:
        df = pd.read_csv("Whitelist.csv")
        if df.shape[0] == 0:
            embed = discord.Embed(
                title=f"Total number of submitted wallets is `{df.shape[0]}`",
                color=discord.Color.blurple())
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            df = df.truncate(df.shape[0])
            with open('Whitelist.csv', 'w', encoding='UTF8') as writer_file:
                csv_writer = csv.writer(writer_file)
                csv_writer.writerow(df)
            embed = discord.Embed(
                title="Reset successful!",
                color=discord.Color.blurple())
            embed.add_field(name="✅ Wallet count has been successfully reset to `0` and all data has been erased.",
                            value="Use the command `/start` to initialize the bot using a different configuration, if any",
                            inline=False)
            await ctx.respond(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title=f"ERROR ❌ ",
                              color=discord.Color.red())
        embed.add_field(name="Initiate the bot", value="Buy the license or initiate the license and variables (if you "
                                                       "already have one) using the `/start` command", inline=False)
        await ctx.respond(embed=embed, ephemeral=True)


@commands.has_permissions(administrator=True)
@bot.slash_command(
    name="wallet-count",
    description="To check how many wallets have been submitted",
    guild_ids=[968473991155179520, 996682296293851176, 997393143081226251]
)
async def _count(ctx):
    data = pd.read_csv("Whitelist.csv")
    embed = discord.Embed(
        title=f"Total number of successfully submitted wallets is `{data.shape[0]}`",
        color=discord.Color.blurple())
    await ctx.respond(embed=embed, ephemeral=True)


@commands.has_permissions(administrator=True)
@bot.slash_command(
    name="check-settings",
    description="To check present configurations of the bot",
    guild_ids=[968473991155179520, 996682296293851176, 997393143081226251]
)
async def _check(ctx):
    if Modal_test.currency:
        embed = discord.Embed(title=f"This project's currency is set to `{Modal_test.currency}` and the minimum "
                                    f"wallet balance required to qualify for submission is `{Modal_test.minimun_balance}`.",
                              color=discord.Color.blurple())
        await ctx.respond(
            embed=embed,
            ephemeral=True)
    else:
        embed = discord.Embed(
            title="ERROR ❌",
            color=discord.Color.red())
        embed.add_field(name='Initiate the bot', value='Buy the license or initiate the license and variables (if you '
                                                       'already have one) using the `/start` command', inline=False)
        await ctx.respond(
            embed=embed, ephemeral=True)


@commands.has_permissions(administrator=True)
@bot.slash_command(
    name='start',
    description='To initialize the bot by configuring currency/blockchain and preferred wallet balance',
    guild_ids=[968473991155179520, 996682296293851176, 997393143081226251]
)
async def _start(ctx, license_key: Option(str, "Provide license key to activate bot", required=True),
                 currency: Option(str, "Choose if this project is on ETH or SOL", required=True),
                 wallet_balance: Option(float, "Key in the minimum wallet balance to be eligible for Whistelist",
                                        required=True)):
    if license_key == 'blac|<white':
        Modal_test.licenseKey = True
        Modal_test.currency = currency
        Modal_test.minimun_balance = wallet_balance
        embed = discord.Embed(
            title=f"Well done! 🎉",
            color=discord.Color.green())
        embed.add_field(name='Your bot has been successfully set up!',
                        value=f'✅ Your selected currency is `{Modal_test.currency}`.\n✅ You have keyed in `{Modal_test.minimun_balance}` as the minimum wallet balance to be eligible for Whitelist.\n\nUse the command `/send-panel` to invoke the bot on the channel.')
        await ctx.respond(embeds=[embed],
                          ephemeral=True)
    else:
        embed = discord.Embed(
            title=f"ERROR ❌",
            color=discord.Color.red())
        embed.add_field(name='You have entered an invalid license key!',
                        value=f'Please key in a valid license key or contact the developer for support')
        await ctx.respond(embeds=[embed],
                          ephemeral=True)


@commands.has_permissions(administrator=True)
@bot.slash_command(
    name='send-panel',
    description='To send the wallet submission panel on the channel',
    guild_ids=[968473991155179520, 996682296293851176, 997393143081226251]
)
async def _heybottie(ctx):
    if ctx.author == bot.user:
        return
    if Modal_test.licenseKey:
        print(ctx.guild.id)
        for guild in bot.guilds:
            if guild.id == ctx.guild.id:
                for channel in guild.text_channels:  # getting only text channels
                    if channel.permissions_for(guild.me).send_messages:  # checking if you have permissions
                        # username = str(message.author).split('#')[0]
                        # Modal_test.user_name = username
                        # Modal_test.User_ID = message.author.id
                        # print(message)
                        button = Button(label='Add', style=discord.ButtonStyle.green, emoji='✅')
                        button2 = Button(label='Check', style=discord.ButtonStyle.gray, emoji='☑')
                        button3 = Button(label='Delete', style=discord.ButtonStyle.danger, emoji='✖')
                        view = View(timeout=None)
                        view.add_item(button)
                        view.add_item(button2)
                        view.add_item(button3)
                        fname = str(guild.id) + '.csv'

                        async def button3_callback(interaction):
                            print(fname)
                            df = pd.read_csv(fname)
                            Updated = list()
                            Modal_test.User_ID = interaction.user.id
                            user = await bot.fetch_user(interaction.user.id)
                            Modal_test.user_name = str(user).split('#')[0]
                            flag = False
                            with open(fname, 'r') as csv_file:
                                csv_reader = csv.reader(csv_file)
                                if df.shape[0] != 0:
                                    for line in csv_reader:
                                        if line[2] != str(Modal_test.User_ID):
                                            Updated.append(line)
                                        else:
                                            flag = True
                                            embed = discord.Embed(
                                                title=f"You have removed your previous wallet address from the "
                                                      f"Whitelist.\n Please click ```Add``` to submit a new wallet "
                                                      f"address before the deadline.",
                                                color=discord.Color.red())
                                            await interaction.response.send_message(embeds=[embed], ephemeral=True)
                            if flag:
                                with open(fname, 'w', encoding='UTF8', newline='') as writer_file:
                                    csv_writer = csv.writer(writer_file)
                                    csv_writer.writerows(Updated)
                            else:
                                embed = discord.Embed(
                                    title="You have not submitted your wallet address yet. \nPlease click `Add` to submit "
                                          "your wallet address before the deadline.",
                                    color=discord.Color.red())
                                await interaction.response.send_message(embeds=[embed], ephemeral=True)

                        async def button2_callback(interaction):
                            print(guild.id)
                            df = pd.read_csv(str(guild.id) + '.csv')
                            Modal_test.User_ID = interaction.user.id
                            user = await bot.fetch_user(interaction.user.id)
                            Modal_test.user_name = str(user).split('#')[0]
                            with open(str(guild.id) + '.csv', 'r') as csv_file:
                                csv_reader = csv.reader(csv_file)
                                flag = False
                                Address = '\0'
                                if df.shape[0] != 0:
                                    for line in csv_reader:
                                        if line[2] == str(Modal_test.User_ID):
                                            Address = line[1]
                                            flag = True
                                            break
                                        else:
                                            flag = False
                                if flag:
                                    embed = discord.Embed(
                                        title="You have successfully registered yourself on the Whitelist!",
                                        color=discord.Color.green())
                                    embed.add_field(name="Wallet Address:", value=f"{Address}", inline=False)
                                    await interaction.response.send_message(embeds=[embed], ephemeral=True)
                                else:
                                    embed = discord.Embed(
                                        title="You have not submitted your wallet address yet. \n Please click `Add` to "
                                              "submit your wallet address before the deadline.",
                                        color=discord.Color.red())
                                    await interaction.response.send_message(embeds=[embed], ephemeral=True)

                        async def button_callback(interaction):
                            modal = MyModal(guild_id=guild.id)
                            Modal_test.User_ID = interaction.user.id
                            user = await bot.fetch_user(interaction.user.id)
                            Modal_test.user_name = str(user).split('#')[0]
                            await interaction.response.send_modal(modal)

                button.callback = button_callback
                button2.callback = button2_callback
                button3.callback = button3_callback
                # if channel.name == 'general':
                embed = discord.Embed(
                    title=f"Congratulations! 🎉  If you are seeing this, you are officially accepted to be on our Whitelist!",
                    color=discord.Color.green())
                embed.add_field(
                    name=f"The following are the instructions to officially submit your wallet address that will be used "
                         f"for minting:",
                    value="\n\n:one: Click __**Add**__ to submit your wallet address\n\n:two: "
                          f"Click __**Check**__ if you would like to check the wallet address "
                          f"you have submitted\n\n:three: Click __**Delete**__ if you would like to remove your "
                          f"existing wallet address and submit an entirely new one",
                    inline=False)
                embedtxt = discord.Embed(title="All set! Your bot is ready for use!", color=discord.Color.green())
                await ctx.respond(embed=embedtxt, ephemeral=True)
                await ctx.channel.send(embed=embed, view=view)
                break
    else:
        embed = discord.Embed(title=f"ERROR ❌ ",
                              color=discord.Color.red())
        embed.add_field(name="Initiate the bot", value="Buy the license or initiate the license and variables (if you "
                                                       "already have one) using the `/start` command", inline=False)
        await ctx.respond(embed=embed, ephemeral=True)


@commands.has_permissions(administrator=True)
@bot.slash_command(
    name="download-csv",
    description="To download the .csv file of successfully submitted wallets",
    guild_ids=[968473991155179520, 996682296293851176, 997393143081226251]
)
async def _download_csv(ctx):
    data = pd.read_csv("Whitelist.csv")
    if data.shape[0] == 0:
        embed = discord.Embed(title="ERROR ❌",
                              color=discord.Color.red())
        embed.add_field(name="There is no wallet address submitted yet", value=f"0️⃣", inline=False)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        await ctx.respond(file=discord.File("Whitelist.csv"), ephemeral=True)


# bot = discord.Client(intents=discord.Intents.default())
# @client.command()
# async def clear(ctx, amount=10):
#     await ctx.channel.purge(limit=amount)
#
# client.run(TOKEN)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    data = ["UserName", "Wallet_Address", "User_ID"]
    for guild in bot.guilds:
        fname = str(guild.id) + '.csv'
        # print(fname)
        if not os.path.exists('9123123193851176.csv'):
            with open(fname, 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Whitelist | Collecting wallet addresses"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


class MyModal(Modal):
    def __init__(self, guild_id):
        self.guild_id = guild_id
        print(self.guild_id)
        super().__init__(title="Submit Wallet Address")  # title of the modal up top
        if Modal_test.currency == "Eth" or Modal_test.currency == "ETH" or Modal_test.currency == "eth":
            self.add_item(InputText(label="Wallet Address", placeholder="0xGh4351Fe436ds73sa6F06542w13794DD04E59Fde4"))
        else:
            self.add_item(InputText(label="Wallet Address", placeholder="83astBRguLMdt2h5U1Tpdq5tjFoJ6noeWasT3mDLVcri"))
        # self.add_item(
        #     InputText(
        #         label="Long Input",
        #         value="Default",  # sort of like a default
        #         style=discord.InputTextStyle.long,  # long/short
        #     )
        # )

    async def callback(self, interaction: discord.Interaction):

        Modal_test.wallet_address = str(self.children[0].value)
        if Modal_test.currency == "Eth" or Modal_test.currency == "ETH" or Modal_test.currency == "eth":
            Modal_test.valid_wallet = w3.isAddress(str(self.children[0].value))
            if Modal_test.valid_wallet:
                Modal_test.balance = w3.fromWei(w3.eth.get_balance(str(self.children[0].value)), 'ether')
            else:
                embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                embed.add_field(name="INVALID wallet address. ", value=f'**Resubmit a valid address.**',
                                inline=False)
                await interaction.response.send_message(embeds=[embed], ephemeral=True)
        if Modal_test.currency == "Sol" or Modal_test.currency == "SOL" or Modal_test.currency == "sol":
            sol = http_client.get_balance(str(self.children[0].value))
            try:
                sol = sol['result']['value']
            except:
                embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                embed.add_field(name="INVALID wallet address. ",
                                value=f'**Resubmit a valid address.**',
                                inline=False)
                await interaction.response.send_message(embeds=[embed], ephemeral=True)
                return
            Modal_test.balance = sol * 0.000000001
            print(Modal_test.balance)
            print(Modal_test.minimun_balance)
            if Modal_test.balance < Modal_test.minimun_balance:
                embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                embed.add_field(name="Your wallet balance is insufficient to qualify for the Whitelist.",
                                value=f'**Resubmit your wallet address once you have sufficient balance to qualify '
                                      f'before the deadline.**',
                                inline=False)
                await interaction.response.send_message(embeds=[embed], ephemeral=True)
                return
            else:
                guild_id = 0
                flag = file_submission(self.guild_id)
                if flag == 'Done':
                    embed = discord.Embed(
                        title=f"Congratulations {Modal_test.user_name}! We are excited to have you on board!",
                        color=discord.Color.green())
                    embed.add_field(name="You have successfully registered the following wallet address:",
                                    value=self.children[0].value, inline=False)
                    await interaction.response.send_message(embeds=[embed], ephemeral=True)
                if flag.isdigit():
                    embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                    embed.add_field(name=f"This wallet has already been registered by you or another user.",
                                    value=f"**Click on `Check` to see if it was submitted by you.**", inline=False)
                    await interaction.response.send_message(embeds=[embed], ephemeral=True)
                else:
                    embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                    embed.add_field(name=f"This User has already been registered with another Wallet.",
                                    value=f'**Click on `Check` to see the Address**',
                                    inline=False)
                    await interaction.response.send_message(embeds=[embed], ephemeral=True)
                return
        if Modal_test.balance >= Modal_test.minimun_balance:
            if Modal_test.valid_wallet:
                flag = file_submission(self.guild_id)
                if flag == 'Done':
                    embed = discord.Embed(
                        title=f"Congratulations {Modal_test.user_name}! We are excited to have you on board!",
                        color=discord.Color.green())
                    embed.add_field(name="You have successfully registered the following wallet address:",
                                    value=self.children[0].value, inline=False)
                    await interaction.response.send_message(embeds=[embed], ephemeral=True)
                if flag.isdigit():
                    embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                    embed.add_field(
                        name=f"You have already submitted a wallet address. You can only submit **ONE (1)** wallet "
                             f"address.",
                        value=f"**Click on `Check` to see the wallet address you have already submitted.**",
                        inline=False)
                    await interaction.response.send_message(embeds=[embed], ephemeral=True)
                else:
                    embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                    embed.add_field(name=f"This wallet has already been registered by another user.",
                                    value=f'**Click on `Add` to submit another Address**',
                                    inline=False)
                    await interaction.response.send_message(embeds=[embed], ephemeral=True)

            else:
                embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
                embed.add_field(name="INVALID wallet address. ",
                                value=f'**Resubmit a valid address.**',
                                inline=False)
                await interaction.response.send_message(embeds=[embed], ephemeral=True)
        else:
            embed = discord.Embed(title=f"ERROR ❌", color=discord.Color.red())
            embed.add_field(name="Your wallet balance is insufficient to qualify for the Whitelist.",
                            value='**Resubmit your wallet address once you have sufficient balance, to qualify before '
                                  'the deadline.**',
                            inline=False)
            await interaction.response.send_message(embeds=[embed], ephemeral=True)


def file_submission(guild_id):
    data = [Modal_test.user_name, Modal_test.wallet_address, Modal_test.User_ID]
    fname = str(guild_id) + '.csv'
    df = pd.read_csv(fname)
    with open(fname, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        if df.shape[0] != 0:
            for line in csv_reader:
                if line[2] == str(Modal_test.User_ID):
                    return str(Modal_test.User_ID)
                if line[1] == Modal_test.wallet_address:
                    return Modal_test.wallet_address
    with open(fname, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(data)

        f.close()
        print(Modal_test.user_name)
        print(Modal_test.wallet_address)
        print(Modal_test.User_ID)
        return 'Done'


bot.run(TOKEN)
