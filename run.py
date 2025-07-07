# This is the entry point of our application. Its only job is to import and run our Flask app. 
# You'll execute python run.py to start the server.

from app import create_app, db

app = create_app()


@app.shell_context_processor
def make_shell_processor():
    return {'db': db}

if __name__ == '__main__':
    app.run(debug=True)