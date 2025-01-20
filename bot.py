from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define a function for the /start command
def start(update: Update, context: CallbackContext):
    # Define the image path (make sure the image exists in the directory)
    image_path = "Car.png"  # Adjust the path if necessary
    
    # Create inline buttons
    keyboard = [
        [InlineKeyboardButton("Open", url="https://t.me/Carsx_bot/start")],
        [InlineKeyboardButton("Join community", url="https://t.me/cars_ann")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with image and text
    update.message.reply_photo(
        photo=open(image_path, 'rb'),
        caption="Vroom\nLet's drive together! 🚗",  # The caption text
        reply_markup=reply_markup
    )

# Main function to start the bot
def main():
    # Use your bot token here
    token = "7899640920:AAEmIEb6qOfx1oxmYmLQU8wALLFyRuRz_Dg"

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()