from flask import Blueprint, redirect, url_for, session
from app import oidc

auth = Blueprint("auth", __name__)


@auth.route("/logout", methods=["GET"])
def logout():
    # Clear the session and redirect to the logout URL
    oidc.logout()
    session.clear()
    return redirect(url_for("main.static_web"))


@auth.route("/callback", methods=["GET"])
def callback():
    # Check if the user is authenticated
    # print(vars(oidc))
    # print(vars(session))
    if oidc.user_loggedin:
        # Retrieve user information
        user_info = oidc.user_getinfo(["sub", "email", "name"])
        print(user_info)
        # Store user info in the session or process it as needed
        session["user"] = {"id": user_info.get("sub"), "email": user_info.get("email"), "name": user_info.get("name")}

        print("redircting to main.static_web")
        return redirect(url_for("main.static_web"))
    else:
        print("not auth redirecting to main.static_web")
        # If not authenticated, redirect to the login page
        return "Not authenticated", 401
