
from configparser import (
	ConfigParser,
	ExtendedInterpolation
)

config = ConfigParser(
	interpolation = ExtendedInterpolation()
)

#config.read("settings.ini")

try:
	config.read("settings.ini")
except:
	print("settings ini error format") #if an syntax format error
	raise SystemExit()

print(config["log"]["log_filename"])
print(config["log"]["log_filename"])

if ("username" in config["database"]):
	print("username is in database")

print(config.get("database","password")) 

#access sections 
#config. return >string<
print("config.sections(): ", config.sections())
print("config.options(\"database\"): ", config.options("database"))

print("type: ", type(config["database"]["port"]))

port = int(config["database"]["port"])
print("port type: ", port, " ", type(port))

print("*" * 20)
port1 = config.getint("database","port")
print("port1: ", port1, type(port1))

#fallback if member is not in .ini file
print("*" * 20)
port2 = config.getint("database","port_1", fallback=7)
print(port2, type(port2))

#getfloat()
#getboolean()
print("*" * 20)
if (config.getboolean("log", "logging_on")):
	print("logging on.....")
else:
	print("logging off...") 

'''
config = ConfigParser(
	interpolation = ExtendedInterpolation()
)'''

print(config["log"]["log_dir"])

print(config["database"]["archive_dir"])


"""
output:
log.txt
log.txt
username is in database
test123
config.sections():  ['log', 'database']
config.options("database"):  ['server', 'port', 'username', 'password', 'archive_dir']
type:  <class 'str'>
port type:  6070   <class 'int'>
********************
port1:  6070 <class 'int'>
********************
7 <class 'int'>
********************
logging off...
/app/logs
/app/archive

"""
