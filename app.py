import json

from scripts.util import *
from assets.config import *
from assets.keyboards import *
from assets.messages import *

from telegram import (
    Update
)

from telegram.ext import (
    Updater,
    Filters,
    Defaults,
    CallbackContext,
    MessageHandler,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler
)


# from sentence_transformers import SentenceTransformer
# from bs4 import BeautifulSoup
# import psycopg2 as pcg

def get_trait_by_id(cursor, id):
    pass


def get_all_traits(cursor):
    pass


def start(update: Update, context: CallbackContext):
    update.message.reply_text(start_message, reply_markup=start_reply)


def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data == "start":
        query.edit_message_text(start_message, reply_markup=start_reply)

    if data == "start_1":
        query.edit_message_text(start_1_message, reply_markup=start_1_reply)

    if data == "start_2":
        query.edit_message_text(start_2_message, reply_markup=start_2_reply)

    if data == "start_1_1":
        query.edit_message_text(
            start_1_1_message, reply_markup=start_1_1_reply)

    if data == "start_1_2":
        query.edit_message_text(
            start_1_2_message, reply_markup=start_1_2_reply)

    if data == "login":
        query.edit_message_text(login_message)

    if "search" in data:
        query.edit_message_text("This is trait description placeholder.. This trait... Etc...")

    query.answer()


def process_document(update: Update, context: CallbackContext):
    # if user_logged_in:
    #   bot.send_message("You are already logged in")
    #   return None
    
    raise ValueError
    document = update.message.document
    file_bytearray = context.bot.get_file(document).download_as_bytearray()

    is_file_valid = check_file(file_bytearray)
    if is_file_valid:
        context.bot.send_message(update.effective_chat.id, correct_file_message)
    else:
        context.bot.send_message(update.effective_chat.id, wrong_file_message, reply_markup=wrong_file_reply)


def search(update: Update, context: CallbackContext):
    # if user.is_registered:
    #   get_search_engine(query)
    # search_query = update.message.text

    buttons = [InlineKeyboardButton(
        "Trait Name", callback_data="search") for _ in range(5)]
    keyboard = InlineKeyboardMarkup([[button] for button in buttons])

    update.message.reply_text(
        "Find articles in this advisories", reply_markup=keyboard)

def error_hanlder(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=DEVELOPER_CHAT_ID, text=f"Error was raised while handling update {json.dumps(update.to_dict(   ), indent=4)} {context.error}")

# print("Connecting to database...", end="", flush=True)
# conn = pcg.connect(
#     database="postgres",
#     user="postgres",
#     host="34.72.238.182",
#     password="SerendiPMa1688%"
# )
# cursor = conn.cursor()
# print("OK!")

# print("Loading traits description..")
# cursor.execute("SELECT trait_description FROM lntraits")
# traits = []
# for text in cursor.fetchall():
#     text = BeautifulSoup(text).text.replace("\xa0", " ")
#     traits.append(text)
# print("OK!")

# print("Loading SBERT model...")
# model = SentenceTransformer("paraphrase-albert-small-v2")

# print("Creating traits embeddings..")
# corpus_embeddgings = model.encode(traits)
# print("OK!")

defaults = Defaults("html", disable_web_page_preview=True)
updater = Updater(token=TELEGRAM_TOKEN, defaults=defaults)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, search))
dispatcher.add_handler(MessageHandler(Filters.document, process_document))
dispatcher.add_handler(CallbackQueryHandler(callback))

dispatcher.add_error_handler(error_hanlder)

updater.start_webhook(
    listen=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    url_path=TELEGRAM_TOKEN,
    webhook_url=f"https://{WEBHOOK_URL}:{WEBHOOK_PORT}/{TELEGRAM_TOKEN}",
    cert=CERT_PATH,
    key=KEY_PATH
)

# updater.start_polling()