import asyncio
import random
import math
from datetime import datetime, timedelta
import pytz
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton

# 🎯 Konfigurasi Bot
BOT_TOKEN = "8581548235:AAFAOEMOmfsDGdogbN6aHTcqdsQtgaZSDm8"  # Ganti dengan token kamu
LINK_URL = "https://t.me/asdassadher314"
IMAGE_PATH = r"D:\WORK PROGRAM\POP\\"  # Pastikan path ini sesuai

# 🎯 Inisialisasi Bot
bot = Bot(token=BOT_TOKEN)
SAO_PAULO_TZ = pytz.timezone("America/Sao_Paulo")  # Zona waktu São Paulo

# ==========================================
# RTP SYSTEM ALGORITHM (PORTED FROM WEBSITE)
# ==========================================

CONFIG = {
    "rtp_min": 30,
    "rtp_max": 99,
    "normal_min": 2,
    "normal_max": 15,
    "auto_options": [10, 30, 50, 80],
    "turbo_options": ["𝐀𝐭𝐢𝐯𝐨", "𝗗𝗲𝘀𝗮𝘁𝗶𝘃𝗮𝗱𝗼"]
}

def js_string_to_hash(s):
    hash_val = 0
    for char in s:
        char_code = ord(char)
        hash_val = (hash_val * 31 + char_code) & 0xFFFFFFFF
    
    if hash_val > 0x7FFFFFFF:
        hash_val -= 0x100000000
    return abs(hash_val)

def get_time_seed():
    now = datetime.now(SAO_PAULO_TZ)
    rounded_minute = (now.minute // 3) * 3
    # JS getMonth() is 0-11, Python is 1-12
    month_index = now.month - 1
    
    total_minutes = (now.year * 525600 +
                     month_index * 43800 +
                     now.day * 1440 +
                     now.hour * 60 +
                     rounded_minute)
    return total_minutes

def seeded_random(seed):
    seed = int(abs(seed)) & 0xFFFFFFFF
    seed = (seed + 0x6D2B79F5) & 0xFFFFFFFF
    t = seed
    
    t_unsigned = t
    t = ( ((t_unsigned ^ (t_unsigned >> 15)) & 0xFFFFFFFF) * ((t | 1) & 0xFFFFFFFF) ) & 0xFFFFFFFF
    
    t_unsigned = t
    term2 = ( ((t_unsigned ^ (t_unsigned >> 7)) & 0xFFFFFFFF) * ((t | 61) & 0xFFFFFFFF) ) & 0xFFFFFFFF
    t = (t ^ (t + term2)) & 0xFFFFFFFF
    
    t_unsigned = t
    return ((t_unsigned ^ (t_unsigned >> 14)) & 0xFFFFFFFF) / 4294967296

def get_seeded_random_int(seed, min_val, max_val):
    seed = (seed * 9301 + 49297) % 233280
    rnd = seeded_random(seed)
    return math.floor(rnd * (max_val - min_val + 1)) + min_val

def get_seeded_choice(seed, options):
    seed = (seed * 9301 + 49297) % 233280
    rnd = seeded_random(seed)
    idx = math.floor(rnd * len(options))
    return options[idx]

def generate_game_data(game_name):
    time_seed = get_time_seed()
    game_hash = js_string_to_hash(game_name)
    
    # RTP
    seed_rtp = time_seed * 1000 + game_hash
    rtp = get_seeded_random_int(seed_rtp, CONFIG["rtp_min"], CONFIG["rtp_max"])
    
    # Normal Spins (Seed + 1000)
    seed_normal = seed_rtp + 1000
    normal = get_seeded_random_int(seed_normal, CONFIG["normal_min"], CONFIG["normal_max"])
    
    # Auto Spins (Seed + 2000)
    seed_auto = seed_rtp + 2000
    auto = get_seeded_choice(seed_auto, CONFIG["auto_options"])
    
    # Turbo (Seed + 3000)
    seed_turbo = seed_rtp + 3000
    turbo = get_seeded_choice(seed_turbo, CONFIG["turbo_options"])
    
    return rtp, normal, auto, turbo

# 🎯 Channel dan game yang berbeda
channels_games = {
    "@asdassadher314": [
        "🐝 3 Buzzing Wilds"
    ],
}

# 🎯 Fungsi untuk mengirim prediksi ke channel tertentu
async def send_prediction(channel_id, games):
    game = random.choice(games)
    image_path = f"{IMAGE_PATH}{game}.png"
    
    # Use deterministic data from website algorithm
    rtp, normal, auto, turbo = generate_game_data(game)

    now = datetime.now(SAO_PAULO_TZ)
    valid_until = now + timedelta(minutes=5)
    valid_until_str = valid_until.strftime("%H:%M")

    caption = (
        f"   {game}\n\n"
        f"📊 <b>Porcentagem (RTP):</b> {rtp}%\n\n"
        f"🎯 <b>Estratégia de Apostas:</b>\n"
        f"Normal: {normal} X\n"
        f"Auto: {auto}\n"
        f"Turbo: {turbo}\n\n"
        f"⏳ <b>Válido até:</b> {valid_until_str}\n\n"
        f"Jogue agora e ganhe!\n"
        f"Boa sorte! 🍀"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎁 BOT BÔNUS", url=LINK_URL)]
    ])

    try:
        with open(image_path, "rb") as photo:
            await bot.send_photo(
                chat_id=channel_id,
                photo=photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=keyboard
            )
        print(f"✅ Predição enviada para {channel_id}: {game} (RTP: {rtp}%)")
    except Exception as e:
        print(f"❌ Falha ao enviar para {channel_id}: {e}")

# 🎯 Fungsi utama (loop terus menerus)
async def main():
    while True:
        for channel, games in channels_games.items():
            await send_prediction(channel, games)
            await asyncio.sleep(10)  # jeda antar channel

        await asyncio.sleep(300)  # jeda 5 menit sebelum siklus berikutnya

# Jalankan
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
