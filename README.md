# Run Redmine as a Dokku app

## Quick start

```
DOKKU_HOST=dokku.me dokku apps:create redmine
dokku postgres:create redmine
dokku postgres:link redmine redmine
dokku config:set REDMINE_SECRET_TOKEN=$(< /dev/urandom tr -dc 'a-f0-9' | head -c80; echo;)
dokku storage:mount /srv/redmine/data:/home/redmine/data
dokku storage:mount /srv/redmine/log:/var/log/redmine
dokku storage:mount /srv/redmine/plugins:/home/redmine/redmine/plugins
git push dokku master
dokku domains:add git.acme.com
dokku letsencrypt
```

Your new Gitlab instance is now running at <https://git.acme.me>