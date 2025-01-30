import flet as ft

# Login Page Content
class Login_Content:
    def __init__(self, page: ft.Page):
        self.page = page
        self.email_input = ft.TextField(label="Email", autofocus=True)
        self.password_input = ft.TextField(label="Password", password=True)
        self.login_button = ft.ElevatedButton(text="Login", on_click=self.on_login)
        self.content = ft.Column(
            controls=[
                self.email_input,
                self.password_input,
                self.login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def get_content(self):
        return self.content

    def set_login_handler(self, handler):
        self.login_handler = handler

    async def on_login(self, e):
        email = self.email_input.value
        password = self.password_input.value
        if email and password:
            await self.login_handler(email, password)