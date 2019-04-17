from hse_arch import create_app

app = create_app('development')
# cli.register(app)

if __name__ == '__main__':
    app.run()
