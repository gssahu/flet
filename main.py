import flet  as ft


def main(page: ft.Page):
    def btn_clicked(e):
        page.add(ft.Text("user name {0} password {1}".format(user.value,password.value),color="green"))
    page.window_width = 300.00
    page.window_height= 600.00
    page.add(ft.AppBar(title=ft.Text("My Application"), bgcolor=ft.colors.RED_800))
    user = ft.TextField(hint_text="User Name:")
    password = ft.TextField(hint_text="Password:",password=True)
    btn = ft.FilledButton(text="LOGIN",on_click=btn_clicked)
    page.add(user)
    page.add(password)
    page.add(btn)

ft.app(target=main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER) 