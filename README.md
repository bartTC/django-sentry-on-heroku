# Django Sentry on Heroku

Get this up and runnnig by::

```bash
# Create and provision Heroku application 
heroku create
heroku addons:add shared-database:5mb
# Sent config variables
heroku config:add SENTRY_KEY=<some-random-access-key>
# Initialize Sentry
heroku run bash
	# Run this one command in the Heroku shell, then exit it:
heroku run sentry --config=sentry_conf.py upgrade
heroku run sentry --config=sentry_conf.py createsuperuser
heroku scale web=1
```


## Email Support

Configure email support thru Sendgrid:

``` bash
heroku addons:add sendgrid:starter
heroku config:set MAIL_TO=you@example.com
```

And finally go to heroku.com, find your app and the SendGrid addon,
and complete the account setup.
