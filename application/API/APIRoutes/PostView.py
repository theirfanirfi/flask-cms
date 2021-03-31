from flask_classful import FlaskView
from flask import request, jsonify
from application.API.utils import AuthorizeRequest, notLoggedIn, b64_to_data
from application.API.Factory.Factory import BF
class PostView(FlaskView):

    def index(self):
        response = dict({"isLoggedIn": True})
        user = AuthorizeRequest(request.headers)

    def post(self):
        response = dict({"isLoggedIn": True})
        user = AuthorizeRequest(request.headers)
        image = None
        if not user:
            return jsonify(notLoggedIn)

        if request.method == "POST":
            if request.form["post_title"] == "" or request.form["description"] == "":
                response.update(
                    {"isPostCreated": False, "message": "Post title and description cannot be empty."}
                )
                return jsonify(response)

            post_title = b64_to_data(request.form["post_title"])
            post_description = b64_to_data(request.form["description"])
            if request.files:
                image = request.files['image']

            if not post_title or not post_description:
                response.update(
                    {"isPostCreated": False, "message": "Post title and description cannot be empty."}
                )
                return jsonify(response)

            isPostAdded, post = BF.getBL("post").add_post(post_title, post_description, image, user)
            response.update({"isPostCreated": isPostAdded, "post": post, "isError": not isPostAdded})
            return jsonify(response)
        else:
            return "invalid request"