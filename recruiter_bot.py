from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from db_functions import calculate_payment, get_all_clients
import os
from dotenv import load_dotenv

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Здравствуйте! Используйте /calculate для расчета платежей.')

async def calculate(update: Update, context: CallbackContext) -> None:
    clients = get_all_clients()
    if not clients:
        await update.message.reply_text("Нет доступных клиентов.")
        return

    client_list = "\n".join([f"{i + 1}. {client[1]}" for i, client in enumerate(clients)])
    await update.message.reply_text(f"Выберите клиента:\n{client_list}\n\nОтветьте номером клиента и суммой (например, '1 10000').")

async def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        msg = update.message.text.split()
        client_num = int(msg[0]) - 1
        amount = float(msg[1])

        clients = get_all_clients()
        if 0 <= client_num < len(clients):
            client_name = clients[client_num][1]
            payment,formula = calculate_payment(client_name, amount)
            if payment is not None:
                await update.message.reply_text(f"Платеж для {client_name} (формула: '{formula}') на сумму {amount} составляет {payment}.")
            else:
                await update.message.reply_text(f"Не удалось рассчитать платеж для {client_name}. Проверьте данные.")
        else:
            await update.message.reply_text("Неверный номер клиента.")
    except (IndexError, ValueError):
        await update.message.reply_text("Неверный ввод. Пожалуйста, укажите номер клиента и сумму (например, '1 10000').")

def main():
    # Загрузка переменных окружения из файла .env
    load_dotenv()

    # Получение токена из переменной окружения
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("calculate", calculate))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
