# Who Stream

![icon]('logo.png?raw=true')

Check if someone is streaming on Twitch via Google Home - WIP

# What is Who Stream ?

Who stream lets you ask your google home to know if a streamer is live on Twitch.
For doing this it uses :

- [Dialogflow](https://dialogflow.com/)
- [Google Assistant](https://developers.google.com/assistant)
- [Flask-RESTX](https://github.com/python-restx/flask-restx)
- [Twitch API](https://dev.twitch.tv/)

# What it can do

It can check if a specific streamer is live (❤️ [mistermv](https://www.twitch.tv/mistermv))
If you want to know more about the progress, check the github project.

# How to use Who Stream ?

Who stream will be accessible to anyone with a google home.
You don't need to install all of this locally to get all the experience !
The app is currently in Alpha release. If you want to test it,
contact me to add you to alpha users.

# Local Installation

This projet use [pipenv](https://pipenv.readthedocs.io/en/latest/).
To install this project, just do: `pipenv install`.

Then we'll need to configure Dialogflow. For this, you'll need to:
- Create a new project
- Add an intent. If you don't want to create one, you can upload the example inside the Dialogflow folder.
- Add a webhook in Fulfillment.
- Inside your intent events, add the `GOOGLE_ASSISTANT_WELCOME` event.
- Enable in your intent the webhook in the Fulfillment part.

You can use [localtunnel](https://localtunnel.github.io/www/) if you use the API locally
to get an URL accessible for Dialogflow.

Next, you'll need to get your Twitch API access. For that,
[Follow the Twitch API guide](https://dev.twitch.tv/docs/api#step-1-setup).
Then, copy / paste `.env.example` and rename it `.env` . Complete the values inside
it with the corresponding IDs you have generated on your Twitch API Dashboard.

Now, it's time to run this API 🥳 !
You can run the project with the command : `pipenv run python app.py`.
You'll be greeted with the swagger interface of the API in debug mode.

After all of that, you can configure your app in the Actions Console from google.
Follow the steps from the front page to release your app to the world.

And voilà, your setup is finished. You can use the command on your Google Home !
