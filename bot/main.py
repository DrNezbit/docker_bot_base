import discord
import sqlalchemy
import sys

python_version=f"Python: {sys.version}"
discord_version=(f"discord.py: v{discord.__version__}")
sqlalchemy_version=f"SQLalchemy: v{sqlalchemy.__version__}"
print(f"Container Built \n{python_version} \n{discord_version} \n{sqlalchemy_version}")
