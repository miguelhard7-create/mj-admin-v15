import telebot
import json
import random
import string
import os

# CONFIGURAÇÕES
TOKEN = "8793020623:AAF07ri4q_X3TjJQxn3z0zxRQ9owh_TH7MM"
bot = telebot.TeleBot(TOKEN)
DB_FILE = "banco_dados.json"

# Carregar ou criar banco de dados
def carregar_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return []

def salvar_db(dados):
    with open(DB_FILE, 'w') as f:
        json.dump(dados, f, indent=4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = (
        "🚀 *AUXÍLIO VIP MJ - GERADOR*\n\n"
        "Comandos disponíveis:\n"
        "/gerar [nome] - Cria uma key de 24h\n"
        "/status - Ver estatísticas do painel"
    )
    bot.reply_to(message, msg, parse_mode="Markdown")

@bot.message_handler(commands=['gerar'])
def comando_gerar(message):
    args = message.text.split()
    nome = args[1] if len(args) > 1 else "USER"
    
    # Criar Key
    nova_key = "MJ-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    validade = 24 * 60 * 60 * 1000 # 24 horas em ms
    
    db = carregar_db()
    db.append({
        "key": nova_key,
        "owner": nome,
        "status": "Ativa",
        "validade": 9999999999999, # Para teste inicial como vitalício ou use timestamp
        "duracao": validade
    })
    salvar_db(db)
    
    bot.reply_to(message, f"✅ *KEY GERADA!*\n\n👤 Nome: {nome}\n🔑 Key: `{nova_key}`\n⏳ Validade: 24 Horas")

print("🤖 Bot MJ Online...")
bot.infinity_polling()

