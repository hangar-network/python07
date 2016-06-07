# Based on: https://github.com/mayuresh/python-firebase-demo
from firebase import firebase
from sseclient import SSEClient
from multiprocessing import Process
import json
import authentication

FIREBASE_URL = "https://python07chat.firebaseio.com/"
MESSAGE_PATTERN = "{} disse: {}"

def retrieve_and_print_messages():
    # Server Side Event.
    sse = SSEClient(FIREBASE_URL + "Messages.json")
    for new_message in sse:
        # message_data is a dictionary (returned by json.loads). The content of this
        # dictionary is the same content of new_message.data (a string that respects
        # the JSON standard)
        message_data = json.loads(new_message.data)
        # If data field is empty (equal to None in the dictionary), we had no message, so let's skip
        if message_data is None or message_data["data"] is None:
            continue
        # Old messages and New messages are retrieved with a difference.
        # The old ones have this "appeareance":
        # { "data": { "UNIQUE_ID": {"name": "username", "message": "message sent by the user"}, "path": "/" }}
        # While the new ones are like:
        # { "data": {"name": "username", "message": "message sent by the user"}, "path": "/UNIQUE_ID" }
        # We need only the innermost data (name and message), so, we must split into 2 cases:
        if message_data["path"] == "/": #the old ones
            print("Mensagens Antigas: ")
            # a way to iterate over a dictionary reading keys and values
            for (key, message) in message_data["data"].items():
                print(MESSAGE_PATTERN.format(message["name"], message["message"]))
            print("______________________________") # I want to separate old and new messages
        else: # the new ones
            print(MESSAGE_PATTERN.format(message_data["data"]["name"], message_data["data"]["message"]))

if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None)
    processo = Process(target=retrieve_and_print_messages)
    processo.start()

    if True: # we'll put an authentication request here
        username = input("Nome: ")
        msg = input("Mensagem de Apresentação: ")
        if msg == "":
            msg = "Entrei no chat, galera!"
        fb.post('/Messages', {
            "name": username,
            "message": msg
        })

        while True:
            msg = input()
            print("\n")
            fb.post('/Messages', {
                "name": username,
                "message": msg
            })
