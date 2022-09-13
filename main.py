import os
import telebot
from dotenv import load_dotenv

load_dotenv()

data_jadwal_1 = {
  "Senin": [["5-6", "Struktur Data Teori", "online"], ["7-8", "Statmat 2", "online"]],
  "Selasa" : [["3-4", "SIG Teori", "offline"], ["5-6", "Metstat 2 Teori", "online"], ["7-8", "Basis Data Teori", "online"]],
  "Rabu" : [["1-2", "Struktur Data Prak", "offline"], ["4-6", "MPS", "Offline"]],
  "Kamis" : [["1-2", "Mestat 2 Prak", "Online"], ["3-4", "Basis Data Prak", "Offline"], ["7-8", "SIG Prak", "Offline"]],
  "Jumat" : [["1-2", "PKN", "Offline"]]
}

data_jadwal_2 = {
  "Senin": [["5-6", "Struktur Data Teori", "offline"], ["7-8", "Statmat 2", "offline"]],
  "Selasa" : [["3-4", "SIG Teori", "online"], ["5-6", "Metstat 2 Teori", "offline"], ["7-8", "Basis Data Teori", "offline"]],
  "Rabu" : [["1-2", "Struktur Data Prak", "online"], ["4-6", "MPS", "Online"]],
  "Kamis" : [["1-2", "Mestat 2 Prak", "Offline"], ["3-4", "Basis Data Prak", "Online"], ["7-8", "SIG Prak", "Online"]],
  "Jumat" : [["1-2", "PKN", "Online"]]
}

api_token = os.getenv("API_TOKEN");
bot = telebot.TeleBot(api_token)


# /cek senin 2
@bot.message_handler(commands=["cek"])
def cek_jadwal(message) :
  text = message.text.split(' ')[1:]
  if len(text) == 2:
    hari = text[0]
    minggu = text[1]
  
    if int(minggu) % 2 == 0 :
      tipe_jadwal = data_jadwal_2
    else :
      tipe_jadwal = data_jadwal_1

    for key,value in tipe_jadwal.items() :
      if key.lower() == hari.lower() :
        for i in value :
          bot.reply_to(message, text=f'\n Jam ke: {i[0]} \n Matkul: {i[1]} \n Tipe: {i[2]}')
  else :
    bot.reply_to(message, text="Masukkan inputan sesuai petunjuk!")
    

@bot.message_handler(commands=['help'])
def send_help(message):
  bot.reply_to(message, 'Silahkan tuliskan jadwal hari yang ingin di cek. Untuk mengecek jadwal bisa dengan mengetikkan: /cek <spasi> hari <spasi> minggu ke-. Contoh: /cek senin 2')

@bot.message_handler(commands=["start"])
def start_bot(message):
  username = message.from_user.username
  
  bot.reply_to(message, f'Hi {username} Jumpa lagi 🖐.')

print('bot is running ... ')
bot.polling()

