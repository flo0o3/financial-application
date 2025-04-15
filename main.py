from kivy. app import App
from kivy. uix. label import Label

class MainApp(App):
    def build(self):
        label = Label(text ='lets go',
                      size_hint = (1,1),
                      pos_hint ={'center_x': .4, 'center_y': .8}

                      )
        return label

if __name__ == '__main__':
    MainApp().run()

