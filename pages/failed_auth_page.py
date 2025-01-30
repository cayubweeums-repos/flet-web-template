import flet as ft

# Failed Authentication Page Content
class Failed_Auth_Content:
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Column(
            controls=[
                ft.Text("Authentication Failed", size=24, weight="bold"),
                ft.ElevatedButton(text="Retry Login", on_click=self.retry_login),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def get_content(self):
        return self.content

    async def retry_login(self, e):
        self.page.go("/login")