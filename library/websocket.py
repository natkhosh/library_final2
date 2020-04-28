
import json

from django.apps import apps
from syncasync import sync_to_async


@sync_to_async
def getBookCount(book):
    return book.objects.all().count()


async def websocket_application(scope, receive, send):
    Book = apps.get_model('book', 'Book')
    while True:
        event = await receive()


        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            print(event['text'])
            if event['text'] == 'books?':
                now_book_in_db = await getBookCount(Book)
                await send({
                    'type': 'websocket.send',
                    'text': json.dumps({'value': now_book_in_db})
                })