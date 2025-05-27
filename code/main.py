import telebot
from telebot import types
import time
from constants import API_KEY
from film import search_film
from compliment import get_random_compliment_from_file
from motivation import Motivation_quete
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading
import random
import datetime
from zoneinfo import ZoneInfo
import time as time_module
import pytz
import time as time_module
from datetime import datetime, timedelta, time

bot = telebot.TeleBot(API_KEY, parse_mode=None)

#===================1 /start COMMAND 1====================
start1 = "Hi dear "
start2 = "<3\n"
start3 = "I'm BOT and i was created by Tyom, 🤗 especially for you, because YOU are an amazing person❤️\nIf you have any questions` text him @tyomxxx\n"
start4 = "What is your name?😊"


@bot.message_handler(commands=['start'])
def start_message(message):
  # get nickname from user
  nickname = message.from_user.username or (
      message.from_user.first_name + " " + message.from_user.last_name if
      message.from_user.first_name and message.from_user.last_name else None)
  bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/start' command)

  if (nickname):
    bot.send_message(message.chat.id, start1 + nickname + start2 + start3)
  else:
    ask_user(message)

  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('/sketch')
  button2 = types.KeyboardButton('/song')
  button3 = types.KeyboardButton('/tyom')
  button4 = types.KeyboardButton('/honest_mind')
  button5 = types.KeyboardButton('/game')
  button6 = types.KeyboardButton('/heart')
  button7 = types.KeyboardButton('/hug')
  button8 = types.KeyboardButton('/meow')
  button9 = types.KeyboardButton('/mrrr')
  button10 = types.KeyboardButton('/kiss_me')
  button11 = types.KeyboardButton('/film')
  button12 = types.KeyboardButton('/compliment_me')
  button13 = types.KeyboardButton('/me?')
  button14 = types.KeyboardButton('/motivation')
  button15 = types.KeyboardButton('/i_am_sad_now')
  button16 = types.KeyboardButton('/Hiyori_song')
  keyboard.add(button1, button2, button3, button4, button5, button6,   button7, button8, button9, button10, button11,
               button12, button13, button14, button15, button16)

  bot.send_message(message.chat.id, 'Press the buttons as much as you want😁', reply_markup=keyboard)
  

#====================0 /start COMMAND 0=========================


#==============1 Kiss button 1======================================
@bot.message_handler(commands=['kiss_me'])
def Send_kiss(message):
  bot.forward_message( 6921647429, message.chat.id, message.message_id)  # Forward message to me ('/kiss_me' command)  
  bot.send_message(message.chat.id, "Sure! Wait a minute..")
  time.sleep(2)
  bot.send_message(message.chat.id, "💋")
  bot.send_message(message.chat.id, "💋💋")
#==============0 Kiss button 0======================================

#===================1 GAME 1=================================
GAME_URL1 = "https://tyomaliengame.netlify.app/"

GAME_URL2 = "https://doancongbang1991.github.io/mobileapp/mobile/darkninja/"

GAME_URL3 = "https://doancongbang1991.github.io/mobileapp/mobile/stickygoo/"

GAME_URL4 = "https://doancongbang1991.github.io/mobileapp/mobile/blackbats/"

GAME_URL5 = "https://doancongbang1991.github.io/mobileapp/mobile/evilwyrm/"

