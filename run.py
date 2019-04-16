from hse_arch import create_app

app = create_app()
# cli.register(app)

if __name__ == '__main__':
    app.run()
