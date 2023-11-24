import flet as ft
from flet import TextField,Checkbox,ElevatedButton,Text,Row,Column
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = 'Signup'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    

    #set up our fields
    text_username : TextField = ft.TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password : TextField = ft.TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    Checkbox_signup : Checkbox = ft.Checkbox(label='I agree to terms and conditions', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Signup', width=200, disabled=True)
    
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    def validate(e: ControlEvent)-> None:
        if all ([text_username.value, text_password.value, Checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True


            page.update()

    
    def submit(e:ControlEvent) -> None:
        print('Username: ', text_username.value)
        print('Password', text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER,
                
            )
            
        )


        #LINK THE FUNCTION TO THE UI
        text_username.on_change = validate
        text_password.on_change = validate
        Checkbox_signup.on_change = validate
        button_submit.on_click = submit

        #Render the signup page

    page.add(
        Row(
            controls=[
                Column(
                    [
                        text_username,
                        text_password,
                        Checkbox_signup,
                        button_submit
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ =='__main__':
    ft.app(target=main)
    
     





