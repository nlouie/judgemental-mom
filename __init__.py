from flask import Flask

from auth_config import CONFIG     # for authomatic
from authomatic import Authomatic
# http://peterhudec.github.io/authomatic/reference/adapters.html#authomatic.adapters.WerkzeugAdapter
from authomatic.adapters import WerkzeugAdapter


# ----------------- Init ----------------------------#

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['DEBUG'] = True

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)


app.run()