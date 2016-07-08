# Django Sentry 8 on Heroku

This repository lets you setup Sentry 8 on Heroku by the Heroku toolbelt.
If you think this is too complicated, see [this repository](https://github.com/alex88/sentry-heroku)
which makes the whole thing a one-click event.

### Initial Setup Steps

1. Create the Heroku application and attach required addons. They are all free.

        heroku apps:create <app-name>
        heroku addons:create heroku-postgresql:hobby-dev
        heroku addons:create heroku-redis:hobby-dev
        heroku addons:create sendgrid:starter

2. Set some default environment settings:

        heroku config:add SECRET_KEY=<some-random-access-key>

3. Push this repository and let it deploy. This will take a while.

        git push heroku master

4. Initialize Sentry. This takes even more time. It will ask you to create
   an initial administration user.

        heroku run sentry --config=. upgrade

That's all. Open the web url of your application and finish the setup.
You'll find the web url here at the end:

    heroku apps:info <app-name>
