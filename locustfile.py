from locust import HttpUser, task, between


class AquaFeedUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def home(self):
        self.client.get("/")

    @task(2)
    def sensores(self):
        self.client.get("/sensores")

    @task(2)
    def alarmes(self):
        self.client.get("/alarmes")

    @task(1)
    def listar_tanques(self):
        self.client.get("/tanques")