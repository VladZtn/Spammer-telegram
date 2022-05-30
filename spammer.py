from pyrogram import Client, filters
import time

api_id = 18370524
api_hash = "1e3693002c2d99186dd721204ac516c5"

app = Client('my_account', api_id=api_id, api_hash=api_hash)

print('SPAMMER BY VLADOSSIK')

repeat_range = int(input('Введіть кількість повторів: '))
speed_range = int(input('Выберите режим скорости(1 - быстро, 2 - средняя скорость, 3 - медленно): '))
repeat_range += 1

if speed_range == 1:
    speed_range = 0
    
elif speed_range == 2:
    speed_range = 0.2

elif speed_range == 3:
    speed_range = 0.5

else:
    print('Введите скорость')

    exit()

@app.on_message(filters.me)

async def echo(client, message):
    
    print('Спам отправлен by Vladossik')
    for i in range(0, repeat_range):
        await message.reply_text(message.text)
        time.sleep(speed_range)
        

app.run()
