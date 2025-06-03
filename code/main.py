import telebot
from telebot import types
import time
import random
import datetime
import threading
from zoneinfo import ZoneInfo # Standard library module for timezones
import schedule
import os

# Assuming these are available and correctly implemented in your project
from constants import API_KEY
from film import search_film
from compliment import get_random_compliment_from_file
from motivation import Motivation_quete






bot = telebot.TeleBot(API_KEY, parse_mode=None)

# =================== GLOBAL TEXTS AND DATA STRUCTURES ====================
start1 = "Hi dear "
start2 = "<3\n"
start3 = "I'm BOT and i was created by Tyom, 🤗 especially for you, because YOU are an amazing person❤️\nIf you have any questions` text him @tyomxxx\n"
start4 = "What is your name?😊"

# Game URLs
GAME_URL1 = "https://tyomaliengame.netlify.app/"
GAME_URL2 = "https://doancongbang1991.github.io/mobileapp/mobile/darkninja/"
GAME_URL3 = "https://doancongbang1991.github.io/mobileapp/mobile/stickygoo/"
GAME_URL4 = "https://doancongbang1991.github.io/mobileapp/mobile/blackbats/"
GAME_URL5 = "https://doancongbang1991.github.io/mobileapp/mobile/evilwyrm/"

# Cute messages and texts
cute1 = "Yes! You are very beautiful<3 hehe"
heart = "💜"
heart1 = "❤️"
feel_heart1 = "Can you hear the silence?"
feel_heart2 = "Can you see the dark?"
feel_heart3 = "Can you fix the broken"
feel_heart4 = "Can you..?"
feel_heart5 = "Can you feel my heart?"
love_you = "I Love YOU so fucking much^^"
text_meow = "meow^^"
fall_in_love = "Now this is for you🥹"

love_text = """
I hate this word 
Love 
Because I love so many things 
Like autumn, like listening music, like rain.. 
So you must understand how small it feels to say I love you 
But yet I do 
And I do but this is not a feeling I've felt before 
This love isn't like the one I have for the sun, the summer nights, the waves of the sea.. 
This love is new 
And I'm usually scared of the unknown 
But you make this unexplainable feeling Feel like home 
You make feel safe and warm 
But not the warm a rainy day, a fluffy blanket, a fire makes me feel 
You make my heart warm 
You make me a better person 
Yet devour my thoughts 
But I let it happen 
Because nothing is better than you in my mind 
I love you 
I love you and the feelings you give me 
The feelings are unique 
More unique than every snowflake on a cold mountain♡         
"""

i_wanna_be_yours_text = """
Verse 1:
I wanna be your morning coffee,
The warmth that starts your day.
I wanna be your favorite book,
The one you read and replay.
I wanna be your cozy sweater,
Wrapped around you in the cold.
I wanna be your softest pillow,
The comfort that you hold.

Bridge:
Let me be the light that guides you,
The calm when days are gray.
I’ll be the warmth beside you,
Every step of the way.

Chorus:
I wanna be yours, I wanna be yours,
In every little thing, I wanna be yours.
I wanna be, I wanna be yours,
Through all the highs and lows, I wanna be yours.

Outro:
So here’s my heart, it's open wide,
Every simple way, I’ll be by your side.
Don't leave me behind,
I wanna be your side.

Forever and always
I wanna be
I wanna be
I wanna be yours
I wana be
I wanna be yours..♡
"""

# Dictionary to store per-chat index for 'tyom' responses
tyom_responses_data = {}

# =================== /START COMMAND ====================
@bot.message_handler(commands=['start'])
def start_message(message):
    nickname = message.from_user.username or \
               (message.from_user.first_name + " " + message.from_user.last_name \
                if message.from_user.first_name and message.from_user.last_name else None)
    bot.forward_message(6921647429, message.chat.id, message.message_id) # Forward message to me ('/start' command)

    if nickname:
        bot.send_message(message.chat.id, start1 + nickname + start2 + start3)
    else:
        ask_user(message)

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [
        '/sketch', '/song', '/tyom', '/honest_mind', '/game', '/heart',
        '/hug', '/meow', '/mrrr', '/kiss_me', '/film', '/compliment_me',
        '/me?', '/motivation', '/i_am_sad_now', '/Hiyori_song'
    ]
    keyboard.add(*[types.KeyboardButton(btn) for btn in buttons])

    bot.send_message(message.chat.id, 'Press the buttons as much as you want😁', reply_markup=keyboard)

