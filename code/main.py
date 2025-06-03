import telebot
from telebot import types
import time
import random
from zoneinfo import ZoneInfo  # For timezones if you use them later

from constants import API_KEY
from film import search_film
from compliment import get_random_compliment_from_file
from motivation import Motivation_quete

bot = telebot.TeleBot(API_KEY, parse_mode=None)

# =================== GLOBAL TEXTS ====================
start1 = "Hi dear "
start2 = "<3\n"
start3 = ("I'm BOT and I was created by Tyom, 🤗 especially for you, because YOU are an amazing person❤️\n"
          "If you have any questions, text him @tyomxxx\n")
start4 = "What is your name?😊"

GAME_URLS = [
    ("👽 Play Alien 👽", "https://tyomaliengame.netlify.app/"),
    ("🥷 Play Dark Ninja 🥷", "https://doancongbang1991.github.io/mobileapp/mobile/darkninja/"),
    ("🔥🐉 Play Evil Dragon 🐉🔥", "https://doancongbang1991.github.io/mobileapp/mobile/stickygoo/"),
    ("🍥 Play Sticky Goo 🍥", "https://doancongbang1991.github.io/mobileapp/mobile/blackbats/"),
    ("🦇 Play Black Bats 🦇", "https://doancongbang1991.github.io/mobileapp/mobile/evilwyrm/")
]

# Cute messages
tyom_responses_data = {}

# =================== /start COMMAND ====================
@bot.message_handler(commands=['start'])
def start_message(message):
    nickname = (message.from_user.username or
                (f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.first_name and message.from_user.last_name else None))
    bot.forward_message(6921647429, message.chat.id, message.message_id)  # Forward to admin

    if nickname:
        bot.send_message(message.chat.id, f"{start1}{nickname}{start2}{start3}")
    else:
        ask_user(message)

    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [
        '/sketch', '/song', '/tyom', '/honest_mind', '/game', '/heart',
        '/hug', '/meow', '/mrrr', '/kiss_me', '/film', '/compliment_me',
        '/me?', '/motivation', '/i_am_sad_now', '/Hiyori_song'
    ]
    keyboard.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, 'Press the buttons as much as you want 😁', reply_markup=keyboard)


