docker run \
        --name=bind9 \
        --restart=always \
        --publish 53:53/udp \
        --publish 53:53/tcp \
        --publish 127.0.0.1:953:953/tcp \
        internetsystemsconsortium/bind9:9.16
