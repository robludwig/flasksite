import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'thiscantbeguessed'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	
	def config_app(self, app):
		pass
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,'dev-data.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,'test-data.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///" + os.path.join(basedir, 'data.sqlite')

class HerokuConfig(ProductionConfig):
	@classmethod
	def init_app(cls, app):
		ProductionConfig.init_app(app)

		import logging
		from logging import StreamHandler
		file_handler = StreamHandler()
		file_handler.setLevel(logging.WARNING)
		app.logger.addHandler(file_handler)

config = {
		'development' : DevelopmentConfig,
		'testing'     : TestingConfig,
		'production'  : ProductionConfig,
		'heroku'      : HerokuConfig,
		'default'     : DevelopmentConfig

		}
