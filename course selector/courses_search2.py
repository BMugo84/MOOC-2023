from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
import constants as keys
import pandas as pd

# conversation handler 
UNIVERSITY, COURSE = range(2)

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
        "Hello! I am the Brainhost bot, your course selection assistant!"
        "Please select a university from the list below to explore the available courses:",
        reply_markup = ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="Universities?",
            resize_keyboard = True
            ) # type: ignore
    )

    context.user_data['university_response'] = update.message.text# type: ignore

    return UNIVERSITY

async def handle_university(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """
    This function handles the user's university selection and prompts for the course selection.
    """
    # fetch text from start_command output
    text: str = update.message.text.upper()

    # create another keyboardbutton for courses
    filtered_df = df.loc[df['INSTITUTION NAME'] == text]
    courses = filtered_df['PROGRAMME NAME'].tolist()
    reply_keyboard = ReplyKeyboardMarkup([[course] for course in courses], one_time_keyboard=True)

    await update.message.reply_text( 
        "Please select the course needed",
        reply_markup = reply_keyboard
    )

    context.user_data['course_response'] = update.message.text 

    return COURSE


async def handle_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function handles the user's course selection and displays the cutoff points for the selected course.
    """
    text = update.message.text
    start_response = context.user_data.get('university_response')  # Fetch text from handle_university output
    first_level_response = context.user_data.get('course_response')  # Fetch text from course selection

    # Filter the dataframe to select the cutoff points for the selected course and institution
    filtered_df = df.loc[(df['PROGRAMME NAME'] == text.upper()) & (df['INSTITUTION NAME'] == first_level_response.upper())]
    cutoffs = filtered_df[['2015 CUTOFF', '2016 CUTOFF', '2017 CUTOFF', '2018 CUTOFF', '2019 CUTOFF', '2020 CUTOFF', '2021 CUTOFF']]

    cutoffs = cutoffs.to_dict(orient='list')
    print(cutoffs)

    output_lines = []
    for year, cutoff_values in cutoffs.items():
        line = f"{year}: {', '.join(map(str, cutoff_values))}"
        output_lines.append(line)

    await update.message.reply_text(
        "\n".join(output_lines)
    )


async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    await update.message.reply_text(
        "Bye! I hope we can talk again some day."
    )

    return ConversationHandler.END



if __name__ == '__main__':
    app = Application.builder().token(keys.API_KEY).build()


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            UNIVERSITY: [MessageHandler(filters.TEXT & ~(filters.COMMAND), handle_university)],
            COURSE: [MessageHandler(filters.TEXT & ~(filters.COMMAND), handle_course)],
        },
        fallbacks=[CommandHandler("exit", exit)],
    )

    app.add_handler(conv_handler)
    print('Polling...')
    app.run_polling(poll_interval=3) # type: ignore