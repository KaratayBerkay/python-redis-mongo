import os


class App:
    def __init__(self):
        self.routes = os.getenv("ROUTES", {})

    def boot_application(self):
        path = os.getenv("PATH_INFO")
        method = os.getenv("REQUEST_METHOD")
        print('path', path)
        print('method', method)
        print('routes', self.routes)
        return {
            "routes": self.routes
        }


if __name__ == "__main__":
    app = App()
    app.boot_application()
