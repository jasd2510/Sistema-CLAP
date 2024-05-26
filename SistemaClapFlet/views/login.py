from flet import *
from flet_route import Params, Basket
import logica
from time import sleep
from datetime import datetime

class login:
    def __init__(self):
        #RUTAS
        self.routeRegistrar = "/register"
        self.routePrincipal = "/principal"
        self.routeRecuperar = "/recuperar"
        self.routeLiderPolitico = "/liderPolitico"

        #LOGO

        self.logo = Image(src=f"{logica.rutaactual}\img\clap.png")
        #self.logo = Image(src="SistemaClapFlet\img\clap.png")

    def view(self, page:Page, params:Params, basket:Basket):

        self.restanIntentos = 0
        self.intentos = 0

        def window_event(e):
            if e.data == "close":
                if bool(logica.datoUser) == True:
                    fechaS = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    logica.consulta("UPDATE bitacora SET fechaSalida = ? WHERE fechaEntrada = ? AND usuarios_id = ?", [fechaS, logica.datoUser[0][5], logica.datoUser[0][4]])
                    page.window_destroy()
                else:
                    page.window_destroy()

        page.window_prevent_close = True
        page.on_window_event = window_event

        page.window_maximizable = False
        page.title = "CLAP"
        page.window_resizable = False
        page.window_height = "725"
        page.window_width = "500"
        page.window_center()
        page.window_bgcolor = colors.TRANSPARENT
        page.bgcolor = colors.TRANSPARENT
        sleep(1)
        page.window_visible = True
        page.update()

        #CAMPOS DE TEXTOS
        self.usuario = TextField(hint_text="Ingrese su usuario", label="Usuario", border_radius=30, border_color="#820000", prefix_icon=icons.PERSON, width=300, height=60, on_change=lambda _: self.quitarError(page, self.usuario))
        self.contrasena = TextField(hint_text="Ingrese su contraseña", label="Contraseña", border_radius=30, border_color="#820000", prefix_icon=icons.LOCK, password=True, can_reveal_password=True, width=300, height=60, on_change=lambda _: self.quitarError(page, self.contrasena))

        self.parametroUsuario = self.usuario.value
        paramteroContrasena = self.contrasena.value

        self.text_recuperar = TextButton("Olvido su contrasena?", on_click=lambda _: logica.enrutamiento(page, self.routeRecuperar))
        self.iniciar_sesion = ElevatedButton("Iniciar Sesión", width=300, bgcolor="#cb3234", color="#ffffff", on_click=lambda _:self.loguearse(self.usuario, self.contrasena, page))
        self.registrarTxt = Text("No se encuentra registrado?")
        self.registrarBtn =  TextButton("Crear cuenta", on_click=lambda _: logica.enrutamiento(page, self.routeRegistrar))
        self.derechos_autor = Text("Creado por: Diego Marin, Marco Bandrez, Joel Seco", size=15)

        #CONTENIDO DE LA PAGINA
        self.body = Container(
            height=690,
            width=500,
            bgcolor="#820000",
            border_radius=50,
            content=Column(
                controls=[
                    Container(
                        height=150,
                        alignment=alignment.center,
                        content=self.logo
                    ),

                    Container(
                        bgcolor="white",
                        height=550,
                        width=500,
                        border_radius=border_radius.only(topLeft=50, bottomLeft=50, bottomRight=50),
                        padding=padding.all(30),
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                Column(
                                    spacing=20,
                                    controls=[self.usuario,self.contrasena,]
                                ),
                                self.text_recuperar,
                                self.iniciar_sesion,
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[self.registrarTxt, self.registrarBtn]
                                ),
                                self.derechos_autor
                            ]
                        )
                    )
                ]
            )
        )

        return View(
            "/",
            horizontal_alignment="center",
            vertical_alignment="center",
            padding=0,
            bgcolor="transparent",
            controls=[
                self.body,
            ]
        )

    def loguearse(self, usuario, contrasena, pagee):
        usuario = usuario
        contrasena = contrasena
        pagee = pagee
        
        queryy = "SELECT nivel FROM usuarios WHERE usuario =? AND contrasena=? AND estatus = 1"
        parameters = usuario.value, contrasena.value
        resultado = logica.consulta(queryy, parameters)
        bloqueoUser = logica.consulta("SELECT id FROM usuarios WHERE usuario = ? AND nivel = 2", [usuario.value])
        bloqueoContra = logica.consulta("SELECT id FROM usuarios WHERE contrasena = ? AND usuario = ? AND nivel = 2", [contrasena.value, usuario.value])

        if (usuario.value == "") or (contrasena.value == ""):
            if usuario.value == "":
                usuario.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()

            if contrasena.value == "":
                contrasena.error_text = "Campo vacio, por favor rellenelo para continuar"
                pagee.update()
                
            else: return

        elif (bool(bloqueoUser) == True) and (bool(bloqueoContra) == False):
            if self.intentos == 3:
                logica.consulta("UPDATE usuarios SET estatus = 2 WHERE usuario = ?", [usuario.value])
                self.intentos = 0
                pagee.snack_bar = SnackBar(content=Text(f"El usuario a sido bloqueado por medidas de seguridad"), bgcolor="RED")
                pagee.snack_bar.open = True
                pagee.update()
            else:
                self.intentos = self.intentos + 1
                pagee.snack_bar = SnackBar(content=Text(f"La contraseña no coincide con el usuario, tiene 3 intentos antes de bloquear la cuenta y lleva {self.intentos} intento"))
                pagee.snack_bar.open = True
                pagee.update()

        elif (logica.consulta("SELECT id FROM usuarios WHERE usuario =? AND estatus = 2", [usuario.value])):
            pagee.snack_bar = SnackBar(content=Text(f"Tu usuario se encuentra bloqueado"), bgcolor="RED")
            pagee.snack_bar.open = True
            pagee.update()
        
        elif resultado:
            if resultado[0][0] == 1:
                fechaE = datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
                logica.capturar(self.usuario.value, fechaE)
                idUsuario = logica.datoUser[0][4]
                logica.enrutamiento(pagee, self.routeLiderPolitico)
                logica.consulta("INSERT INTO bitacora VALUES (NULL, ?, NULL, ?)", [fechaE, idUsuario])
                self.intentos = 0
            if resultado[0][0] == 2:    
                fechaE = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                logica.capturar(self.usuario.value, fechaE)
                idUsuario = logica.datoUser[0][4]
                logica.enrutamiento(pagee, self.routePrincipal)
                logica.consulta("INSERT INTO bitacora VALUES (NULL, ?, NULL, ?)", [fechaE, idUsuario])
                self.intentos = 0
        else:
            pagee.snack_bar = SnackBar(content=Text("El usuario no esta registrado"))
            pagee.snack_bar.open = True
            pagee.update()

    def quitarError(self, pagee, textfield):
        pagee = pagee
        textfield = textfield

        textfield.error_text = None
        pagee.update()

    def ir_a_registrarse(self, pages):
        pages = pages

        pages.go("/register")