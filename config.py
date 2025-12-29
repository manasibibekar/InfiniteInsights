class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///infinite_insights..db"
    
    JWT_SECRET_KEY = "secretsecret"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRY_SECONDS = 3600  # 1 hour