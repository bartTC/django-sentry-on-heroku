# Django Sentry on Heroku

Get this up and runnnig by the following shell commands:

```bash
# Create and provision Heroku application 
heroku create
heroku addons:add shared-database:5mb
heroku config:add SENTRY_KEY=<some-random-access-key>
git push heroku master
# Initialize Sentry
heroku run sentry --config=sentry_conf.py upgrade
heroku run sentry --config=sentry_conf.py createsuperuser
```


## Email Support

Configure email support thru Sendgrid:

``` bash
heroku addons:add sendgrid:starter
heroku config:set MAIL_TO=you@example.com
```

And finally go to heroku.com, find your app and the SendGrid addon,
and complete the account setup.
