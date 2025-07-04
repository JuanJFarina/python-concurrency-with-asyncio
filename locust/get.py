from locust import FastHttpUser, task


class GetUser(FastHttpUser):
    @task
    def test_get(self):
        self.client.get("/get")
