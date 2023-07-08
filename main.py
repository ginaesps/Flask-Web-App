#runs when you want to start the server

from website import create_app

app = create_app()

# if indicates that main should only be executed if it runs. If it is exported, the web server should not run
if __name__ == '__main__': 
    app.run(debug = True)