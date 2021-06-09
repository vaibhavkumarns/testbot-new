import os


class DefaultConfig:
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    # APP_ID = os.environ.get("MicrosoftAppId", "06e03ae2-39b1-4c2d-bb92-88a9d82479aa")
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Zpq3~phWY653KMwCu.zxWwDy3MIC2--Y7n")