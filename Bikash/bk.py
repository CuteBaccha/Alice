# Powered By @I_LOVE_YOU_MY_HEARTBEET @ID_SELLER00

from typing import Union, List
from pyrogram import filters
from Bikash.config import COMMAND_PREFIXES

## ALice family

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
