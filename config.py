# 没必要更改此端口，若要更改此端口，也要手动去改docker-compose.yml文件和./nginx/nginx.conf里对应的端口
PORT = 1234

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"
# 如果要更改此域名，请记得同时更改./nginx/nginx.conf里的www.clouflare.com为你要更改的域名
TLS_DOMAIN = "www.cloudflare.com"
PROXY_PROTOCOL = True

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
