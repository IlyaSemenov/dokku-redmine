FROM sameersbn/redmine:3.2.1-6

ENTRYPOINT ["/sbin/dokku-entrypoint.sh"]
CMD ["app:start"]

COPY sbin/* /sbin/
