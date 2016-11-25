# Run Redmine as a Dokku app

## Quick start

1. Clone/fork this repo.
2. Update settings in `dokku.env` (please refer to <https://github.com/sameersbn/docker-redmine#available-configuration-parameters>).
3. Run:

```
DOKKU_HOST=dokku.me dokku apps:create redmine
dokku postgres:create redmine
dokku postgres:link redmine redmine
dokku config:set REDMINE_SECRET_TOKEN=$(< /dev/urandom tr -dc 'a-f0-9' | head -c80; echo;)
dokku config:set $(cat dokku.env)
dokku storage:mount /srv/redmine/data:/home/redmine/data
dokku storage:mount /srv/redmine/log:/var/log/redmine
dokku storage:mount /srv/redmine/plugins:/home/redmine/redmine/plugins
git push dokku master
```

Your new Redmine instance is now running at <http://redmine.dokku.me>.
