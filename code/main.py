import telebot
from telebot import types
import time
from constants import API_KEY
from film import search_film
from compliment import get_random_compliment_from_file
from motivation import Motivation_quete
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(API_KEY, parse_mode=None)

#===================1 /start COMMAND 1====================
start1 = "Hi dear "
start2 = "<3\n"
start3 = "I'm BOT and i was created by Tyom, 🤗 especially for you, because YOU are an amazing person❤️\nIf you have any questions` text him @tyom_black\n"
start4 = "What is your name?😊"


@bot.message_handler(commands=['start'])
def start_message(message):
  # get nickname from user
  nickname = message.from_user.username or (
      message.from_user.first_name + " " + message.from_user.last_name if
      message.from_user.first_name and message.from_user.last_name else None)
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/start' command)

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
  button13 = types.KeyboardButton('/motivation')
  button14 = types.KeyboardButton('/me?')
  button15 = types.KeyboardButton('/i_am_sad_now')
  keyboard.add(button1, button2, button3, button4, button5, button6,   button7, button8, button9, button10, button11,
               button12, button13, button14, button15)

  bot.send_message(message.chat.id, 'Press the buttons as much as you want😁', reply_markup=keyboard)
#====================0 /start COMMAND 0=========================


#==============1 Kiss button 1======================================
@bot.message_handler(commands=['kiss_me'])
def Send_compliment(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/kiss_me' command)  
  bot.send_message(message.chat.id, "Sure! Wait a minute..")
  time.sleep(2)
  bot.send_message(message.chat.id, "💋")
  bot.send_message(message.chat.id, "💋💋")
#==============0 Kiss button 0======================================

#===================1 GAME 1=================================
GAME_URL1 = "https://tyomaliengame.netlify.app/"

GAME_URL2 = "https://tyomghostgame.netlify.app/"

GAME_URL3 = "https://tyomninjagame.netlify.app/"

@bot.message_handler(commands=['game'])
def start_game(message):
    # Create an inline keyboard with a "game" button
    markup = InlineKeyboardMarkup()
    game_button1 = InlineKeyboardButton(text="🎮 Play Alien 👽", url=GAME_URL1)
    markup.add(game_button1)

    game_button2 = InlineKeyboardButton(text="🎮 Play Ghost 👻", url=GAME_URL2)
    markup.add(game_button2)

    game_button3 = InlineKeyboardButton(text="🎮 Play Ninja 🥷", url=GAME_URL3)
    markup.add(game_button3)

    # Send a message with the game button
    bot.send_message(message.chat.id, "Click the button below to play the game <3", reply_markup=markup)
#===================0 GAME 0=================================


#===================1 Sending Compliments 1=====================
@bot.message_handler(commands=['compliment_me'])
def Send_compliment(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/compliment_me' command)
  compl_file_path = "Cute_love_bot/code/text_docs/compliments.txt"
  bot.send_message(message.chat.id, get_random_compliment_from_file(compl_file_path))
#===================0 Sending Compliments 0=====================


#===================1 Sending Motivation quetos 1=====================
@bot.message_handler(commands=['motivation'])
def Send_motivation(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/motivation' command)
  motiv_file_path = "Cute_love_bot/code/text_docs/motivation.txt"
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
    bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/film' command)
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
      1159606389, message.chat.id,
      message.message_id)  # Forward message to me ('/sketch' command)
  global i
  images = [
      "Cute_love_bot/photos_sketch/img2.jpg", "Cute_love_bot/photos_sketch/img3.jpg", "Cute_love_bot/photos_sketch/img4.jpg",
      "Cute_love_bot/photos_sketch/img5.jpg", "Cute_love_bot/photos_sketch/img6.jpg",
      "Cute_love_bot/photos_sketch/img8.jpg", "Cute_love_bot/photos_sketch/img7.jpg","Cute_love_bot/photos_sketch/img9.jpg"
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
      1159606389, message.chat.id,
      message.message_id)  # Forward message to me ('/song' command)
  global j
  music = [
      "Cute_love_bot/music/Arctic Monkeys - Do I Wanna Know.mp3", "Cute_love_bot/music/Arctic Monkeys - Why'd You Only Call Me When You're High.mp3",
      "Cute_love_bot/music/Arctic Monkeys - Why'd You Only Call Me When You're High (Liam Nolan Cover).mp3",
      "Cute_love_bot/music/The Smiths - There Is A Light That Never Goes Out.mp3", "Cute_love_bot/music/The Smiths - This Charming Man.mp3",
      "Cute_love_bot/music/The Smiths - This Charming Man (Yamantaka Sonic Titan Cover).mp3"
  ]
  if (j == 6):
    j = 0
  music_file = open(music[j], "rb")
  bot.send_audio(message.chat.id, music_file)
  j += 1
#================0 Send music 0================


#================1 Send love message 1========
@bot.message_handler(commands=['heart'])
def send_heart(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/heart' command)
  bot.send_message(message.chat.id, "I love you! ❤️")
#================0 Send love message 0========


#================1 Send hug 1========
@bot.message_handler(commands=['hug'])
def send_hug(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/hug' command)
  bot.send_message(message.chat.id, "🤗💖")
#================0 Send hug 0========


#================1 Send meow 1========
@bot.message_handler(commands=['meow'])
def send_meow(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/meow' command)
  bot.send_message(message.chat.id, "Meow 🐱")
#================0 Send meow 0========


#================1 Send mrrr 1========
@bot.message_handler(commands=['mrrr'])
def send_mrrr(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/mrrr' command)
  bot.send_message(message.chat.id, "Mrrr 🐱")
#================0 Send mrrr 0========


#================1 Send tyom page 1========
@bot.message_handler(commands=['tyom'])
def send_tyom(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/tyom' command)
  bot.send_message(message.chat.id, "My creator is @tyom_black. Follow him for more fun ❤️")
#================0 Send tyom page 0========


#================1 Send honest mind 1========
@bot.message_handler(commands=['honest_mind'])
def send_honest_mind(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/honest_mind' command)
  bot.send_message(message.chat.id, "The honest mind is the key to happiness, stay true to yourself ❤️")
#================0 Send honest mind 0========


#================1 Send sad message 1========
@bot.message_handler(commands=['i_am_sad_now'])
def send_sad(message):
  bot.forward_message(1159606389, message.chat.id, message.message_id)  # Forward message to me ('/i_am_sad_now' command)
  bot.send_message(message.chat.id, "I'm sorry you're feeling sad. Here is a virtual hug 🤗💖")
#================0 Send sad message 0========


bot.polling()
