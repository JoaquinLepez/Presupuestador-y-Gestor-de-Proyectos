class Config:
     SQLALCHEMY_TRACK_MODIFICATIONS = False

     @staticmethod
     def init_app(app):
         pass
        # app.run(host="0.0.0.0", port=5000, debug=True)

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://joaquin:123456789@localhost:5432/dev_database'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://joaquin:123456789@localhost:5432/test_database'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://joaquin:123456789@localhost:5432/database'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}


