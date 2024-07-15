class Config:
	SECRET_KEY = 'B!1weNAt1T⌃%kvhUI*S⌃'

class DevelopmentConfig(Config):
	DEBUG = True
	MYSQL_HOST = 'systemtest.gdl.mex.ibm.com'
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = ''
	MYSQL_DB = 'ejercicios'
	

config = {
	'development' : DevelopmentConfig
}