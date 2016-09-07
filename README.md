# Run Redmine as a Dokku app

## Quick start

```
git clone https://github.com/iteratia/dokku-redmine.git
cd dokku-redmine
DOKKU_HOST=dokku.me dokku apps:create redmine
dokku postgres:create redmine
dokku postgres:link redmine redmine
dokku config:set REDMINE_SECRET_TOKEN=$(< /dev/urandom tr -dc 'a-f0-9' | head -c80; echo;)
dokku storage:mount /srv/redmine/data:/home/redmine/data
dokku storage:mount /srv/redmine/log:/var/log/redmine
dokku storage:mount /srv/redmine/plugins:/home/redmine/redmine/plugins
git push dokku master
dokku domains:add redmine.acme.com
dokku letsencrypt
```

Your new Redmine instance is now running at <https://redmine.acme.com>
