import re
import time

VERSION = str(int(time.time()))


def on_post_page(output, page, config):
    """Append ?v=<build time> to the site's own css/js so browsers never serve a stale copy."""
    return re.sub(r'((?:stylesheets|javascripts)/[\w.-]+\.(?:css|js))(")', r"\1?v=" + VERSION + r"\2", output)
