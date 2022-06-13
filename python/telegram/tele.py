from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "5591863640:AAHqDldhR_IeWV8vvegVa3zsnJ_947XBt0s"

def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""

    update.message.reply_text('Please choose:',
                              reply_markup = keyboard_main_menu())


def main_menu(update: Update, context: CallbackContext) -> None:
    """ Displays the main menu keyboard when called. """

    query = update.callback_query
    query.answer()
    query.edit_message_text(text         = 'Please choose:',
                            reply_markup = keyboard_main_menu())


def keyboard_main_menu():
    """ Creates the main menu keyboard """

    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='1'),
         InlineKeyboardButton("Option 2", callback_data='2'),],
    ]

    return InlineKeyboardMarkup(keyboard)


def confirm(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""

    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Yes", callback_data=f'YES{query.data}'),
         InlineKeyboardButton("No",  callback_data='main'),],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=f"Selected option {query.data}."
                                 f"Are you sure ? ",
                            reply_markup=reply_markup)


def do_action_1(update: Update, context: CallbackContext) -> None:

    keyboard = [[InlineKeyboardButton("Main menu", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option {query.data}\n"
                                 f"Executed action 1.",
                            reply_markup=reply_markup)


def do_action_2(update: Update, context: CallbackContext) -> None:

    keyboard = [[InlineKeyboardButton("Main menu", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option {query.data}\n"
                                 f"Executed action 2.",
                            reply_markup=reply_markup)


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(confirm, pattern='^(|1|2)$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(do_action_1, pattern='YES1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(do_action_2, pattern='YES2'))


    # Start the Bot
    updater.start_polling()
    print('started')

if __name__ == '__main__':
    main()
