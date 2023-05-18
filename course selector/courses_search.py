from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import constants as keys
import pandas as pd

# import dataframe 
df = pd.read_excel('DEGREE COURSES.xlsx')

universities = [
    "University of Nairobi",
    "Kenyatta University",
    "Jomo Kenyatta University of Agriculture and Technology",
    "Egerton University	",
    "Moi University	",
    "Technical University of Kenya",
    "Maseno University",
    "Murang'a University of Technology",
    "Kisii University",
    "University of Embu	",
    "Karatina University	",
    "Masinde Muliro University of Science and Technology	",
    "Dedan Kimathi University of Technology	 ",
    "Multimedia University of Kenya	",
    "Pwani University	",
    "Meru University of Science and Technology",
    "South Eastern Kenya University",
    "The Co-operative University of Kenya",
    "Garissa University	",
    "Technical University of Mombasa",
    "Jaramogi Oginga Odinga University of Science and Technology",
    "University of Eldoret",
    "Kibabii University",
    "Chuka University",
    "Machakos University",
    "Maasai Mara University",
    "Kirinyaga University",
    "Laikipia University",
    "Rongo University",
    "University of Kabianga	",
    "Taita Taveta University"
]


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """ Statrs the convo"""
    reply_keyboard = [[university] for university in universities]

    await update.message.reply_text(
        "Hello! I am Brainhost bot here to help you select courses!"
        "Which course branch are you interested in?",
        reply_markup = ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="Testing?",
            resize_keyboard = True
            ) # type: ignore
        )
    
def handle_response(text:str) -> tuple:

    # fetch university name from df to match against user text 
    unique_uni_name = df['INSTITUTION NAME'].unique()
    processed: str = text.upper()
    if processed in unique_uni_name:
        courses_df = df[df['INSTITUTION NAME'] == processed]
        courses = courses_df['PROGRAMME NAME']
        reply_keyboard = [[course] for course in courses]
        return [[course] for course in courses]
    
    return "doesnt work yet"

    

    
    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a bot. Please type something so that i can respond')



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # we want to check if the message type is from a group
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # debugger
    print(f'user ({update.message.chat.id}) in  {message_type}: "{text}"')

    # check whether message type is group or private
    if message_type == 'group':

        # if the message is from a group and a user responds using the bot username 
        if keys.BOT_USERNAME in text:
            new_text: str = text.replace(keys.BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    # debugger
    print('Bot: ', response)
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(keys.API_KEY).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)