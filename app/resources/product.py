import falcon
from falcon import Request, Response


class ProductResource():
    @staticmethod
    def on_get(req: Request, resp: Response):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.media = [
            {"name": "Sepatu"},
            {},
            {}
        ]
        resp.content_type = falcon.MEDIA_JSON
