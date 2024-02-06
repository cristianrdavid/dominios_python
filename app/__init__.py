from flask import Flask

# crear el objero prinsipal 
app = Flask(__name__)

#importasr a las rutas definidas 

from app import routes


if __name__== "__main__":
    app.run()