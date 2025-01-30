"""
Imports
#----------------------------------------------------------------------------------------------------
"""
import os
import datetime
from time import sleep
import logging
import flet as ft
from flet import Page, Theme
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.id import ID
from pages.success_auth_page import Success_Auth_Content
from pages.failed_auth_page import Failed_Auth_Content
from pages.login_page import Login_Content

_time = datetime.date.today()
FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
logging.basicConfig(filename='./{}.log'.format(_time), format=FORMAT, level=logging.DEBUG, datefmt="[%X]")
log = logging.getLogger("main")

# Initialize Appwrite Client
client = Client()
client.set_endpoint('http://<serverIP/domain>/v1')  # Your Appwrite endpoint
client.set_project('<project_id>')  # Your Appwrite project ID
client.set_key('<api_key>')  # Your Appwrite API key
client.set_self_signed() # Use only on dev/test environments when using a local dev Appwrite instance.

account = Account(client)

def main(page: Page):
    ## Initialize page contents
    login_page = Login_Content(page)

    page.title = "flet-web-template"
    page.theme_mode = 'dark'
    page.theme = Theme(color_scheme_seed='red')

    async def route_change(route):
        log.debug(f"Route changed to {page.route}")
        troute = ft.TemplateRoute(page.route)
        content_column.controls.clear()

        # Route matching
        if troute.match("/login"):
            content_column.controls.append(login_page.get_content())
        elif troute.match("/auth-failed"):
            content_column.controls.append(Failed_Auth_Content(page).get_content())
        elif troute.match("/auth-success"):
            # Validate session data
            session_id = page.session.get("session_id")
            user_id = page.session.get("user_id")
            if session_id and user_id:
                content_column.controls.append(
                    Success_Auth_Content(page).get_content()
                )
            else:
                page.go("/login")
        else:
            content_column.controls.append(ft.Text(f"404 - Page not found: {page.route}"))

        page.update()

    page.on_route_change = route_change

    # Persistent layout
    content_column = ft.Column(expand=True)

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        content_column
                    ],
                    expand=True
                )
            ],
            expand=True
        )
    )

    async def handle_login(email, password):
        try:
            # Authenticate user with Appwrite
            session = account.create_email_password_session(email, password)
            log.info(f"User authenticated: {session['userId']}")

            # Store session data in Flet's session storage
            page.session.set("session_id", session['$id'])
            page.session.set("user_id", session['userId'])

            # Redirect to success page
            page.go("/auth-success")
        except Exception as e:
            log.error(f"Authentication failed: {e}")
            # Redirect to failure page
            page.go("/auth-failed")

    # Attach login handler to the login page
    login_page.set_login_handler(handle_login)

    page.go("/login")

ft.app(target=main)