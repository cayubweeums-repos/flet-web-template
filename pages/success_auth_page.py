import flet as ft

# Success Authentication Page Content
class Success_Auth_Content:
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Column(
            controls=[
                ft.Text("Authentication Successful!", size=24, weight="bold"),
                ft.ElevatedButton(text="Logout", on_click=self.logout),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def get_content(self):
        return self.content

    async def logout(self, e):
        # Clear session data
        self.page.session.remove("session_id")
        self.page.session.remove("user_id")
        self.page.go("/login")