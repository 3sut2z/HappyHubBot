import os
import discord
from discord.ext import commands
from discord import app_commands
from urllib.parse import urlparse, parse_qs
import requests

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Bot is ready")
    await tree.sync()
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Happy Hub 🔥"))

# Arceus Command
@tree.command(
    name="arceus",
    description="Bypass key Arceus-x"
)
@app_commands.describe(link="Link Get Key Arceus-x")
async def arceux(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    hwid = parse_qs(parsed_url.query).get('hwid', [''])[0]

    if not hwid:
        embed = discord.Embed(
            title="Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Made by Happy Hub")
        embed.set_thumbnail(url="")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-arceusx/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description="```New link or try again```",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="")
            elif data['key'] == 'Not allowed bypass':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description="```Not allowed bypass```",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="TYPE",
                    value="hwid",
                    inline=False
                )
                embed.add_field(
                    name="KEY FOR MOBILE",
                    value=f"{data['key']}",
                    inline=False
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="** Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="** Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

# Codex Command
@tree.command(
    name="codex",
    description="Bypass key Codex"
)
@app_commands.describe(link="Link Get Key Codex")
async def codex(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    token = parse_qs(parsed_url.query).get('token', [''])[0]

    if not token:
        embed = discord.Embed(
            title="Invalid Link",
            description=f"{link}",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Made by Happy Hub")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-codex/?token={token}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description="**New link or try again**",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
            elif data['key'] == 'Not allowed bypass':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description="Not allowed bypass",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="")
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="TYPE",
                    value="token",
                    inline=False
                )
                embed.add_field(
                    name="KEY FOR MOBILE",
                    value=f"{data['key']}",
                    inline=False
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="** Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="** Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

# Delta Command
@tree.command(
    name="delta",
    description="Bypass key Delta"
)
@app_commands.describe(link="Link Get Key Delta")
async def delta(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    id = parse_qs(parsed_url.query).get('id', [''])[0]

    if not id:
        embed = discord.Embed(
            title="Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Made by Happy Hub")
        embed.set_thumbnail(url="")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-delta/?hwid={id}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="TYPE",
                    value="id",
                    inline=False
                )
                embed.add_field(
                    name="KEY FOR MOBILE",
                    value=f"{data['key']}",
                    inline=False
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="** Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="** Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

# Fluxus Command
@tree.command(
    name="fluxus",
    description="Bypass key Fluxus"
)
@app_commands.describe(link="Link Get Key Fluxus")
async def fluxus(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    HWID = parse_qs(parsed_url.query).get('HWID', [''])[0]

    if not HWID:
        embed = discord.Embed(
            title="Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Made by Happy Hub")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-fluxus/?hwid={HWID}&api_key=E99l9NOctud3vmu6bPne"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="TYPE",
                    value="HWID",
                    inline=False
                )
                embed.add_field(
                    name="KEY FOR MOBILE",
                    value=f"{data['key']}"
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="** Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="** Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

# Vegax Command
@tree.command(
    name="vegax",
    description="Bypass key Vegax"
)
@app_commands.describe(link="Link Get Key Vegax")
async def vegax(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    hwid = parse_qs(parsed_url.query).get('hwid', [''])[0]

    if not hwid:
        embed = discord.Embed(
            title="Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Made by Happy Hub")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-vegax/?hwid={hwid}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="TYPE",
                    value="hwid",
                    inline=False
                )
                embed.add_field(
                    name="KEY FOR MOBILE",
                    value=f"{data['key']}",
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="** Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="** Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

# Hydrogen Command
@tree.command(
    name="hydrogen",
    description="Bypass key Hydrogen"
)
@app_commands.describe(link="Link Get Key Hydrogen")
async def delta(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    id = parse_qs(parsed_url.query).get('id', [''])[0]

    if not id:
        embed = discord.Embed(
            title="Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Made by Happy Hub")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-hydrogen/?hwid={id}&api_key=E99l9NOctud3vmu6bPne"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="TYPE",
                    value="id",
                    inline=False
                )
                embed.add_field(
                    name="KEY FOR MOBILE",
                    value=f"{data['key']}",
                    inline=False
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="** Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="** Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)   
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

# Linkvertise Command
@tree.command(
    name="linkvertise",
    description="Bypass Linkvertise link"
)
@app_commands.describe(link="Linkvertise URL")
async def linkvertise(interaction: discord.Interaction, link: str):
    api_url = f"https://stickx.top/api-linkvertise/?link={link}&api_key=E99l9NOctud3vmu6bPne"

    initial_embed = discord.Embed(
        title="**Please wait...**",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=initial_embed)

    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description="```Error: New link or try again```",
                    color=0xff0000
                )
            elif data['key'] == 'Not allowed bypass':
                embed = discord.Embed(
                    title="**Bypass Failed**",
                    description="```Not allowed bypass```",
                    color=0xff0000
                )
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"{data['key']}",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Successful!",
                    value=f"{data['key']}",
                    inline=False
                )
                embed.set_footer(text="Made by Happy Hub")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1293223923562975335/1312712534977019914/images.png?ex=674e2711&is=674cd591&hm=71100ee12b5c0d8e31a16427a51bda96e45d445ea5af2808bb978b31a46dc862&=&format=webp&quality=lossless")
        else:
            embed = discord.Embed(
                title="**Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )

    await interaction.edit_original_response(embed=embed)
    await interaction.followup.send(f"{data['key']}", ephemeral=True)

client.run(TOKEN)
