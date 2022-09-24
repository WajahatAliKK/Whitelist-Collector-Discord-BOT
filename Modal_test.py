user_name = ''
wallet_address = ''
User_ID = 0
valid_wallet = False
balance = 0
licenseKey = False
currency = []
minimun_balance = []


# function Main(paramet)
# {
#     var data = aqFile.ReadWholeTextFile("D://Base-JSON40.json",aqFile.ctUTF8);
#     var objJSON2 = JSON.parse(data).Data[paramet];
#     aqString.ListSeparator = (":");
#     Log.Message(data)
#     Log.Message(data.length);
#     Log.Message(aqString.GetListItem(objJSON2,0));
#     for (var key in data)
#     {
#         var Parentvalue=data[key];
#         for ( var value in Parentvalue)
#         if(paramet==key)
#         {
#             Log.Message(value)
#             Log.Message(ParentValue);
#             break;
#         }
#     }
# }
#
# function output()
# {
#     Main("APPL_CRTE_DTE")
# }
# import discord
# from discord.ui import InputText, Modal
#
# bot = discord.Bot()
#
# servers = [968473991155179520]
#
#
# @bot.event
# async def on_ready():
#     print(f"We have logged in as {bot.user}")
#
#
# class MyModal(Modal):
#     def __init__(self) -> None:
#         super().__init__(title="A Modal")  # title of the modal up top
#         self.add_item(InputText(label="Short Input", placeholder="Placeholder"))
#         self.add_item(
#             InputText(
#                 label="Long Input",
#                 value="Default",  # sort of like a default
#                 style=discord.InputTextStyle.long,  # long/short
#             )
#         )
#
#     async def callback(self, interaction: discord.Interaction):
#         embed = discord.Embed(title="Your Modal Results", color=discord.Color.blurple())
#         embed.add_field(name="First Input", value=self.children[0].value, inline=False)
#         embed.add_field(name="Second Input", value=self.children[1].value, inline=False)
#         await interaction.response.send_message(embeds=[embed])
#
#
# @bot.event
# async def on_message(interaction):
#     modal = MyModal()
#     await interaction.response.send_modal(modal)
#
#
# bot.run("OTczOTIxNjE5ODI1Mjc5MDE3.GRWJzL.eOvClJNIu7WiBjD2ALpbD3oMNwlytCdjAIF9SI")
