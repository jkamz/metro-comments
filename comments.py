from models import CommentsModel, users


class Comments:
    def createComment(self):
        author = input("please enter your name:")

        user = [user for user in users if user["username"] == author]

        if not user:
            return "please log in"

        comment = input("please enter comment:")

        new_comment = CommentsModel().create_comment(author, comment)

        return new_comment
