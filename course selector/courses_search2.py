from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import constants as keys
import pandas as pd

# keyboard buttons for universities
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

# import dataframe 
df = pd.read_excel('DEGREE COURSES.xlsx')

# create the start_command function 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [[university] for university in universities]
    await update.message.reply_text(    # type: ignore
        "Hello! I am Brainhost bot here to help you select courses!"
        "Which course branch are you interested in?",
        reply_markup = ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="Universities?",
            resize_keyboard = True
            ) # type: ignore
    )

    context.user_data['university_response'] = update.message.text# type: ignore

async def handle_university(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # fetch text from start_command output
    text = update.message.text# type: ignore
    text = text.upper()# type: ignore

    # create another keyboardbutton for courses
    filtered_df = df.loc[df['INSTITUTION NAME'] == text]
    courses = filtered_df['PROGRAMME NAME'].tolist()
    reply_keyboard = ReplyKeyboardMarkup([[course] for course in courses], one_time_keyboard=True)

    await update.message.reply_text(       # type: ignore
        "Please select the course needed",
        reply_markup = reply_keyboard
    )

    context.user_data['course_response'] = update.message.text # type: ignore


async def handle_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # fetch text from handle_university output
    start_response = context.user_data.get('university_response')# type: ignore
    first_level_response = context.user_data.get('course_response')# type: ignore

    # print out cutoff points for the selected course
    filtered_df = df.loc[(df['PROGRAMME NAME'] == first_level_response.upper()) & (df['INSTITUTION NAME'] == start_response.upper())]# type: ignore
    cutoffs = filtered_df[['2015 CUTOFF', '2016 CUTOFF', '2017 CUTOFF', '2018 CUTOFF', '2019 CUTOFF', '2020 CUTOFF', '2021 CUTOFF']]
    await update.message.reply_text(
        f'{cutoffs}'
    )



if __name__ == '__main__':
    app = Application.builder().token(keys.API_KEY).build()

    # add handler to handle user input 
    app.add_handler(CommandHandler('start', start_command))

    # add handler to handle university messages
    app.add_handler(MessageHandler(filters.TEXT & ~(filters.COMMAND), handle_university))

    # add handler to handle courses
    app.add_handler(MessageHandler(filters.TEXT & ~(filters.COMMAND), handle_course))

    print('Polling...')
    app.run_polling(poll_interval=3)