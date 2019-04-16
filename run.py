from hse_arch import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)
# cli.register(app)

if __name__ == '__main__':
    app.run()
