class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///infinite_insights.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "super-secret-key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRY_SECONDS = 3600
