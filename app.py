from dip import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
else:
    gunicorn_app = create_app(dev_config=False)