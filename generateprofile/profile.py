import random
from .useragents import user_agents_list
from .proxies import proxies_list

class GenerateProfile():
    def __init__(self):
        pass

    def getUserAgent(self):
        userAgentLenght = len(user_agents_list) - 1
        return user_agents_list[random.randint(0, userAgentLenght)]

    def getProxy(self):
        proxiesLenght = len(proxies_list) - 1
        return proxies_list[random.randint(0, proxiesLenght)]