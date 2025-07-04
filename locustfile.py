from locust import HttpUser, task


class TimeUser(HttpUser):
    @task
    def test_time(self):
        self.client.get("/time")
