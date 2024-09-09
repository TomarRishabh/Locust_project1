from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def send_hii_message(self):
        self.client.post("/send-message/", json={"message": "Hii"})
