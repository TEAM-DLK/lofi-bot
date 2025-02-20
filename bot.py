import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Function to download song from SoundCloud
def download_song(update, context):
    # Get the URL sent by the user
    song_url = ' '.join(context.args)
    
    if song_url:
        url = "https://soundcloud-songs-downloader.p.rapidapi.com/"
        payload = {"url": song_url}
        headers = {
            "x-rapidapi-key": "a850f0e046msh09fcc3ee5253422p15c903jsna96a5d25b3b9",
            "x-rapidapi-host": "soundcloud-songs-downloader.p.rapidapi.com",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Make the API request to SoundCloud Downloader
        response = requests.post(url, data=payload, headers=headers)
        
        # If the request was successful, send the download link to the user
        if response.status_code == 200:
            data = response.json()
            if 'url' in data:
                download_link = data['url']
                update.message.reply_text(f"Here is your download link: {download_link}")
            else:
                update.message.reply_text("Sorry, I couldn't find the song.")
        else:
            update.message.reply_text("There was an error retrieving the song.")
    else:
        update.message.reply_text("Please provide a valid SoundCloud song URL.")

# Set up the Telegram bot with the API token
def main():
    updater = Updater("YOUR_TELEGRAM_BOT_API_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Add the command handler for '/download'
    dp.add_handler(CommandHandler("download", download_song))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()