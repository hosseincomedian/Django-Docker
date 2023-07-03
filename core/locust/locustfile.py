from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    def on_start(self):
        response = self.client.post("accounts/api/v1/jwt/create/", data={
            "email": "ho@gmail.com",
            "password": "ho"
        }).json()
        print(response)
        self.client.headers = {"Authorization": f"Bearer {response.get('access', None)}"}

    @task
    def post_list(self):
        self.client.get("blog/api/v1/post/")
 
    @task
    def cat_list(self):
        self.client.get("blog/api/v1/category/")

        