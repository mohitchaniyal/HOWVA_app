from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
#Window.size=(720,1280)
home_page_helper="""
ScreenManager:
    LoginScreen:
    SignupScreen:
    DashboardScreen: 
<LoginScreen>:
    name:'login_page'
    Image :
        source : "logo.png"
        pos_hint:{'center_x':.5,"center_y":.7}
        size_hint:(None,None)
        width:400
        height:400
    MDTextField :
        id:'login_email'
        hint_text:"Email or Phone Number"
        pos_hint:{'center_x':.5,"center_y":.5}
        size_hint:(None,None)
        helper_text:"example@email.com or 821850****"
        helper_text_mode:"on_focus" #persistent
        width:550
        height:300
        icon_right:"account"
        icon_right_color:app.theme_cls.primary_color
    MDTextField :
        id:login_password
        hint_text:"Password"
        pos_hint:{'center_x':.5,"center_y":.4}
        size_hint:(None,None)
        helper_text:"Don't Know Click Forget Password"
        helper_text_mode:"on_focus" #persistent
        width:550
        height:300
        icon_right:"shield-key"
        password:True
        icon_right_color:app.theme_cls.primary_color
    MDRectangleFlatButton :
        text:' Login '
        pos_hint:{'center_x':0.5,"center_y":0.3}
        size_hint:(None,None)
        width:300
        height:250
        on_press:root.manager.current='dashboard'
        on_press:app.login()
    MDRectangleFlatButton :
        text:'Sign Up'
        pos_hint:{'center_x':0.5,"center_y":0.2}
        size_hint:(None,None)
        width:300
        height:250
        on_press:root.manager.current='signup_page'



<SignupScreen>:
    name:'signup_page'
    MDTextField :
        hint_text:"Enter Your First Name"
        pos_hint:{'center_x':.5,"center_y":.9}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"account"
        icon_right_color:app.theme_cls.primary_color
    MDTextField :
        hint_text:"Enter Your Last Name"
        pos_hint:{'center_x':.5,"center_y":.8}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"account"
        icon_right_color:app.theme_cls.primary_color
    MDTextField :
        hint_text:"Enter Your Phone Number"
        pos_hint:{'center_x':.5,"center_y":.7}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"phone"
        icon_right_color:app.theme_cls.primary_color
    MDTextField :
        hint_text:"Enter Your Email"
        pos_hint:{'center_x':.5,"center_y":.6}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"mail"
        icon_right_color:app.theme_cls.primary_color
    MDTextField :
        hint_text:"Enter Your Password"
        pos_hint:{'center_x':.5,"center_y":.5}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"shield-key"
        icon_right_color:app.theme_cls.primary_color
        password:True
    MDTextField :
        hint_text:"Security Question"
        pos_hint:{'center_x':.5,"center_y":.4}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"account-question"
        icon_right_color:app.theme_cls.primary_color

    MDTextField :
        hint_text:"Security Answer"
        pos_hint:{'center_x':.5,"center_y":.3}
        size_hint:(None,None)
        width:550
        height:300
        icon_right:"animation-play"
        icon_right_color:app.theme_cls.primary_color

    MDRectangleFlatButton :
        text:'sign up'
        pos_hint:{'center_x':0.5,"center_y":0.2}
        size_hint:(None,None)
        width:300
        height:250
        on_press:root.manager.current='login_page'
              

<DashboardScreen>:
    name:'dashboard'
    BoxLayout:
        orientation:"vertical"
        MDToolbar:
            title:'Mohit'
            #left_action_items:[["menu",lambda x:camera.play]]
        
        MDLabel:
            text:'I Am Your Assistant Rem Rem'
            halign:'center'
        MDBottomAppBar:

            MDToolbar:
                #title: "Titl"
                icon: "microphone"
                type: "bottom"
                left_action_items: [["abjad-arabic", lambda x: x]]
                right_action_items: [["abjad-hebrew", lambda x: x]]
        """
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass
sm=ScreenManager()
sm.add_widget(LoginScreen(name='login_page'))
sm.add_widget(SignupScreen(name='signup_page'))
sm.add_widget(DashboardScreen(name='dashboard'))


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette="DeepOrange"
        self.screen=Builder.load_string(home_page_helper)
        return self.screen 
    def login(self):
        pass
    
MainApp().run()