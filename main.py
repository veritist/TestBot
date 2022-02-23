#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    #update.message.reply_markdown_v2(r'Hi {user.mention_markdown_v2()}\!',reply_markup=ForceReply(selective=True),
    update.message.reply_text(('Hello, please message me in case you can\'t reach your dispatcher or anyone else on the team you were trying to get ahold of\. I will contact the office and get someone to assist you\.\n\nPlease try to describe your problem in a single message\.\n\nThank you\!\n\n'+'_PS\. I am a robot and do not reply to your messages directly, you will get contacted by a person, please be patient\._'), parse_mode='MarkdownV2');
    context.bot.pinChatMessage(chat_id=update.message.chat_id, message_id=update.message.message_id+1, disable_notification=None, timeout=None, api_kwargs=None);
    


#def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    #update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    
    #update.message.reply_text(update.message.text) (*_bold and italic_*', parse_mode='MarkdownV2)
    #update.message.reply_text('*_bold and italic_*', parse_mode='MarkdownV2');
    
    
    update.message.reply_text(('Your message was received, someone on our team will get in touch with you shortly\. '+'_This is an automated message\._'), parse_mode='MarkdownV2');
    context.bot.forwardMessage("-647801647", from_chat_id=update.message.chat_id, message_id=update.message.message_id, disable_notification=None, timeout=None, api_kwargs=None, protect_content=None);


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5145301460:AAGXj7nVfyut_bBTfW6aOE3K0VAn8jCjgxs", use_context=True);

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    #dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()