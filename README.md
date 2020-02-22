# Who Stream

Check if someone is streaming on Twitch via Google Home - WIP

# What is Who Stream ?

Who stream lets you ask your google home to know if a streamer is live on Twitch.
For doing this it uses :

- [IFTTT Google Assistant integration -> Webhook](https://ifttt.com/applets/110325821d)
- [Flask-RESTX](https://github.com/python-restx/flask-restx)
- [Twitch API](https://dev.twitch.tv/)

# What it can do

ATM, nothing ! This is the early stage of the project.
Next step for me is to check if a specific streamer is live (❤️ [mistermv](https://www.twitch.tv/mistermv))
If you want to know more about the progress, check the github project.

# Installation

This projet use [pipenv](https://pipenv.readthedocs.io/en/latest/).
To install this project, just do: `pipenv install`.

Then we'll need to configure IFTTT. To do this, you can copy the applet linked above.
Configure this freshly copied IFTTT applet to redirect response to your url
(It should look like this : `http://example.com/is_live/`), set the language
and what you want to say to your assistant to enable it.

You can use [localtunnel](https://localtunnel.github.io/www/) if you use the API locally
to get an URL accessible for IFTTT.

Now, it's time to run this API 🥳 !
You can run the project with the command : `pipenv run python app.py`.
You'll be greeting with the swagger interface of the API in debug mode.

And voilà, your setup is finished. You can use the command on you Google Home !
