"""
Imports
#----------------------------------------------------------------------------------------------------
"""
import os
import logging
import datetime
import flet as ft
from flet import Page, Theme

# Set environment variables
os.environ["FLET_SECRET_KEY"] = os.urandom(12).hex()


async def main(page: Page):
    page.title = "W.I.P. appwrite"
    page.theme_mode = 'dark'
    page.theme = Theme(color_scheme_seed='red')

    page.add(
        ft.Row(
            [
                ft.Column(
                    [ft.Text('Hello World!')],
                    expand=True
                )
            ],
            expand=True
        )
    )

    page.go("/")

ft.app(target=main)