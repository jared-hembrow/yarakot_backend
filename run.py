from service import app
from os import getenv

port = getenv("PORT")

if __name__ == '__main__':
    app.run(port=port, debug=True, host="0.0.0.0")
