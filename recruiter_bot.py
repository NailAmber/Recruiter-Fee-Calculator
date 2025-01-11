from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from db_functions import calculate_payment, get_all_clients, add_client, update_client_formula, delete_client
import os
import re
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Получение токена и доверенных пользователей из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TRUSTED_USERS = os.getenv("TRUSTED_USERS")
TRUSTED_USERS = [int(user_id) for user_id in TRUSTED_USERS.split(",")]

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Здравствуйте! Используйте:\n\n/calculate для расчета платежей,\n/list_clients для вывода формул клиентов,\n/add_client для добавления нового клиента,\n/update_client для обновления формулы клиента,\n/delete_client для удаления клиента.')

async def calculate(update: Update, context: CallbackContext) -> None:
    clients = get_all_clients()
    if not clients:
        await update.message.reply_text("Нет доступных клиентов.")
        return

    client_list = "\n".join([f"{i + 1}. {client[1]}" for i, client in enumerate(clients)])
    await update.message.reply_text(f"Выберите клиента:\n{client_list}\n\nОтветьте номером клиента и суммой (например, '1 10000').")

def restricted(func):
    async def wrapped(update: Update, context: CallbackContext, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in TRUSTED_USERS:
            await update.message.reply_text("У вас нет доступа к этой команде.")
            return
        return await func(update, context, *args, **kwargs)
    return wrapped

@restricted
async def add_client_command(update: Update, context: CallbackContext) -> None:
    try:
        # Используем регулярное выражение для извлечения названия клиента и формулы
        pattern = r'\"(.+?)\"\s+\"(.+?)\"'
        match = re.search(pattern, update.message.text)

        if match:
            client_name = match.group(1)
            formula = match.group(2)
            add_client(client_name, formula)
            await update.message.reply_text(f"Клиент \"{client_name}\" с формулой \"{formula}\" добавлен.")
        else:
            raise IndexError

    except IndexError:
        await update.message.reply_text("Пожалуйста, укажите название клиента и формулу в кавычках. Пример: /add_client \"Банк Абоба\" \"amount * 12 + 4\"")

@restricted
async def update_client_command(update: Update, context: CallbackContext) -> None:
    try:
        pattern = r'\"(.+?)\"\s+\"(.+?)\"'
        match = re.search(pattern, update.message.text)

        if match:
            client_name = match.group(1)
            new_formula = match.group(2)

            if update_client_formula(client_name, new_formula):
                await update.message.reply_text(f"Формула для клиента \"{client_name}\" обновлена на \"{new_formula}\".")
            else:
                await update.message.reply_text(f"Клиент \"{client_name}\" не найден.")
        else:
            raise IndexError

    except IndexError:
        await update.message.reply_text("Пожалуйста, укажите название клиента и новую формулу в кавычках. Пример: /update_client \"Банк Абоба\" \"amount * 12 / 4\"")
        await show_list_clients(update)

@restricted
async def delete_client_command(update: Update, context: CallbackContext) -> None:
    try:
        pattern = r'\"(.+?)\"'
        match = re.search(pattern, update.message.text)

        if match:
            client_name = match.group(1)
            if delete_client(client_name):
                await update.message.reply_text(f"Клиент \"{client_name}\" удален.")
            else:
                await update.message.reply_text(f"Клиент \"{client_name}\" не найден.")
        else:
            raise IndexError

    except IndexError:
        await update.message.reply_text("Пожалуйста, укажите название клиента в кавычках. Пример: /delete_client \"Банк Абоба\"")
        await show_list_clients(update)

# Команда для вывода списка клиентов с их формулами

async def show_list_clients(update: Update):
    clients = get_all_clients()
    if not clients:
        await update.message.reply_text("Нет доступных клиентов.")
        return

    client_list = "\n".join([f"\"{client[1]}\": \t{client[2]}" for client in clients])
    await update.message.reply_text(f"Список клиентов и их формул:\n\n{client_list}")


async def list_clients_command(update: Update, context: CallbackContext) -> None:
    await show_list_clients(update)

async def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        msg = update.message.text.split()
        client_num = int(msg[0]) - 1
        amount = float(msg[1])

        clients = get_all_clients()
        if 0 <= client_num < len(clients):
            client_name = clients[client_num][1]
            payment, formula = calculate_payment(client_name, amount)
            if payment is not None:
                await update.message.reply_text(f"Платеж для {client_name} (формула: '{formula}') на сумму {amount} составляет {payment}.")
            else:
                await update.message.reply_text(f"Не удалось рассчитать платеж для {client_name}. Проверьте данные.")
        else:
            await update.message.reply_text("Неверный номер клиента.")
    except (IndexError, ValueError):
        await update.message.reply_text("Неверный ввод. Пожалуйста, укажите номер клиента и сумму (например, '1 10000').")

def main():
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("calculate", calculate))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CommandHandler("add_client", add_client_command))
    application.add_handler(CommandHandler("update_client", update_client_command))
    application.add_handler(CommandHandler("delete_client", delete_client_command))
    application.add_handler(CommandHandler("list_clients", list_clients_command))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