# =================== Kiss Button ====================
@bot.message_handler(commands=['kiss_me'])
def send_kiss(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Sure! Wait a minute..")
    time.sleep(2)
    bot.send_message(message.chat.id, "💋")
    bot.send_message(message.chat.id, "💋💋")

# =================== GAME COMMAND ====================
@bot.message_handler(commands=['game'])
def start_game(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="👽 Play Alien 👽", url=GAME_URL1))
    markup.add(InlineKeyboardButton(text="🥷 Play Dark Ninja 🥷", url=GAME_URL2))
    markup.add(InlineKeyboardButton(text="🔥🐉 Play Evil Dragon 🐉🔥", url=GAME_URL3))
    markup.add(InlineKeyboardButton(text="🍥 Play Sticky Goo 🍥", url=GAME_URL4))
    markup.add(InlineKeyboardButton(text="🦇 Play Black Bats 🦇", url=GAME_URL5))
    bot.send_message(message.chat.id, "Click the button below to play the game <3", reply_markup=markup)

# =================== Sending Compliments ====================
@bot.message_handler(commands=['compliment_me'])
def send_compliment(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    compl_file_path = "code/text_docs/compliments.txt"
    bot.send_message(message.chat.id, get_random_compliment_from_file(compl_file_path))

# =================== Sending Motivation Quotes ====================
@bot.message_handler(commands=['motivation'])
def send_motivation(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    motiv_file_path = "code/text_docs/motivation.txt"
    bot.send_message(message.chat.id, Motivation_quete(motiv_file_path))

# =================== Search and Send Films Link (REWORKED) ====================
@bot.message_handler(commands=['film'])
def search_get_film(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Tell me what movie would you like to watch and I'll try to find it for you.\n(Enter Latin letter)")
    bot.register_next_step_handler(message, process_film_request)

def process_film_request(message):
    user_input = message.text
    film_link = search_film(user_input)

    if film_link:
        bot.send_message(message.chat.id, "Looks like I found the movie, enjoy)\n" + film_link)
    else:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("No, thank you", callback_data="stop_film_search")
        btn2 = types.InlineKeyboardButton("Find another movie", callback_data="continue_film_search")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "I couldn't find that movie, sorry(\nExplain another way or tell me another movie!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["stop_film_search", "continue_film_search"])
def callback_query_film_search(call):
    if call.data == "stop_film_search":
        bot.send_message(call.message.chat.id, "Alright, maybe next time <3")
    elif call.data == "continue_film_search":
        bot.send_message(call.message.chat.id, "OK, tell me the movie title again.")
        bot.register_next_step_handler(call.message, process_film_request)
    bot.answer_callback_query(call.id) # Always answer callback queries to remove "loading" state on button

# =================== Get User's Name ====================
def ask_user(message):
    bot.send_message(message.chat.id, start4)
    bot.register_next_step_handler(message, process_name_step)

def process_name_step(message):
    name = message.text
    bot.send_message(message.chat.id, start1 + name + start2 + start3)

# =================== Send Sketch Image (REWORKED) ====================
@bot.message_handler(commands=["sketch"])
def image(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    images = [
        "photos_sketch/img2.jpg", "photos_sketch/img3.jpg", "photos_sketch/img4.jpg",
        "photos_sketch/img5.jpg", "photos_sketch/img6.jpg",
        "photos_sketch/img8.jpg", "photos_sketch/img7.jpg", "photos_sketch/img9.jpg"
    ]
    img_path = random.choice(images) # Pick a random image
    with open(img_path, "rb") as img_file:
        bot.send_photo(message.chat.id, img_file)

# =================== Send Music (REWORKED) ====================
@bot.message_handler(commands=['song'])
def send_music(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    music_files = [ # Renamed variable to avoid conflict with imported 'music' module if any
        "music/Arctic Monkeys - Do I Wanna Know.mp3", "music/Arctic Monkeys - Why'd You Only Call Me When You're High.mp3",
        "music/Beach House - Space Song.mp3", "music/Bring Me The Horizon - Drown.mp3", "music/Bring Me The Horizon - Ludens.mp3",
        "music/Bring Me The Horizon - Shadow Moses.mp3", "music/Bring Me The Horizon - Sleepwalking.mp3", "music/Roar - I Can’t Handle Change.mp3",
        "music/Swing - Lynn.mp3", "music/The Drums - Money.mp3", "music/Young - Vacations.mp3"
    ]
    selected_music = random.choice(music_files) # Pick a random song
    with open(selected_music, 'rb') as music_file:
        bot.send_audio(message.chat.id, music_file)

# =================== Send Video (REWORKED) ====================
@bot.message_handler(commands=['i_am_sad_now'])
def send_video(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Wait a minute pls💞")
    videos = [
        "mem_Video/mem1.mp4", "mem_Video/mem2.mp4", "mem_Video/mem3.mp4", "mem_Video/mem4.mp4",
        "mem_Video/mem5.mp4"
    ]
    selected_video = random.choice(videos) # Pick a random video
    with open(selected_video, 'rb') as video_file:
        bot.send_video(message.chat.id, video_file)
    bot.send_message(message.chat.id, "Don't be sad!\nit's time to smile💗\nCos your smile makes me feel alive in this shitty world💖")

# =================== Sending Some Cute Messages ===================
@bot.message_handler(commands=['tyom'])
def cute_words(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    tyom_responses = ["ha jan❤️", "Yeah? wanna hug?🤗", "shutup and kiss me💋💜", "jana"]
    
    chat_id = message.chat.id
    # Get current index for this chat_id, default to 0 if not exists
    current_tyom_idx = tyom_responses_data.get(chat_id, 0)
    
    bot.send_message(chat_id, tyom_responses[current_tyom_idx])
    
    # Update index for next time (cyclically)
    tyom_responses_data[chat_id] = (current_tyom_idx + 1) % len(tyom_responses)
    

@bot.message_handler(commands=['me?'])
def saying_pretty(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, cute1)

@bot.message_handler(commands=['heart'])
def giving_heart(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    # Sending sequence of messages with delays
    bot.send_message(message.chat.id, feel_heart1)
    time.sleep(1)
    bot.send_message(message.chat.id, feel_heart2)
    time.sleep(1)
    bot.send_message(message.chat.id, feel_heart3)
    time.sleep(1.5)
    bot.send_message(message.chat.id, feel_heart4)
    time.sleep(1.5)
    bot.send_message(message.chat.id, feel_heart5)
    time.sleep(1)
    for _ in range(7): # Use _ since loop variable isn't used
        bot.send_message(message.chat.id, heart)
    time.sleep(0.20)
    for _ in range(7):
        bot.send_message(message.chat.id, heart1)
    for _ in range(20):
        bot.send_message(message.chat.id, love_you)
    bot.send_message(message.chat.id, heart1)

# =================== Sending Hug GIF (REWORKED) ===================
@bot.message_handler(commands=['hug'])
def sending_hug(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    gif_files = [ # Renamed variable for clarity
        "hug_GIF/hug1.mp4", "hug_GIF/hug2.mp4", "hug_GIF/hug3.mp4",
        "hug_GIF/hug4.mp4", "hug_GIF/hug5.mp4"
    ]
    selected_gif = random.choice(gif_files) # Pick a random GIF
    with open(selected_gif, 'rb') as gif_file:
        bot.send_animation(message.chat.id, gif_file)

# =================== Saying ILY with Song ====================
@bot.message_handler(commands=['honest_mind'])
def fall_in_love(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, fall_in_love)
    with open("ily_song/tyom black - I.L.U.mp3", 'rb') as music_file:
        bot.send_audio(message.chat.id, music_file)
    bot.send_message(message.chat.id, love_text)

# =================== Sending Our Song ====================
@bot.message_handler(commands=['Hiyori_song'])
def our_song(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    with open("song for isvira/tyom black - I wanna Be Yours.mp3", 'rb') as music_file:
        bot.send_audio(message.chat.id, music_file)
    bot.send_message(message.chat.id, i_wanna_be_yours_text)
    bot.send_message(message.chat.id, "You deserve this song, so it's yours now💋")

# =================== Saying 'meow' and Send Cat Image (REWORKED) ===================
@bot.message_handler(commands=['meow'])
def meow(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    for _ in range(2):
        bot.send_message(message.chat.id, text_meow)
    cat_images = [ # Renamed variable for clarity
        "cat/cat1.jpg", "cat/cat2.jpg", "cat/cat3.jpg", "cat/cat4.jpg",
        "cat/cat5.jpg", "cat/cat6.jpg", "cat/cat7.jpg"
    ]
    selected_cat_img = random.choice(cat_images) # Pick a random cat image
    with open(selected_cat_img, "rb") as img_file:
        bot.send_photo(message.chat.id, img_file)

# =================== Saying 'mrrr' ===================
@bot.message_handler(commands=['mrrr'])
def mrrr(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    for _ in range(10):
        bot.send_message(message.chat.id, "meow<3")
    for _ in range(15):
        bot.send_message(message.chat.id, "mrrr>>>>>>>")
    for _ in range(10):
        bot.send_message(message.chat.id, "❤️")
    # Ensure this path is correct: "Cute_love_bot/cat/cat8.jpg"
    # If this script is NOT in Cute_love_bot/ itself, remove "Cute_love_bot/"
    img_path = "cat/cat8.jpg" # Assuming 'cat' folder is relative to script
    try:
        with open(img_path, "rb") as img_file:
            bot.send_photo(message.chat.id, img_file)
    except FileNotFoundError:
        print(f"Error: Could not find cat image at {img_path}. Please check the path.")
        bot.send_message(message.chat.id, "Sorry, I couldn't send the cat image right now.")


# ===================1 Daily Messages (Background Thread) 1====================


#===========1 Generating random o'clock to send message in that time 1==============================
ALLOWED_HOURS = list(range(3, 20)) # Allowed hours: from 3:00 to 19:00 (before 8 PM)
MIN_GAP = 4  # Minimum 4-hour difference

def generate_three_times():
    while True:
        times = sorted(random.sample(ALLOWED_HOURS, 3))
        if (times[1] - times[0] >= MIN_GAP) and (times[2] - times[1] >= MIN_GAP):
            return [f"{h:02}:00" for h in times]

# Generate and unpack into variables
time1, time2, time3 = generate_three_times()
#===========0 Generating random o'clock to send message in that time 0==============================

# ========== CONFIG ==========
CHAT_ID = '7843995956'
MESSAGE_FILE = 'message.txt'
POSITION_FILE = 'position.txt'
# ============================
def get_next_message():
    # Load all messages from message.txt
    with open(MESSAGE_FILE, 'r', encoding='utf-8') as f:
        messages = [line.strip() for line in f if line.strip()]

    # Load current position
    position = 0
    if os.path.exists(POSITION_FILE):
        with open(POSITION_FILE, 'r') as f:
            try:
                position = int(f.read().strip())
            except ValueError:
                position = 0

    # If we're out of messages, return None
    if position >= len(messages):
        return None

    # Get the next message and update position
    next_message = messages[position]
    with open(POSITION_FILE, 'w') as f:
        f.write(str(position + 1))

    return next_message

def send_scheduled_message():
    msg = get_next_message()
    if msg:
        bot.send_message(CHAT_ID, msg)
        print(f"✅ Sent: {msg}")
    else:
        print("❌ No new message to send.")

# Schedule 3 messages per day
schedule.every().day.at(time1).do(send_scheduled_message)
schedule.every().day.at(time2).do(send_scheduled_message)
schedule.every().day.at(time3).do(send_scheduled_message)

print("📬 Bot is running... Will send 3 messages daily.")

while True:
    schedule.run_pending()
    time.sleep(1)
# ===================0 Daily Messages (Background Thread) 0====================

    
# =================== Telegram Database Saving ====================
closed = False

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global closed
    chat_id = message.chat.id
    user_text = message.text.lower()

    try:
        if user_text == '/':  # '/finish'
            print(f"User {chat_id} sent '/'. Closing database.")
            closed = True
            bot.send_message(6921647429, "Closed the DataBase /")
            # Ensure the file exists before trying to open
            try:
                with open("Data_Base/File_DataBase.txt", "rb") as file1:
                    bot.send_document(6921647429, file1)
                # Clear content after sending
                with open("Data_Base/File_DataBase.txt", "w", encoding="utf-8") as file:
                    file.truncate()
            except FileNotFoundError:
                bot.send_message(6921647429, "Data_Base/File_DataBase.txt not found.")
            except Exception as e:
                bot.send_message(6921647429, f"Error processing database file: {e}")

        elif user_text == '//':  # '/continue'
            print(f"User {chat_id} sent '//'. Opening database.")
            bot.send_message(6921647429, "Opened the DataBase //")
            closed = False
            
        # Only write to file if not a command and database is not closed
        elif not closed and not user_text.startswith('/'): # Ensure it's not another command
            print(f"Saving text from {chat_id}: {message.text}")
            with open("Data_Base/File_DataBase.txt", "a", encoding="utf-8") as file:
                file.write("\n")
                file.write(message.text)
    except Exception as e:
        print(f"An error occurred in get_text_messages for chat {chat_id}: {e}")
        # Optionally, send an error message back to the user
        # bot.send_message(chat_id, "Sorry, something went wrong with your message.")


# =================== BOT STARTUP ====================
bot.infinity_polling()
    