@bot.message_handler(commands=['game'])
def start_game(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/game' command)
    # Create an inline keyboard with a "game" button
    markup = InlineKeyboardMarkup()
    game_button1 = InlineKeyboardButton(text="👽 Play Alien 👽", url=GAME_URL1)
    markup.add(game_button1)

    game_button2 = InlineKeyboardButton(text="🥷 Play Dark Ninja 🥷", url=GAME_URL2)
    markup.add(game_button2)

    game_button3 = InlineKeyboardButton(text="🔥🐉 Play Evil Dragon 🐉🔥", url=GAME_URL3)
    markup.add(game_button3)

    game_button4 = InlineKeyboardButton(text="🍥 Play Sticky Goo 🍥", url=GAME_URL4)
    markup.add(game_button4)

    game_button5 = InlineKeyboardButton(text="🦇 Play Black Bats 🦇", url=GAME_URL5)
    markup.add(game_button5)



    # Send a message with the game button
    bot.send_message(message.chat.id, "Click the button below to play the game <3", reply_markup=markup)
#===================0 GAME 0=================================


#===================1 Sending Compliments 1=====================
@bot.message_handler(commands=['compliment_me'])
def Send_compliment(message):
  bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/compliment_me' command)
  compl_file_path = "code/text_docs/compliments.txt"
  bot.send_message(message.chat.id, get_random_compliment_from_file(compl_file_path))
#===================0 Sending Compliments 0=====================


#===================1 Sending Motivation quetos 1=====================
@bot.message_handler(commands=['motivation'])
def Send_motivation(message):
  bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/motivation' command)
  motiv_file_path = "code/text_docs/motivation.txt"
  bot.send_message(message.chat.id, Motivation_quete(motiv_file_path))
#===================0 Sending Motivation quetos 0=====================


#===================1 Search and send films link 1=====================
capture_user_input = False  # Flag to indicate whether to capture user input after the "/film" command
stop_loop = False  # Flag to stop the loop

@bot.message_handler(commands=['film'])
def Search_get_film(message):
    global capture_user_input, stop_loop
    capture_user_input = True
    stop_loop = False  # Reset the loop control flag
    bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/film' command)
    bot.send_message(message.chat.id, "Tell me what movie would you like to watch and I'll try to find it for you.\n(Enter Latin letter)")

@bot.message_handler(func=lambda message: capture_user_input and message.text)
def handle_captured_text(message):
    global capture_user_input, stop_loop
    user_input = message.text

    while not stop_loop:
        film_link = search_film(user_input)  # Your search_film function goes here

        if film_link:
            bot.send_message(message.chat.id, "Looks like I found the movie, enjoy)\n" + film_link)
            break
        else:
            bot.send_message(message.chat.id, "I couldn't find that movie, sorry(\nExplain another way or tell me another movie!")

            # Create buttons
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("No, thank you", callback_data="stop")
            btn2 = types.InlineKeyboardButton("Find movie", callback_data="continue")
            markup.add(btn1, btn2)

            # Send the message with buttons
            bot.send_message(message.chat.id, "Do you want to find movie?", reply_markup=markup)

            break  # Exit the loop and wait for the user's response

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global capture_user_input, stop_loop

    if call.data == "stop":
        stop_loop = True  # Stop the loop
        capture_user_input = False  # Stop capturing user input
        bot.send_message(call.message.chat.id, "Alright, maybe next time <3")

    elif call.data == "continue":
        capture_user_input = True  # Continue capturing user input
        bot.send_message(call.message.chat.id, "OK, tell me.")
#===================0 Search and send films link 0=====================


#================1 Get user's Name 1============
def ask_user(message):
  bot.send_message(message.chat.id, start4)
  bot.register_next_step_handler(message, process_name_step)

def process_name_step(message):
  name = message.text
  bot.send_message(message.chat.id, start1 + name + start2 + start3)
#================0 Get user's Name 0============


#===================1 Send sketch image 1============
i = 0

@bot.message_handler(commands=["sketch"])
def image(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/sketch' command)
  global i
  images = [
      "photos_sketch/img2.jpg", "photos_sketch/img3.jpg", "photos_sketch/img4.jpg",
      "photos_sketch/img5.jpg", "photos_sketch/img6.jpg",
      "photos_sketch/img8.jpg", "photos_sketch/img7.jpg","photos_sketch/img9.jpg"
  ]
  if (i == 8):
    i = 0
  img = open(images[i], "rb")
  bot.send_photo(message.chat.id, img)
  i += 1
#====================0 Send sketch image 0===================


#================1 Send music 1==============
j = 0

@bot.message_handler(commands=['song'])
def send_music(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/song' command)
  global j
  music = [
      "music/Arctic Monkeys - Do I Wanna Know.mp3", "music/Arctic Monkeys - Why'd You Only Call Me When You're High.mp3",
      "music/Beach House - Space Song.mp3", "music/Bring Me The Horizon - Drown.mp3", "music/Bring Me The Horizon - Ludens.mp3",
      "music/Bring Me The Horizon - Shadow Moses.mp3", "music/Bring Me The Horizon - Sleepwalking.mp3", "music/Roar - I Can’t Handle Change.mp3",
      "music/Swing - Lynn.mp3", "music/The Drums - Money.mp3", "music/Young - Vacations.mp3"
  ]
  if (j == 11):
    j = 0
  with open(music[j], 'rb') as music:
    # Send the music file
    bot.send_audio(message.chat.id, music)
    j += 1
#================0 Send music 0==============


#================1 Send video 1=================
k = 0

@bot.message_handler(commands=['i_am_sad_now'])
def send_video(message):
  bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/i_am_sad_now' command)
  bot.send_message(message.chat.id, "Wait a minute pls💞")
  global k
  videos = [
     "mem_Video/mem1.mp4", "mem_Video/mem2.mp4", "mem_Video/mem3.mp4", "mem_Video/mem4.mp4",
     "mem_Video/mem5.mp4"
  ]

  if (k == 5):
    k = 0

  with open(videos[k], 'rb') as video_file:
    bot.send_video(message.chat.id, video_file)
  bot.send_message(message.chat.id, "Don't be sad!\nit's time to smile💗\nCos your smile makes me feel alive in this shitty world💖")
  k += 1
#================0 Send video 0=================


#==============1 Sending some cute messages 1===================
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

#fall_in_love = """
#There is something in me, that's how I expressed it.
#Here is the text, everything comes from my heart..🥹
#"""

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

@bot.message_handler(commands=['tyom'])
def Cute_words(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/tyom' command)
  global i
  tyom_responce = ["ha jan❤️", "Yeah? wanna hug?🤗","shutup and kiss me💋💜","jana"]
  if i == 4:
    i = 0

  bot.send_message(message.chat.id, tyom_responce[i])
  i += 1
  

@bot.message_handler(commands=['me?'])
def saying_pretty(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/Es?' command)
  bot.send_message(message.chat.id, cute1)


@bot.message_handler(commands=['heart'])
def giving_heart(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/heart' command)
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
  for i in range(7):
    bot.send_message(message.chat.id, heart)
  time.sleep(0.20)
  for i in range(7):
    bot.send_message(message.chat.id, heart1)
  for i in range(20):
    bot.send_message(message.chat.id, love_you)
  bot.send_message(message.chat.id, heart1)
#==============0 Sending some cute messages 0===================


#==============1 Sending hug GIF 1===================
@bot.message_handler(commands=['hug'])
def sending_hug(message):
  bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward message to me ('/hug' command)

  global i
  lst1 = [
        "hug_GIF/hug1.mp4", "hug_GIF/hug2.mp4", "hug_GIF/hug3.mp4",
        "hug_GIF/hug4.mp4", "hug_GIF/hug5.mp4"
  ]

  if (i == 5):
    i = 0
  with open(lst1[i], 'rb') as gif_file:
    bot.send_animation(message.chat.id, gif_file)
  i += 1
#==============0 Sending hug GIF 0===================


#=================1 Saying ILY with song 1==================
@bot.message_handler(commands=['honest_mind'])
def Fall_in_love(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/honest_mind' command)
  bot.send_message(message.chat.id, fall_in_love)
  with open("ily_song/tyom black - I.L.U.mp3", 'rb') as music:
    bot.send_audio(message.chat.id, music)
  bot.send_message(message.chat.id, love_text)
#=================0 Saying ILY with song 0==================


#=================1 Sending our song 1======================
@bot.message_handler(commands=['Hiyori_song'])
def Our_song(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/our_song' command)
  with open("song for isvira/tyom black - I wanna Be Yours.mp3", 'rb') as music:
    bot.send_audio(message.chat.id, music)
  bot.send_message(message.chat.id, i_wanna_be_yours_text)
  bot.send_message(message.chat.id, "You deserve this song, so it's yours now💋")
#=================0 Sending our song 0======================

#==============1 saying 'meow' and send cat image 1===================
@bot.message_handler(commands=['meow'])
def Meow(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/meow' command)
  for j in range(2):
    bot.send_message(message.chat.id, text_meow)
  global i
  images = [
      "cat/cat1.jpg", "cat/cat2.jpg", "cat/cat3.jpg", "cat/cat4.jpg",
      "cat/cat5.jpg", "cat/cat6.jpg", "cat/cat7.jpg"
  ]
  if (i == 7):
    i = 0
  img = open(images[i], "rb")
  bot.send_photo(message.chat.id, img)
  i += 1
#==============0 saying 'meow' and send cat image 0===================


#==============1 saying 'mrrr' 1===================
@bot.message_handler(commands=['mrrr'])
def Mrrr(message):
  bot.forward_message(
      6921647429, message.chat.id,
      message.message_id)  # Forward message to me ('/mrrr' command)
  for i in range(10):
    bot.send_message(message.chat.id, "meow<3")
  for j in range(15):
    bot.send_message(message.chat.id, "mrrr>>>>>>>")
  for k in range(10):
    bot.send_message(message.chat.id, "❤️")
  img = open("Cute_love_bot\cat/cat8.jpg", "rb") 
  bot.send_photo(message.chat.id, img)
#==============0 saying 'mrrr' 0===================

#===================1 sending msg every day that count our meeting in december 1========================
USER_CHAT_ID = 7843995956  # Replace with your girlfriend's Telegram user ID

# === FILE SETUP ===
MESSAGE_FILE = "code/text_docs/kind_messages.txt"

# Load all messages from the file, skipping empty lines
with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
    messages = [line.strip() for line in f if line.strip()]

current_index = 0  # Index of the next message to send

# === SEND A SINGLE MESSAGE ===
def send_next_message():
    global current_index
    if current_index < len(messages):
        msg = messages[current_index]
        bot.send_message(USER_CHAT_ID, msg)
        print(f"Sent message #{current_index + 1}: {msg}")
        current_index += 1
    else:
        print("✅ All messages have been sent!")

# === DAILY MESSAGE LOGIC ===
def send_three_messages_daily():
    global current_index
    TEST_MODE = False  #✅ Set to False when you're ready for real timing

    while current_index < len(messages):
        total_delay_hours = 0
        messages_sent = 0

        while messages_sent < 3 and current_index < len(messages):
            # Check current time in Japan
            now = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
            if 2 <= now.hour < 8:
                sleep_hours = 8 - now.hour
                print(f"🌙 It's nighttime in Japan ({now.hour}:00). Sleeping {sleep_hours} hours...")
                time.sleep(sleep_hours * 3600)
                continue

            send_next_message()
            messages_sent += 1

            if TEST_MODE:
                delay_seconds = 30
                total_delay_hours += delay_seconds / 3600
                print(f"🧪 Test mode: waiting {delay_seconds} seconds before next message...")
                time.sleep(delay_seconds)
            else:
                # Divide remaining 18 hours into 3 parts = average 6h between
                delay_hours = 3 + (random.random() * 6)  # random between 3 to 9 hours
                total_delay_hours += delay_hours
                print(f"⏳ Waiting {delay_hours:.2f} hours before next message...")
                time.sleep(delay_hours * 3600)

        if not TEST_MODE:
            # Wait until next day's window opens (24h total, minus time already passed)
            now = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
            tomorrow = (now + datetime.timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
            sleep_seconds = (tomorrow - now).total_seconds()
            print(f"🌅 Waiting {sleep_seconds/3600:.2f} hours until next day's 8:00 AM JST...")
            time.sleep(sleep_seconds)
        else:
            print("🧪 Test mode: simulating 'next day' wait with 10 seconds...")
            time.sleep(10)
#===================0 sending msg every day that count our meeting in december 0========================


#==============1 Save Telegram DataBase 1================
closed = False

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

  global closed
  try:
    if message.text.lower() == '/':  # '/finish'
      print(message.text)
      closed = True
      bot.send_message(6921647429, "Closed the DataBase   /")
      with open("Data_Base/File_DataBase.txt", "rb") as file1:
        bot.send_document(6921647429, file1)
      with open("Data_Base/File_DataBase.txt", "w") as file:  # for delete file content
        file.truncate()  # for delete file content
  except:
    print("huzich a")
    
  if message.text.lower() == '//':  # '/continue'
    bot.send_message(6921647429, "Opend the DataBase  //")
    closed = False

  elif message.text.lower() != '' and not closed:
    print(message.text)
    with open("Data_Base/File_DataBase.txt", "a", encoding="utf-8") as file:
      file.write("\n")
      file.write(message.text)
#===============0 Save Telegram DataBase 0================


# threading.Thread(target=send_three_messages_daily, daemon=True).start()
bot.infinity_polling()"



