from celery import shared_task
from . import tgbot

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 10, 'countdown': 12})
def send_form(self, message):
    try:
        tgbot.bot.send_message(chat_id=-1002148661131, text=''.join(message))
    except:
        raise Exception