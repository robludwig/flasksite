import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'thiscantbeguessed'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	
	def config_app(self, app):
		pass
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,'dev-data.sqllite')

class TestingConfig(config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,'test-data.sqllite')

class ProductionConfig(config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "sqlite:///" + os.path.join(basedir, 'data.sqllite')

config = {
		'development' : DevelopmentConfig,
		'testing'     : TestingConfig,
		'production'  : ProductionConfig,
		'default'     : DevelopmentConfig

		}
