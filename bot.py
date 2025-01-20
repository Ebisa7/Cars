from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define a function for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Define the image path (make sure the image exists in the directory)
    image_path = "IMG_20250120_212008_499.jpg"  # Adjust the path if necessary
    
    # Create inline buttons
    keyboard = [
        [InlineKeyboardButton("Open", url="https://t.me/Carsx_bot/start")],
        [InlineKeyboardButton("Join community", url="https://t.me/cars_ann")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with image and text
    await update.message.reply_photo(
        photo=open(image_path, 'rb'),
        caption="Vroom\nLet's drive together! 🚗",  # The caption text
        reply_markup=reply_markup
    )

# Main function to start the bot
def main():
    # Use your bot token here
    token = "7899640920:AAEmIEb6qOfx1oxmYmLQU8wALLFyRuRz_Dg"

    # Create the Application and pass the bot token
    application = ApplicationBuilder().token(token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()