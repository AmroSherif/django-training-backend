from rest_framework.response import Response


class UserEditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, id):
        if request.user.id == id:
            return self.get_response(self, request, id)
        return Response("You cannot edit this account")
