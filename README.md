# Run Redmine as a Dokku app

## Quick start

```
DOKKU_HOST=dokku.me dokku apps:create redmine
dokku postgres:create redmine
dokku postgres:link redmine redmine
git push dokku master
dokku domains:add git.acme.com
dokku letsencrypt
```

Your new Gitlab instance is now running at <https://git.acme.me>