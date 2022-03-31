from flask import Flask
from conf.config import DevelopmentConfig

def create_app(config=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/static", static_folder='static')
    app.config.from_object(config)
    from views import cart, categories, bag
    ACTIVE_ENDPOINTS = [('/cart', cart), ("/categories", categories), ("/bag", bag)]  # Movido para evitar importaciones circulares
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()