# =================== kiss_me COMMAND ====================
@bot.message_handler(commands=['kiss_me'])
def send_kiss(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Sure! Wait a minute..")
    time.sleep(2)
    bot.send_message(message.chat.id, "💋")
    bot.send_message(message.chat.id, "💋💋")


# =================== game COMMAND ====================
@bot.message_handler(commands=['game'])
def start_game(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    markup = types.InlineKeyboardMarkup()
    for text, url in GAME_URLS:
        markup.add(types.InlineKeyboardButton(text=text, url=url))
    bot.send_message(message.chat.id, "Click the button below to play the game <3", reply_markup=markup)


# =================== compliment_me COMMAND ====================
@bot.message_handler(commands=['compliment_me'])
def send_compliment(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    compliment_file = "code/text_docs/compliments.txt"
    compliment = get_random_compliment_from_file(compliment_file)
    bot.send_message(message.chat.id, compliment)


# =================== motivation COMMAND ====================
@bot.message_handler(commands=['motivation'])
def send_motivation(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    motivation_file = "code/text_docs/motivation.txt"
    quote = Motivation_quete(motivation_file)
    bot.send_message(message.chat.id, quote)


# =================== film COMMAND ====================
@bot.message_handler(commands=['film'])
def search_get_film(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Tell me what movie you'd like to watch and I'll try to find it for you.\n(Please enter in Latin letters)")
    bot.register_next_step_handler(message, process_film_request)


def process_film_request(message):
    user_input = message.text
    film_link = search_film(user_input)

    if film_link:
        bot.send_message(message.chat.id, "Looks like I found the movie, enjoy! 🎬\n" + film_link)
    else:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("No, thank you", callback_data="stop_film_search")
        btn2 = types.InlineKeyboardButton("Find another movie", callback_data="continue_film_search")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Sorry, I couldn't find that movie 😞\nTry explaining differently or name another movie.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["stop_film_search", "continue_film_search"])
def callback_query_film_search(call):
    if call.data == "stop_film_search":
        bot.send_message(call.message.chat.id, "Alright, maybe next time <3")
    elif call.data == "continue_film_search":
        bot.send_message(call.message.chat.id, "OK, tell me the movie title again.")
        bot.register_next_step_handler(call.message, process_film_request)
    bot.answer_callback_query(call.id)


# =================== Ask for user name if not provided ====================
def ask_user(message):
    bot.send_message(message.chat.id, start4)
    bot.register_next_step_handler(message, process_name_step)


def process_name_step(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, f"{start1}{name}{start2}{start3}")


# =================== sketch COMMAND ====================
@bot.message_handler(commands=["sketch"])
def send_sketch(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    images = [
        "photos_sketch/img2.jpg", "photos_sketch/img3.jpg", "photos_sketch/img4.jpg",
        "photos_sketch/img5.jpg", "photos_sketch/img6.jpg", "photos_sketch/img8.jpg",
        "photos_sketch/img7.jpg", "photos_sketch/img9.jpg"
    ]
    img_path = random.choice(images)
    with open(img_path, "rb") as img_file:
        bot.send_photo(message.chat.id, img_file)


# =================== song COMMAND ====================
@bot.message_handler(commands=['song'])
def send_music(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    music_files = [
        "music/Arctic Monkeys - Do I Wanna Know.mp3",
        "music/Arctic Monkeys - Why'd You Only Call Me When You're High.mp3",
        "music/Beach House - Space Song.mp3",
        "music/Bring Me The Horizon - Drown.mp3",
        "music/Bring Me The Horizon - Ludens.mp3",
        "music/Bring Me The Horizon - Shadow Moses.mp3",
        "music/Bring Me The Horizon - Sleepwalking.mp3",
        "music/Roar - I Can’t Handle Change.mp3",
        "music/Swing - Lynn.mp3",
        "music/The Drums - Money.mp3",
        "music/Young - Vacations.mp3"
    ]
    selected_music = random.choice(music_files)
    with open(selected_music, 'rb') as music_file:
        bot.send_audio(message.chat.id, music_file)


# =================== i_am_sad_now COMMAND ====================
@bot.message_handler(commands=['i_am_sad_now'])
def send_video(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Wait a minute pls💞")
    videos = [
        "mem_Video/mem1.mp4", "mem_Video/mem2.mp4", "mem_Video/mem3.mp4",
        "mem_Video/mem4.mp4", "mem_Video/mem5.mp4"
    ]
    selected_video = random.choice(videos)
    with open(selected_video, 'rb') as video_file:
        bot.send_video(message.chat.id, video_file)
    bot.send_message(message.chat.id, "Don't be sad!\nIt's time to smile💗\n'Cause your smile makes me feel alive in this shitty world💖")


# =================== tyom COMMAND ====================
@bot.message_handler(commands=['tyom'])
def cute_words(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    tyom_responses = ["ha jan❤️", "Yeah? wanna hug?🤗", "shutup and kiss me💋💜", "jana"]

    chat_id = message.chat.id
    current_count = tyom_responses_data.get(chat_id, 0)
    if current_count >= len(tyom_responses):
        tyom_responses_data[chat_id] = 0
    else:
        tyom_responses_data[chat_id] = current_count + 1

    response = tyom_responses[current_count]
    bot.send_message(chat_id, response)


# =================== heart COMMAND ====================
@bot.message_handler(commands=['heart'])
def heart_command(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hey..you are important to me❤")
    time.sleep(3)
    bot.send_message(chat_id, "I just wanted to tell you this..")
    time.sleep(3)
    bot.send_message(chat_id, "Don't forget that")
    time.sleep(4)
    bot.send_message(chat_id, "You are not alone")
    time.sleep(4)
    bot.send_message(chat_id, "You're never alone")


# =================== hug COMMAND ====================
@bot.message_handler(commands=['hug'])
def send_hug(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "🤗")


# =================== me? COMMAND ====================
@bot.message_handler(commands=['me?'])
def send_me(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "You are so sweet💞")


# =================== meow COMMAND ====================
@bot.message_handler(commands=['meow'])
def send_meow(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Meow🐱")


# =================== mrrr COMMAND ====================
@bot.message_handler(commands=['mrrr'])
def send_mrrr(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Mrrr🐱")


# =================== Hiyori_song COMMAND ====================
@bot.message_handler(commands=['Hiyori_song'])
def send_hiyori_song(message):
    bot.forward_message(6921647429, message.chat.id, message.message_id)
    hiyori_song = "https://music.youtube.com/watch?v=TF17FpnOypQ&list=RDAMVMTF17FpnOypQ"
    bot.send_message(message.chat.id, f"Here's a nice song for you:\n{hiyori_song}")


if __name__ == '__main__':
    print('Bot started')
    bot.infinity_polling()
