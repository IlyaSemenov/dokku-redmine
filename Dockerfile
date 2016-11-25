FROM sameersbn/redmine:3.3.1

EXPOSE 80
ENTRYPOINT ["/sbin/dokku-entrypoint.sh"]
CMD ["app:start"]

COPY sbin/* /sbin/
COPY CHECKS /app/
