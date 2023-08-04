from modules.github import GitHub

# Your API_ID and API_HASH from my.telegram.org
api_id = ""
api_hash = ""

# If you are using a userbot, change this to True
userbot = True

# Modules
modules = {
    "stars": GitHub('0stanislav/tg-message-beautifier')
}

# Message variables
message = """
{messageText}

<b>💫 <a href='https://github.com/0stanislav/tg-message-beautifier'>tg-message-beautifier</a> ({stars})</b>
"""
