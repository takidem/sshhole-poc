FROM alpine:3.20

RUN apk add --no-cache openssh \
    && ssh-keygen -A \
    && adduser -D testuser \
    && echo 'testuser:TestPassword123!' | chpasswd

RUN printf '\nPasswordAuthentication yes\nUsePAM no\n' \
    >> /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]
