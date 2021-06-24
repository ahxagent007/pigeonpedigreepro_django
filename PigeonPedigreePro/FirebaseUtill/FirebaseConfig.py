import pyrebase

def configFirebase():
    config = {
        "apiKey": "AIzaSyCwSAYAVuMET_N0kZLdu6BwBfOs7Uf4Et0",
        "authDomain": "pigeon-pedigree-pro.firebaseapp.com",
        "databaseURL": "https://pigeon-pedigree-pro.firebaseio.com",
        "projectId": "pigeon-pedigree-pro",
        "storageBucket": "pigeon-pedigree-pro.appspot.com",
        "messagingSenderId": "320725149252",
        "appId": "1:320725149252:web:5e29f8ebfcb2d9b36b7e11",
        "measurementId": "G-S3SGFX6WQT"
    }

    firebase = pyrebase.initialize_app(config)

    return firebase