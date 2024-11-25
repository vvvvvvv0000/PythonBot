#7757066965:AAH5ud-dxH5efI70xQZihC2bOJYiiAS47r0
"""

from telegram.ext import Application, CommandHandler, MessageHandler, filters
async def start(update,context):

async def echo(update, context):
    await update.message.reply_text(update.message.text)
def main():
    application = Application.builder().token('7757066965:AAH5ud-dxH5efI70xQZihC2bOJYiiAS47r0').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()
if __name__ == '__main__':
    main()

"""
from lib2to3.btm_utils import TYPE_GROUP

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler

app = ApplicationBuilder().token('7757066965:AAH5ud-dxH5efI70xQZihC2bOJYiiAS47r0').build()
async def start_command(update, context):
    welcome_text = (
        "Добро пожаловать в салон красоты  'Айлен'\n"
        "Я помогу вам с информацией о наших услугах.\n"
        "Попробуйте наши следующие команды:\n"
        "/services - узнать об услугах\n"
        "/prays - узнать цену\n "
        "/vremya_raboty - узнать время работы"

    )
    await update.message.reply_text(welcome_text)


async def services_command(update, context):
    services_text = ( "Услуги салона:\n"
                      "/1.Маникюр\n"
                      "/2.Макияж\n"
                      "/3.Прически"
                      )
    await update.message.reply_text(services_text)

async def prays_command(update, context):
    prays_text = ( "Прайс салона:\n"
                      "/1.Маникюр-1000\n"
                      "/2.Макияж-2000\n"
                      "/3.Прически-2500\n"
                      )
await update.message.reply_text(prays_text)

   async def vremya_raboty_command(update, context):
   vremya_raboty_text = ( "Время работы салона:\n"
                          "/Понедельник-Субота 8:00-21:00\n"
                          "/Воскресенье-выходной"
                          )
await update.message.reply_text(vremya_raboty_text)

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, ConversationHandler, \
    MessageHandler, filters

# Стадії конверсії
DATE_END, VREMYA, TYPE = range(3)
async def button_handler(update, context):
    query = update.callback_query
    await query.answer()

    if query.prays == "infor":
        await query.message.reply_text(
            "Что бы узнать о нас,отправьте следующую информацию:\n"
            "-services - узнать об услугах\n"
        "prays - узнать цену\n "
        "vremya_raboty - узнать время работы"
        )
    elif query.data == "services":
        await query.message.reply_text(
            "Услуги салона:\n"
            "/1.Маникюр\n"
            "/2.Макияж\n"
            "/3.Прически"
        )
    elif query.data == "prays":
        await query.message.reply_text(
            "Прайс салона:\n"
             "/1.Маникюр-1000\n"
             "/2.Макияж-2000\n"
             "/3.Прически-2500\n"
        )
    elif query.data == "vremya_raboty":
        await query.message.reply_text(
            "Время работы салона:\n"
            "/Понедельник-Субота 8:00-21:00\n"
            "/Воскресенье-выходной"
        )

   async def start_command(update, context):
       inline_keyboard = [
           [InlineKeyboardButton("Услуги салона", callback_data= "services")],
           [InlineKeyboardButton("Прайс салона", callback_data= "prays")],
           [InlineKeyboardButton("Время работы салона", callback_data= "vremya_raboty" )]
       ]

     markup = InlineKeyboardMarkup(inline_keyboard)

     await update.message.reply_text(
         "Что бы узнать о нас,отправьте следующую информацию:",
         reply_markup=markup
     )
app.add_handler(CallbackQueryHandler(button_handler))
 async def date_start(update, context):
     context.user_data['date_start']=update.message.text
     await update.message.reply_text("Введите дату записи (например, 2028-10-11):")
     return DATE_END
 async def date_end(update, context):
     context.user_data['date_end'] = update.message.text
     await update.message.reply_text("На которое время (например, 14:00):")
     return VREMYA
 async def type_uslug(update, context):
     context.user_data['type_uslug'] = update.message.text
     reply_keyboard = [["Визажист", "Маникюрша", "Педикюрша"]]
     markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
     await update.message.reply_text("Выберите тип услуги:", reply_markup=markup)
     return  TYPE
 async def data_type(update, context):
     context.user_data['data_type'] = update.message.text
     booking_details = (
         f"Ваши данные для записи:\n"
         f"-Дата записи: {context.user_data['date_start']}\n"
         f"-Время: {context.user_data['date_end']}\n"
         f"-Тип услуги: {context.user_data[' type_uslug']}\n"
         "Если все верно, то наш менеджер свяжеться с вами для подтверждения"
     )
     await update.message.reply_text(booking_details, reply_markup=ReplyKeyboardRemove())
     return ConversationHandler.END
# Добавление ConversationHandler для бронирования
booking_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(button_handler, pattern="^book$")],
    states={

                   DATE_END: [MessageHandler(filters.TEXT & ~filters.COMMAND, date_start)],
            VREMYA: [MessageHandler(filters.TEXT & ~filters.COMMAND, date_end)],
        TYPE        : [MessageHandler(filters.TEXT & ~filters.COMMAND, guests)],

}

)

app.add_handler(booking_handler)
