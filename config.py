class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications
    UPLOAD_DIRECTORY = 'uploads/'
    DOWNLOAD_DIRECTORY = 'ann_folder/downloads'
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024
    ALLOWED_EXTENSIONS= '.csv'
    SECRET_KEY = 'Amo101'
    UPLOAD_DIRECTORY_2 = 'map_uploads'
    SHAPE_RESTORE_SHX = 'YES'
