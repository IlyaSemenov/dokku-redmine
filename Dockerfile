FROM sameersbn/redmine:3.2.1-6

EXPOSE 80
ENTRYPOINT ["/sbin/dokku-entrypoint.sh"]
CMD ["app:start"]

COPY sbin/* /sbin/
