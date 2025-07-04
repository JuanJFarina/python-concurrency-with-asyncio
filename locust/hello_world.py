from locust import FastHttpUser, task


class HelloWorldUser(FastHttpUser):
    @task
    def test_hello_world(self):
        self.client.get("/hello-world")
