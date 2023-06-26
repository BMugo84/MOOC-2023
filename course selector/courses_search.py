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

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function handles the start command and displays a list of universities as keyboard buttons.
    """
    reply_keyboard = [[university] for university in universities]
    await update.message.reply_text(
        "Hello! I am the Brainhost bot here to help you select courses!\n"
        "Please select the university you are interested in:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )

    context.user_data['university_response'] = update.message.text

async def handle_university(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function handles the selection of a university by the user.
    It fetches the text from the previous command's output and creates a keyboard button for courses.
    It then prompts the user to select a course from the available options.
    """
    # Fetch text from start_command output
    text = update.message.text.upper()

    # Filter the dataframe to get courses for the selected university
    filtered_df = df.loc[df['INSTITUTION NAME'] == text]
    courses = filtered_df['PROGRAMME NAME'].tolist()

    # Create keyboard buttons for courses
    reply_keyboard = ReplyKeyboardMarkup([[course] for course in courses], one_time_keyboard=True)

    await update.message.reply_text(
        "Please select the course needed:",
        reply_markup=reply_keyboard
    )

    context.user_data['course_response'] = update.message.text


async def handle_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function handles the selection of a course by the user.
    It fetches the text from the user's input and retrieves the selected university and course responses from the user data.
    It then prints out the cutoff points for the selected course.
    """
    text = update.message.text

    # Fetch text from handle_university output
    start_response = context.user_data.get('university_response')
    first_level_response = context.user_data.get('course_response')

    # Retrieve cutoff points for the selected course and university
    filtered_df = df.loc[
        (df['PROGRAMME NAME'] == text.upper()) & (df['INSTITUTION NAME'] == first_level_response.upper())
    ]
    cutoffs = filtered_df[
        ['2015 CUTOFF', '2016 CUTOFF', '2017 CUTOFF', '2018 CUTOFF', '2019 CUTOFF', '2020 CUTOFF', '2021 CUTOFF']
    ]

    # Convert cutoffs to a dictionary
    cutoffs = cutoffs.to_dict(orient='list')
    print(cutoffs)

    # Prepare the output lines for cutoff points
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
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )



if __name__ == '__main__':
    app = Application.builder().token(keys.API_KEY).build()

    # add handler to handle user input 
    app.add_handler(CommandHandler('start', start_command))

    # add handler to handle university messages
    app.add_handler(MessageHandler(filters.TEXT & ~(filters.COMMAND), handle_university))

    # add handler to handle courses
    app.add_handler(MessageHandler(filters.TEXT & ~(filters.COMMAND), handle_course))

    # add handler to exit
    app.add_handler(CommandHandler('exit', exit))

    print('Polling...')
    app.run_polling(poll_interval=3)