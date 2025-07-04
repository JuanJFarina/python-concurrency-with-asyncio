from locust import FastHttpUser, task


class TimeUser(FastHttpUser):
    @task
    def test_time(self):
        self.client.get("/time")
