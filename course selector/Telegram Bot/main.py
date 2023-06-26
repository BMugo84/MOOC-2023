import constants as keys
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import responses as r

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """ Statrs the convo"""
    reply_keyboard = [["test1", "test2", "test3"]]

    await update.message.reply_text(
        "Hello! Thanks for chatting with me!",
        reply_markup = ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="Testing?"
            ) # type: ignore
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a bot. Please type something so that i can respond')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# handle responses

def handle_response(text: str) -> str:

    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there'
    
    if 'how are you' in processed:
        return 'I am good'
    
    if 'i love python ' in processed:
        return 'Remember to subscribe!'
    
    if 'test1' in processed:
        return 'ewe are now working!'
    
    return 'I do not understand the words coming out of your keyboard...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user ({update.message.chat.id}) in  {message_type}: "{text}"')

    if message_type == 'group':
        if keys.BOT_USERNAME in text:
            new_text: str = text.replace(keys.BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(keys.API_KEY).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)



