# All messages structure:
# <step_name>_<step_id>_ ... _<step_id>

from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# This is /start reply markup
start_reply = InlineKeyboardMarkup([
    [InlineKeyboardButton("I already have a DNA test", callback_data="start_1")],
    [InlineKeyboardButton("I have not taken a DNA test yet", callback_data="start_2")]
])

# User have a DNA test
start_1_reply = InlineKeyboardMarkup([
    [InlineKeyboardButton("I have DNA raw file", callback_data="start_1_1")],
    [InlineKeyboardButton("I do not have DNA raw file", callback_data="start_1_2")],
    [InlineKeyboardButton("<< Back", callback_data="start")]
])

# User dont have a DNA test
start_2_reply = InlineKeyboardMarkup([
    [InlineKeyboardButton("<< Back", callback_data="start")]
])

# User have a DNA test and raw file
start_1_1_reply = InlineKeyboardMarkup([
    [InlineKeyboardButton("Log in", callback_data="login")],
    [InlineKeyboardButton("<< Back", callback_data="start_1")]
])

# User have a DNA test, not file
start_1_2_reply = InlineKeyboardMarkup([
    [InlineKeyboardButton("<< Back", callback_data="start_1")]
])

# User sent incorrect file
wrong_file_reply = InlineKeyboardMarkup([
    [InlineKeyboardButton("Email", url="info@xymetrics.com")]
])