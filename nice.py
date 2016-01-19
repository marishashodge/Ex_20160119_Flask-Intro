from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<html><body><p><a href = '/hello'></p>Click me</a><br>Hi! This is the home page.</body></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit"><br>
          <label>Choose your compliment: </label>
          <label><input type= "radio" name = "compliments" value = "awesome">Awesome</label>
          <label><input type= "radio" name = "compliments" value = "terrific">Terrific</label>
          <label><input type= "radio" name = "compliments" value = "fantastic">Fantastic</label>
          <label><input type= "radio" name = "compliments" value = "neato">Neato</label>
          <label><input type= "radio" name = "compliments" value = "fantabulous">Fantabulous</label>
          <label><input type= "radio" name = "compliments" value = "wowza">Wowza</label>
          <label><input type= "radio" name = "compliments" value = "oh-so-not-meh">Oh-so-not-meh</label>
          <label><input type= "radio" name = "compliments" value = "brilliant">Brilliant</label>
          <label><input type= "radio" name = "compliments" value = "ducky">Ducky</label>
          <label><input type= "radio" name = "compliments" value = "coolio">Coolio</label>
          <label><input type= "radio" name = "compliments" value = "incredible">Incredible</label>
          <label><input type= "radio" name = "compliments" value = "wonderful">Wonderful</label>
          <label><input type= "radio" name = "compliments" value = "smashing">Smashing</label>
          <label><input type= "radio" name = "compliments" value = "lovely">Lovely</label>

        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliments")
  

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=False)
