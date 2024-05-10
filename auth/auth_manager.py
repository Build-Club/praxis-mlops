# Authorization

class praxisAuthManager:
    def __init__(self):
        pass

    def wandb(self, user, key):
        wandb.login(user="build-club", key=key)

    def mlflow(self, token, url):
        pass