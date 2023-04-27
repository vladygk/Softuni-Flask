import pyrebase

from decouple import config

SIMPLE_CONFIG = {
    "apiKey": config("API_KEY"),
    "authDomain": config("AUTH_DOMAIN"),
    "projectId": config("PROJECT_ID"),
    "storageBucket": config("STORAGE_BUCKET"),
    "databaseURL": ""
}

SERVICE_ACCOUNT_PATH = "secret.json"

SERVICE_CONFIG = dict(SIMPLE_CONFIG, serviceAccount=SERVICE_ACCOUNT_PATH)


class FirebaseService:
    def __init__(self):
        self.fire_base = pyrebase.initialize_app(SERVICE_CONFIG)
        self.storage = self.fire_base.storage()

    def upload_file(self, file_path, file_name):
        self.storage.child(file_path).put(file_name)

        return self.storage.child(file_path).get_url("")
