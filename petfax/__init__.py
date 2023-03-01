#import

from flask import Flask 

def create_app(): 
    app = Flask(__name__)
    
    #index route

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    from . import pet
    app.register_blueprint(pet.bp)

    return app
