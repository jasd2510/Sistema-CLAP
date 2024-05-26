from flet import *
from flet_route import Params, Basket
from datetime import datetime
from time import sleep

import os
import pathlib
import shutil

import logica
import reporte

class liderPolitico:
    def __init__(self):       
        self.logo = Image(src=f"{logica.rutaactual}\img\clap.png", height=80)

        #self.logo = Image(src="img\clap.png", height=80)
        #self.logo = Image(src="SistemaClapFlet\img\clap.png", height=80)
        self.indicator = Container(bgcolor='WHITE', width=140, height=40, border_radius=border_radius.only(topLeft=15, bottomLeft=15), offset=transform.Offset(0.075,5.5), animate_offset=animation.Animation(500, AnimationCurve.DECELERATE))

    def view(self, page:Page, params:Params, basket:Basket):

        self.bitacoraLista = []

        self.iDLiderCalle = logica.datoUser[0][0]
        self.nombreLiderCalle = logica.datoUser[0][1]
        self.ApellidoLiderCalle = logica.datoUser[0][2]
        self.UbicacionLiderCalle = logica.datoUser[0][3]
        self.idUsuario = logica.datoUser[0][4]
        self.fechaEntradaUser = logica.datoUser[0][5]

        self.check = Checkbox(on_change=lambda _:self.estatusUsuario(page))

        self.entryEmpresa = TextField(label="Empresa", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryEmpresa), logica.validarNombres(self.entryEmpresa, page)])
        self.entryTamano = TextField(label="Tamaño", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryTamano), logica.validarNombres(self.entryTamano, page)])
        self.entryPico = TextField(label="Pico", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryPico), logica.validarNombres(self.entryPico, page)])

        self.entryComunidad = TextField(label="Comunidad", hint_text="Minimo 4 caracteres", max_length=30, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryComunidad), logica.validarNombres(self.entryComunidad, page)])
        self.entryVereda = TextField(label="Vereda\Calle", hint_text="", max_length=30, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.entryVereda), logica.validarNombres(self.entryVereda, page)])
        self.cantidadVerdas = TextField(label="Cantidad de Vereda\Calle", hint_text="", max_length=2, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(page, self.cantidadVerdas), logica.validarNumeros(self.entryComunidad, page)])
        self.cantidadVerdas.value = "1"

        page.title = "CLAP"
        page.window_maximizable = False
        page.window_resizable = False
        page.window_height = "800"
        page.window_width = "1000"
        page.window_center()

        self.titulo = Text("Lideres de Calle", style=TextThemeStyle.TITLE_LARGE, color="white")
        self.textoSlider = Text(f"{self.nombreLiderCalle}", weight=FontWeight.W_500, color="WHITE")

        #self.barraBusqueda = TextField(hint_text="Buscar Jefe de Familia", width=280, height=40)

        self.nombreLi = Text("")
        self.apellidoLi = Text("")
        self.cedulaLi = Text("")
        self.ubicacionLi = Text("")
        self.telefonoLi = Text("")
        self.correoLi = Text("")
        #self.nombreP = Text("")
        #self.apellidoP = Text("")
        #self.cedulaP = Text("")
        #self.ubicacionP = Text("")
        self.preguntaP = Text("")
        self.respuestaP = Text("")
        self.usuarioP = Text("")
        self.contrasenaP = Text("", visible=False)
        #self.telefonoP = Text("")
        #self.correoP = Text("")
        
        self.codigoTelefono = Dropdown(hint_text="Codigo", visible=False, color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.codigoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.numeroTelefono = TextField(label="N telefono", visible=False, hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(page, self.numeroTelefono), logica.validarNumeros(self.numeroTelefono, page)])
        self.correoCambiar = TextField(label="Direccion", visible=False, hint_text="ej: clapcamoruco", max_length=50, border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _: self.quitarError(page, self.correo))
        self.tipoCorreo = Dropdown(hint_text="Correo", visible=False, color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(page, self.tipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com"), dropdown.Option("@outlook.com")])


        self.nombre = Text("")
        self.apellido = Text("")
        self.cedula = Text("")
        self.ubicacion = Text("")
        self.pregunta = Text("")
        self.respuesta = Text("")
        self.usuario = Text("")
        self.contrasena = Text("", visible=False)
        self.telefono = Text("")
        self.correo = Text("")
        self.estatus = Text("")

        self.volverCargarTusDatos(page)

        self.btnCandado = IconButton(icon=icons.LOCK_OUTLINE, on_click=lambda _:self.revelarPass(page))
        self.btnCandadoP = IconButton(icon=icons.LOCK_OUTLINE, on_click=lambda _:self.revelarPassP(page))

        #self.btnLapizTelefono = IconButton(icon=icons.EDIT, on_click=lambda _:self.cambiarTelefono(page))
        #self.btnLapizCorreo = IconButton(icon=icons.EDIT, on_click=lambda _:self.cambiarCorreo(page))

        #self.btnCancelTelefono = IconButton(icon=icons.CANCEL, on_click=lambda _:self.cancelarTelefono(page), visible=False)
        #self.btnCancelCorreo = IconButton(icon=icons.CANCEL, on_click=lambda _:self.cancelarCorreo(page), visible=False)

        #self.btnActualizarTelefono = ElevatedButton("Actualizar", visible=False, on_click=lambda _: self.validarTelefono(page))
        #self.btnActualizarCorreo = ElevatedButton("Actualizar", visible=False, on_click=lambda _: self.validarCorreo(page))

        self.tablaSeleccionarHistorial = DataTable(
            bgcolor="#C5283D",
            columns=[
                #DataColumn(Text("id")),
                DataColumn(Text("Jornada", color="WHITE")),
                DataColumn(Text("Fecha", color="WHITE")),
            ],
            rows=[

            ]
        )

        self.tablaLlenarHistorial = DataTable(
            bgcolor="#C5283D",
            columns=[
                #DataColumn(Text("id")),
                DataColumn(Text("Ci", color="WHITE")),
                DataColumn(Text("Nombre", color="WHITE")),
                DataColumn(Text("Apellido", color="WHITE")),
                DataColumn(Text("Empresa", color="WHITE")),
                DataColumn(Text("Tamano", color="WHITE")),
                DataColumn(Text("Pico", color="WHITE")),
                DataColumn(Text("Agregado", color="WHITE"))
            ],
            rows=[

            ]
        )

        self.columnaCards = Row(
            wrap=True,
        )
        
        self.listaBitacora = ListView(width=400, height=550, spacing=20)

        self.volverGenerarCartas(page)

        #APP BAR
        self.appbar = Container(
            bgcolor="#C5283D",
            border_radius=border_radius.all(15),
            height=100,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(padding=padding.only(left=10) ,content=self.logo),
                    self.titulo,
                    PopupMenuButton(items=[PopupMenuItem(text="Cerrar seccion", on_click=lambda _: self.salir(page))])
                ]
            )
        )

        #SLIDER
        self.slider = Container(
            height=635,
            width=150,
            bgcolor="#C5283D",
            border_radius=border_radius.all(15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=10,
                height=630,
                width=150,
                expand=True,
                controls=[
                    Stack(
                        controls=[
                            Column(
                                height=630,
                                controls=[
                                    self.indicator
                                ]
                            ),

                            Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    Container(
                                        padding=padding.only(top=25),
                                        content=Column(
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            controls=[
                                                CircleAvatar(
                                                    content=Icon(icons.PEOPLE),
                                                    width=80,
                                                    height=80,
                                                ),
                                                Text("Bienvenido", weight=FontWeight.W_500, color="WHITE"),
                                                self.textoSlider,
                                            ]
                                        )
                                    ),

                                    Container(
                                        
                                        margin=margin.only(top=50),
                                        padding=padding.only(left=35),
                                        offset=Offset(x=None, y=None),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Lideres de Calle")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.HOME),
                                                Text("Inicio")
                                            ]
                                        )
                                    ),

                                    Container(
                                        margin=margin.only(top=20),
                                        padding=padding.only(left=35),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorBombonas, self.contenedorBombonas, page), self.cambiar_pagina(6.8), self.cambiarTitulo(page, "Gestion de Bombonas")],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.EVENT_NOTE),
                                                Text("Bombonas")
                                            ]
                                        )
                                    ),

                                    Container(
                                        margin=margin.only(top=20),
                                        padding=padding.only(left=35),
                                        offset=Offset(x=None, y=None),
                                        data=0,
                                        on_click=lambda e: [self.animar(self.contenedorPerfil, self.contenedorPerfil, page), self.cambiar_pagina(8.2), self.cambiarTitulo(page, "Tu Perfil"), self.regresarPassFalse(page)],
                                        content=Row(
                                            controls=[
                                                Icon(name=icons.PEOPLE),
                                                Text("Tu Perfil")
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            )
        )


        #CONTENEDORES PRINCIPALES
        self.contenedorInicio = Container(
            height=635,
            width=815,
            padding=15,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            border_radius=border_radius.all(15),
            alignment=alignment.center,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Row(
                        height=50,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #self.barraBusqueda,
                            Text(""),
                            ElevatedButton("Actualizar Precios", bgcolor="Yellow", color="Black", on_click=lambda _: self.menuPrecios(page))
                        ]
                    ),
                    self.columnaCards
                ]    
            )
        )

        self.contenedorPerfil = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=10),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor="white",
                        height=500,
                        width=800,
                        padding=padding.only(top=40),
                        border_radius=border_radius.all(40),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                Column(
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Nombre:"),
                                                self.nombreLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Nombre", on_click=lambda _: self.editNombreLi(page, self.nombreLi.value))
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Apellido:"),
                                                self.apellidoLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Apellido", on_click=lambda _: self.editApellidoLi(page, self.apellidoLi.value))
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Cedula:"),
                                                self.cedulaLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Cedula", on_click=lambda _: self.editCedulaLi(page, self.cedulaLi.value[0],self.cedulaLi.value[2:]))
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Telefono:"),
                                                self.telefonoLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Telefono", on_click=lambda _: self.editTelefonoLi(page, self.telefonoLi))
                                                #self.codigoTelefono,
                                                #self.numeroTelefono,
                                                #self.btnLapizTelefono,
                                                #self.btnCancelTelefono 
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Correo:"),
                                                self.correoLi,
                                                IconButton(icon=icons.EDIT, tooltip="Editar Correo", on_click=lambda _: self.editCorreoLi(page, self.correoLi))
                                                #self.correoCambiar,
                                                #self.tipoCorreo,
                                                #self.btnLapizCorreo,
                                                #self.btnCancelCorreo
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Ubicacion:"),
                                                self.ubicacionLi,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Pregunta:"),
                                                self.preguntaP,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Respuesta:"),
                                                self.respuestaP,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Usuario:"),
                                                self.usuarioP,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Contraseña:"),
                                                self.contrasenaP,
                                                self.btnCandadoP
                                            ]
                                        ),
                                    ]
                                ),
                                Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Lideres de Calle"), self.regresarPassFalseP(page)]),
                                                ElevatedButton("Ver tu bitacora", on_click=lambda _: [self.animar(self.formularioBitacora, self.formularioBitacora, page), self.cambiarTitulo(page, "Historial de Inicios de sesion"), self.volverGenerarBitacora(page, self.cedulaLi)])
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.contenedorHistorial = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            padding=15,
            border=border.all(2, "#C5283D"),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor="white",
                        height=550,
                        border_radius=border_radius.all(7),  
                        content=Column(
                            expand=True,
                            height=550,
                            scroll=ScrollMode.ALWAYS,
                            controls=[
                                self.tablaSeleccionarHistorial,
                            ]
                        )
                    ),

                    Row(
                        controls=[
                            ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiar_pagina(5.5), self.cambiarTitulo(page, "Mi Comunidad")])
                        ]
                    ),
                ]
            )
        )

        self.formularioLiderCalle = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=10),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor="white",
                        height=500,
                        width=350,
                        padding=padding.only(top=40),
                        border_radius=border_radius.all(40),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Column(
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Nombre:"),
                                                self.nombre,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Apellido:"),
                                                self.apellido,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Cedula:"),
                                                self.cedula,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Ubicacion:"),
                                                self.ubicacion,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Telefono:"),
                                                self.telefono,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Correo:"),
                                                self.correo,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Pregunta:"),
                                                self.pregunta,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Respuesta:"),
                                                self.respuesta,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Usuario:"),
                                                self.usuario,
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Contraseña:"),
                                                self.contrasena,
                                                self.btnCandado
                                            ]
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                Text("Estatus:"),
                                                self.estatus,
                                                self.check
                                            ]
                                        ),
                                    ]
                                ),
                                Column(
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiarTitulo(page, "Lideres de Calle"), self.regresarPassFalse(page)]),
                                                ElevatedButton("Ver Jornadas", bgcolor="Green", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorHistorial, self.contenedorHistorial, page), self.cambiarTitulo(page, "Administrador de jornadas"), self.volverGenerarArchivos(page)])
                                            ]
                                        ),
                                        ElevatedButton("Ver bitacora", on_click=lambda _: [self.animar(self.formularioBitacora, self.formularioBitacora, page), self.cambiarTitulo(page, "Historial de Inicios de sesion"), self.volverGenerarBitacora(page, self.cedula)])
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.formularioBitacora = Container(
            height=635,
            width=815,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            padding=padding.only(top=10),
            alignment=alignment.center,
            border_radius=border_radius.all(15),
            content=Column(
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.listaBitacora,
                    ElevatedButton("Regresar", bgcolor="#cb3234", color="#ffffff", on_click=lambda _:[ self.animar(self.contenedorInicio, self.contenedorInicio, page), self.cambiarTitulo(page, "Lideres de Calle"), self.cambiar_pagina(5.5), self.regresarViewFalse(page)]),
                ]
            )
        )

        self.contenedorBombonas = Container(
            height=635,
            width=815,
            padding=15,
            expand=True,
            bgcolor="WHITE",
            border=border.all(2, "#C5283D"),
            border_radius=border_radius.all(15),
            alignment=alignment.center,
            content=Column(
                spacing=30,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    ElevatedButton("Agregar nueva Empresa", on_click=lambda _: self.nuevaEmpresa(page)),
                    #ElevatedButton("Agregar nuevo Tamaño", on_click=lambda _: self.nuevoTamano(page)),
                    ElevatedButton("Agregar nuevo Pico", on_click=lambda _: self.nuevoPico(page))            
                ]
            )
        )

        #SALTOS DE VISTAS
        #Contenedor del medio
        self.formulario = AnimatedSwitcher(
            self.contenedorInicio,
            expand=True, 
            transition=AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN
        )

        return View(
            "/liderPolitico",
            padding=5,
            controls=[
                self.appbar,

                Container(
                    padding=0,
                    margin=0,
                    content=Row(
                        alignment=CrossAxisAlignment.START,
                        controls=[
                            self.slider,
                            self.formulario
                        ]
                    )
                )
            ]
        )

#MOVERSE
    def animar(self, contenedor1, contenedor2, pageee):
        contenedor1 = contenedor1
        contenedor2 = contenedor2
        pageee = pageee

        self.formulario.content = contenedor2 if self.formulario.content == contenedor1 else contenedor1
        pageee.update()

    def cambiar_pagina(self, ye):
        ye = ye

        self.indicator.offset.y = ye
        self.indicator.update()

    def cambiarTitulo(self, pagee, titulo):
        pagee = pagee
        titulo = titulo

        self.titulo.value = titulo
        pagee.update()

    def quitarError(self, pagee, textfield):
        pagee = pagee
        textfield = textfield

        textfield.error_text = None
        pagee.update()

#OCULTAR Y MOSTRAR CONTRASENAS DE USUARIOS
    def regresarPassFalse(self, pagee):
        pagee = pagee

        if self.contrasena.visible == True:
            self.contrasena.visible = False
            self.btnCandado.icon = icons.LOCK_OUTLINE
            pagee.update()
        else:
            pass

    def revelarPass(self, pagee):
        pagee = pagee

        if self.contrasena.visible == False:
            self.btnCandado.icon = icons.LOCK_OPEN
            self.contrasena.visible = True
            pagee.update()
        else:
            self.btnCandado.icon = icons.LOCK_OUTLINE
            self.contrasena.visible = False
            pagee.update()

    def regresarPassFalseP(self, pagee):
        pagee = pagee

        if self.contrasenaP.visible == True:
            self.contrasenaP.visible = False
            self.btnCandadoP.icon = icons.LOCK_OUTLINE
            pagee.update()
        else:
            pass

    def revelarPassP(self, pagee):
        pagee = pagee

        if self.contrasenaP.visible == False:
            self.btnCandadoP.icon = icons.LOCK_OPEN
            self.contrasenaP.visible = True
            pagee.update()
        else:
            self.btnCandadoP.icon = icons.LOCK_OUTLINE
            self.contrasenaP.visible = False
            pagee.update()

#MODIFICAR PRECIOS
    def menuPrecios(self, pagee):
        pagee = pagee

        self.PrecioPequeña = TextField(label="Pequeña", hint_text="Ingresar precio", border_radius=30, border_color="#820000", width=150, height=60, on_change=lambda _:[self.quitarError(pagee, self.PrecioPequeña), logica.validarNumeros(self.PrecioPequeña, pagee)])
        self.PrecioMediana = TextField(label="Mediana", hint_text="Ingresar precio", border_radius=30, border_color="#820000", width=150, height=60, on_change=lambda _:[self.quitarError(pagee, self.PrecioMediana), logica.validarNumeros(self.PrecioMediana, pagee)])
        self.PrecioRegular = TextField(label="Regular", hint_text="Ingresar precio", border_radius=30, border_color="#820000", width=150, height=60, on_change=lambda _:[self.quitarError(pagee, self.PrecioRegular), logica.validarNumeros(self.PrecioRegular, pagee)])
        self.PrecioGrande = TextField(label="Grande", hint_text="Ingresar precio", border_radius=30, border_color="#820000", width=150, height=60, on_change=lambda _:[self.quitarError(pagee, self.PrecioGrande), logica.validarNumeros(self.PrecioGrande, pagee)])

        self.alertJornada = AlertDialog(
            modal=True,
            content=Column(
            height=400,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text("Ingrese los nuevos precios de los cilindros en los siguientes campos"),
                Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        self.PrecioPequeña,
                        self.PrecioMediana,
                        self.PrecioRegular,
                        self.PrecioGrande
                    ]
                )
            ]
            ),
            actions=[TextButton("Guardar", on_click=lambda _: self.validarPrecios(pagee)), TextButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertJornada))]
            )

        pagee.dialog = self.alertJornada
        self.alertJornada.open = True

        pagee.update()

    def validarPrecios(self, pageee):
        pageee = pageee
        if (self.PrecioPequeña.value == "") or (self.PrecioMediana.value == "") or (self.PrecioRegular.value == "") or (self.PrecioGrande.value == ""):
            if self.PrecioPequeña.value == "":
                self.PrecioPequeña.error_text = "Campo vacio, por favor seleccionar para continuar"
                pageee.update()

            if self.PrecioMediana.value == "":
                self.PrecioMediana.error_text = "Campo vacio, por favor seleccionar para continuar"
                pageee.update()

            if self.PrecioRegular.value == "":
                self.PrecioRegular.error_text = "Campo vacio, por favor seleccionar para continuar"
                pageee.update()
            
            if self.PrecioGrande.value == "":
                self.PrecioGrande.error_text = "Campo vacio, por favor seleccionar para continuar"
                pageee.update()
            else:
                return
        else:
            logica.consulta("UPDATE tamanos SET costo =? WHERE id = 1", [self.PrecioPequeña.value])
            logica.consulta("UPDATE tamanos SET costo =? WHERE id = 2", [self.PrecioMediana.value])
            logica.consulta("UPDATE tamanos SET costo =? WHERE id = 3", [self.PrecioRegular.value])
            logica.consulta("UPDATE tamanos SET costo =? WHERE id = 4", [self.PrecioGrande.value])
            self.cerrarAlertJornada(pageee, self.alertJornada)
            pageee.snack_bar = SnackBar(content=Text("Precios Actualizados Correctamente"), bgcolor="GREEN")
            pageee.snack_bar.open = True
            pageee.update()

    def cerrarAlertJornada(self, pageeee, alert):
        pageeee = pageeee
        alert = alert

        alert.open = False

        pageeee.update()

#GENERAR Y MOSTRAR INFORMACION DE LOS LIDERES
    def volverGenerarCartas(self, pageee):
        pageee = pageee

        self.columnaCards.controls = self.generarCards(pageee)

        pageee.update()

    def generarCards(self, pagee):
        pagee = pagee

        global cartas
        cartas = []

        querySelectJefe = "SELECT lideres.nombre, lideres.apellido, lideres.cedula FROM usuarios JOIN lideres ON lideres_id = lideres.id WHERE usuarios.nivel = 2"
        resultado = logica.consulta(querySelectJefe)

        for nom, ape, ci in resultado:
            cartas.append(
                Container(
                    bgcolor="RED",
                    height=150,
                    width=250,
                    padding=padding.all(7),
                    border_radius=border_radius.all(20),
                    on_click=lambda _, ci=ci: [self.generarJefe(ci, pagee), self.animar(self.formularioLiderCalle, self.formularioLiderCalle, pagee)],
                    content=Column(
                        controls=[
                            Text(f"{nom} {ape}", style=TextThemeStyle.TITLE_LARGE, color="WHITE"),
                            Text(f"{ci}", style=TextThemeStyle.TITLE_MEDIUM, color="WHITE"),
                        ]
                    )
                )
            )
            pagee.update()

        return cartas

    def generarJefe(self, jefee, pageee):
        jefee = jefee
        pageee = pageee

        resultadoUsuario = logica.consulta("SELECT lideres.nombre, lideres.apellido, lideres.cedula, lideres.ubicacion, preguntas.pregunta, respuestas.respuesta, usuarios.usuario, usuarios.contrasena, lideres.telefono, lideres.correo, usuarios.estatus FROM usuarios JOIN respuestas ON respuesta_id = respuestas.id JOIN preguntas ON preguntas_id = preguntas.id JOIN lideres ON lideres_id = lideres.id WHERE lideres.cedula = ?", [jefee])

        self.nombre.value = f"{resultadoUsuario[0][0]}"
        self.apellido.value = f"{resultadoUsuario[0][1]}"
        self.cedula.value = f"{resultadoUsuario[0][2]}"
        self.ubicacion.value = f"{resultadoUsuario[0][3]}"
        self.pregunta.value = f"{resultadoUsuario[0][4]}"
        self.respuesta.value = f"{resultadoUsuario[0][5]}"
        self.usuario.value = f"{resultadoUsuario[0][6]}"
        self.contrasena.value = f"{resultadoUsuario[0][7]}"
        self.telefono.value = f"{resultadoUsuario[0][8]}"
        self.correo.value = f"{resultadoUsuario[0][9]}"
        if resultadoUsuario[0][10] == 1:
            self.estatus.value = "Habilitado"
            self.check.value = False
        else:
            self.estatus.value = "inhabilitado"
            self.check.value = True

        pageee.update()

    def estatusUsuario(self, pagee):
        pagee = pagee

        if self.estatus.value == "Habilitado":
            self.check.value = True
            self.estatus.value = "Inhabilitado"
            logica.consulta("UPDATE usuarios SET estatus = 2 WHERE usuario = ?", [self.usuario.value])
        else:
            self.check.value = False
            self.estatus.value = "Habilitado"
            logica.consulta("UPDATE usuarios SET estatus = 1 WHERE usuario = ?", [self.usuario.value])

        pagee.update()

#GENERAR Y DESCARGAR ARCHIVOS DE LIDERES
    def volverGenerarArchivos(self, pagee):
        pagee = pagee

        self.bitacoraLista.clear()

        self.tablaSeleccionarHistorial.rows = self.generarArchivos(pagee)

        pagee.update()

    def generarArchivos(self, pageee):
        pageee = pageee

        his = []
        coun = 1

        resultadoId = logica.consulta("SELECT archivos_id FROM pedidos JOIN archivos ON archivos_id IS NOT NULL = archivos.id JOIN cilindros ON cilindros_id = cilindros.id JOIN jefesf ON jefesf_id = jefesf.id JOIN lideres ON lideres_id = lideres.id WHERE lideres.cedula = ? GROUP BY archivos_id", [self.cedula.value])

        for idss in resultadoId:

            datos = logica.consulta("SELECT fechaGenerado, id FROM archivos WHERE id = ?", [idss[0]])

            self.bitacoraLista.append([datos[0][0], datos[0][1]])

        for fecha, ids in self.bitacoraLista:
            his.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"Jornada {coun}")),
                    DataCell(Text(f"{fecha}")),
                ],
                on_select_changed=lambda _, fecha = fecha, ids = ids: [self.abrirHistorial(pageee, fecha, ids)]
            ),
            )
            coun = coun + 1

            pageee.update()

        return his

    def abrirHistorial(self, pagee, fechaa, idss):
        pagee = pagee
        fechaa = fechaa
        idss = idss

        self.tablaLlenarHistorial.rows = self.llenarHistroial(pagee, idss)

        #self.animar(self.contenedorLlenarHistorialJornada, self.contenedorLlenarHistorialJornada, pagee)

        self.alertHistorial = AlertDialog(
            modal=True,
            content=Column(
                controls=[
                    Text(f"Jornada realizada el {fechaa}"),
                    Container(
                        bgcolor="white",
                        height=550,
                        border_radius=border_radius.all(7),  
                        content=Column(
                            expand=True,
                            height=550,
                            scroll=ScrollMode.ALWAYS,
                            controls=[
                                self.tablaLlenarHistorial,
                            ]
                        )
                    ),
                ]
            ),
            actions=[ElevatedButton("Descargar Pdf", on_click=lambda _:self.descargarArchivo(pagee, self.alertHistorial, idss)), ElevatedButton("Regresar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertHistorial))]
        )

        pagee.dialog = self.alertHistorial
        self.alertHistorial.open = True

        pagee.update()

    def llenarHistroial(self, pageee, ids):
        pageee = pageee
        ids = ids

        contenido = []

        queryy = "SELECT pedidos.id, jefesf.ci, jefesf.nombre, jefesf.apellido, empresas.empresa, tamanos.tamano, picos.pico, pedidos.fechaAgregada FROM pedidos JOIN jefesf ON jefesf_id = jefesf.id JOIN cilindros ON cilindros_id = cilindros.id JOIN empresas ON cilindros.empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id JOIN lideres ON lideres_id = lideres.id WHERE archivos_id = ? ORDER BY jefesf.ci ASC"
        resultado = logica.consulta(queryy, [ids])

        for idss, cii, nom, ape, empresa, tamano, pico , fecha in resultado:
            contenido.append(DataRow(
                color="WHITE",
                cells=[
                    DataCell(Text(f"{cii}")),
                    DataCell(Text(f"{nom}")),
                    DataCell(Text(f"{ape}")),
                    DataCell(Text(f"{empresa}")),
                    DataCell(Text(f"{tamano}")),
                    DataCell(Text(f"{pico}")),
                    DataCell(Text(f"{fecha}")),
                ],
            ),
            )

            pageee.update()

        return contenido 

    def descargarArchivo(self, pageee, alertt, ids):
        pageee = pageee
        alertt = alertt
        ids = ids

        origen = logica.consulta("SELECT rutas FROM archivos WHERE id = ?", [ids])
        destino = os.path.join(os.path.join(os.environ['USERPROFILE']), rf'Desktop\Reportes')

        rutaEscritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), rf'Desktop\Reportes')

        if os.path.exists(rutaEscritorio) == True:
            pass
        else:
            os.mkdir(rutaEscritorio)

        shutil.copy(origen[0][0], destino)

        self.cerrarAlertJornada(pageee, alertt)
        pageee.snack_bar = SnackBar(content=Text("El PDF se descargo correctamente, puede visualizarlo en la caperta Reportes ubicada en el escritorio"), bgcolor="GREEN")
        pageee.snack_bar.open = True
        pageee.update()

    def volverGenerarBitacora(self, pagee, ci):
        pagee = pagee
        ci = ci

        resultadoBitacora = logica.consulta("SELECT bitacora.fechaEntrada , bitacora.fechaSalida FROM bitacora JOIN lideres ON lideres_id = lideres.id JOIN usuarios ON usuarios_id = usuarios.id WHERE lideres.cedula = ?", [ci.value])

        for entrada, salida in resultadoBitacora:
            self.listaBitacora.controls.append(Text(f"Entrada: {entrada}     Salida : {salida}"))
            pagee.update()

    def regresarViewFalse(self, pagee):
        pagee = pagee

        self.listaBitacora.controls.clear()
        pagee.update()

        if self.contrasena.visible == True:
            self.contrasena.visible = False
            self.btnCandado.icon = icons.LOCK_OUTLINE
            pagee.update()
        else:
            pass

    def volverCargarTusDatos(self, pagee):
        pagee = pagee

        resultadoUsuario = logica.consulta("SELECT lideres.nombre, lideres.apellido, lideres.cedula, lideres.ubicacion, preguntas.pregunta, respuestas.respuesta, usuarios.usuario, usuarios.contrasena, lideres.telefono, lideres.correo FROM usuarios JOIN respuestas ON respuesta_id = respuestas.id JOIN preguntas ON preguntas_id = preguntas.id JOIN lideres ON lideres_id = lideres.id WHERE lideres.id = ?", [logica.datoUser[0][0]])

        self.nombreLi.value = f"{resultadoUsuario[0][0]}"
        self.apellidoLi.value = f"{resultadoUsuario[0][1]}"
        self.cedulaLi.value = f"{resultadoUsuario[0][2]}"
        self.ubicacionLi.value = f"{resultadoUsuario[0][3]}"
        self.preguntaP.value = f"{resultadoUsuario[0][4]}"
        self.respuestaP.value = f"{resultadoUsuario[0][5]}"
        self.usuarioP.value = f"{resultadoUsuario[0][6]}"
        self.contrasenaP.value = f"{resultadoUsuario[0][7]}"
        self.telefonoLi.value = f"{resultadoUsuario[0][8]}"
        self.correoLi.value = f"{resultadoUsuario[0][9]}"

        pagee.update()

    def cerrarAlertJornada(self, pageeee, alert):
        pageeee = pageeee
        alert = alert

        alert.open = False

        pageeee.update()

#AGREGAR NUEVAS CARACTERISTICAS A UN CILINDRO
    def nuevaEmpresa(self, pagee):
        pagee = pagee

        self.alertNuevaEmpresa = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        Text("Añade una nueva empresa"),
                        self.entryEmpresa,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar", on_click=lambda _:self.ValidarEmpresa(pagee)),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertNuevaEmpresa))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertNuevaEmpresa
        self.alertNuevaEmpresa.open = True

        pagee.update()
    
    def ValidarEmpresa(self, pageee):
        pageee = pageee

        if (self.entryEmpresa.value == "") or (len(self.entryEmpresa.value) in range(1, 3)):
            if self.entryEmpresa.value == "":
                self.entryEmpresa.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(self.entryEmpresa.value) in range(1, 3):
                self.entryEmpresa.error_text = "Minimo de caracteres 3r"
                pageee.update()
        elif logica.consulta("SELECT empresa FROM empresas WHERE empresa = ?", [self.entryEmpresa.value]):
            pageee.snack_bar = SnackBar(content=Text("Esta Empresa ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        else:
            logica.consulta("INSERT INTO empresas VALUES (NULL, ?)", [self.entryEmpresa.value])
            self.cerrarAlertJornada(pageee, self.alertNuevaEmpresa)
            self.entryEmpresa.value = ""
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("La empresa se guardo correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def nuevoTamano(self, pagee):
        pagee = pagee

        self.alertNuevaTamano = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        Text("Añade un nuevo tamaño"),
                        self.entryTamano,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar", on_click=lambda _:self.ValidarTamano(pagee)),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertNuevaTamano))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertNuevaTamano
        self.alertNuevaTamano.open = True

        pagee.update()

    def ValidarTamano(self, pageee):
        pageee = pageee
        print(self.entryTamano.value)
        if (self.entryTamano.value == "") or (len(self.entryTamano.value) in range(1, 3)):
            if self.entryTamano.value == "":
                self.entryTamano.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(self.entryTamano.value) in range(1, 3):
                self.entryTamano.error_text = "Minimo de caracteres 3"
                pageee.update()
        elif logica.consulta("SELECT tamano FROM tamanos WHERE tamano = ?", [self.entryTamano.value]):
            pageee.snack_bar = SnackBar(content=Text("Esta Tamaño ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        else:
            logica.consulta("INSERT INTO tamanos VALUES (NULL, ?, 10)", [self.entryTamano.value])
            self.cerrarAlertJornada(pageee, self.alertNuevaTamano)
            self.entryTamano.value = ""
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El nuevo tamaño se guardo correctamente, debe establecerle un costo en el 'Inicio'"))
            pageee.snack_bar.open = True
            pageee.update()

    def nuevoPico(self, pagee):
        pagee = pagee

        self.alertNuevaPico = AlertDialog(
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        Text("Añade un nuevo tipo de pico"),
                        self.entryPico,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar", on_click=lambda _:self.ValidarPico(pagee)),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertNuevaPico))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertNuevaPico
        self.alertNuevaPico.open = True

        pagee.update()

    def ValidarPico(self, pageee):
        pageee = pageee

        if (self.entryPico.value == "") or (len(self.entryPico.value) in range(1, 3)):
            if self.entryPico.value == "":
                self.entryPico.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(self.entryPico.value) in range(1, 3):
                self.entryPico.error_text = "Minimo de caracteres 3r"
                pageee.update()
        elif logica.consulta("SELECT pico FROM picos WHERE pico = ?", [self.entryPico.value]):
            pageee.snack_bar = SnackBar(content=Text("Esta Tamaño ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        else:
            logica.consulta("INSERT INTO picos VALUES (NULL, ?)", [self.entryPico.value])
            self.cerrarAlertJornada(pageee, self.alertNuevaPico)
            self.entryPico.value = ""
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El nuevo tipo de pico se guardo correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

#EDITAR DATOS DEL JEFE DE FAMILIA 
    def editNombreLi(self, pagee, campo):
        pagee = pagee
        campo = campo

        self.entryNombre = TextField(label="Nombre", hint_text="Minimo 3 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryNombre), logica.validarNombres(self.entryNombre, pagee)])
        self.entryNombre.value = campo

        self.alertEditNombre = AlertDialog(
            modal=True,
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.entryNombre,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarNombreLi(pagee, self.entryNombre, "UPDATE lideres SET nombre = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditNombre))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditNombre
        self.alertEditNombre.open = True

        pagee.update()

    def editApellidoLi(self, pagee, campo):
        campo = campo
        pagee = pagee

        self.entryApellido = TextField(label="Apellido", hint_text="Minimo 4 caracteres", max_length=12, capitalization=TextCapitalization.SENTENCES, border_radius=30, border_color="#820000", width=300, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryApellido), logica.validarNombres(self.entryApellido, pagee)])
        self.entryApellido.value = campo

        self.alertEditApellido = AlertDialog(
            modal=True,
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.entryApellido,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarApellidoLi(pagee, self.entryApellido, "UPDATE lideres SET apellido = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditApellido))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditApellido
        self.alertEditApellido.open = True

        pagee.update()

    def editCedulaLi(self, pagee, tipo, cedula):
        pagee = pagee
        tipo = tipo
        cedula = cedula

        self.selectTipoCi = Dropdown(label="Tipo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(page, self.tipoCedula), options=[
                dropdown.Option("V"), dropdown.Option("E")])
        self.selectTipoCi.value = tipo
        self.entryCedula = TextField(label="Cedula", hint_text="Minimo 7 caracteres", border_color="#820000", border_radius=20, width=180, height=60, max_length=8, on_change=lambda _: [self.quitarError(pagee, self.entryCedula), logica.validarNumeros(self.entryCedula, pagee)])
        self.entryCedula.value = cedula

        self.alertEditCedula = AlertDialog(
            modal=True,
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=10,
                    controls=[
                        self.selectTipoCi,
                        self.entryCedula,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarCedulaLi(pagee, self.selectTipoCi, self.entryCedula, "SELECT lideres.nombre, lideres.apellido FROM lideres WHERE lideres.cedula = ?", "UPDATE lideres SET cedula = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditCedula))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditCedula
        self.alertEditCedula.open = True

        pagee.update()

    def editCorreoLi(self, pagee, correo):
        pagee = pagee
        correo = correo
        direccion = ""
        tipo = ""

        if correo.value[-10:] == "@gmail.com":
            direccion = correo.value[:-10]
            tipo = correo.value[-10:]
        else:
            direccion = correo.value[:-12]
            tipo = correo.value[-12:]

        self.entryCorreo = TextField(label="Direccion", hint_text="ej: clapcamoruco", border_color="#820000", border_radius=20, width=180, height=60, on_change=lambda _:[self.quitarError(pagee, self.entryCorreo), logica.validarCorreo(self.entryCorreo, pagee)])
        self.entryCorreo.value = direccion
        self.selectTipoCorreo = Dropdown(hint_text="Correo", color="black",border_color="#820000", border_radius=20, width=120, height=60, on_change=lambda _: self.quitarError(pagee, self.selectTipoCorreo), options=[
                dropdown.Option("@gmail.com"), dropdown.Option("@hotmail.com")])
        self.selectTipoCorreo.value = tipo

        self.alertEditCcorreo = AlertDialog(
            modal=True,
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=2,
                    controls=[
                        self.entryCorreo,
                        self.selectTipoCorreo,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarCorreoLi(pagee, self.selectTipoCorreo, self.entryCorreo, "SELECT lideres.nombre, lideres.apellido FROM lideres WHERE lideres.correo = ?", "UPDATE lideres SET correo = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditCcorreo))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditCcorreo
        self.alertEditCcorreo.open = True

        pagee.update()

    def editTelefonoLi(self, pagee, campo):
        pagee = pagee
        campo = campo

        codigo = campo.value[:4]
        telefono = campo.value[-7:]
        #self.telefonoJ.value[:4], self.telefonoJ.value[-7:]

        self.selectTipoTelefono = Dropdown(hint_text="Codigo", color="black",border_color="#820000", border_radius=20, width=100, height=60, on_change=lambda _: self.quitarError(pagee, self.selectTipoTelefono), options=[
                dropdown.Option("0412"), dropdown.Option("0414"), dropdown.Option("0416"), dropdown.Option("0424"), dropdown.Option("0238")])
        self.selectTipoTelefono.value = codigo
        self.entryTelefono = TextField(label="N telefono", hint_text="0000000", border_color="#820000", border_radius=20, width=180, height=60, max_length=7, on_change=lambda _: [self.quitarError(pagee, self.entryTelefono), logica.validarNumeros(self.entryTelefono, pagee)])
        self.entryTelefono.value = telefono

        self.alertEditTelefono = AlertDialog(
            modal=True,
            content=Container(
                alignment=alignment.center,
                height=150,
                width=300,
                bgcolor="white",
                content=Row(
                    spacing=2,
                    controls=[
                        self.selectTipoTelefono,
                        self.entryTelefono,
                    ]
                )
            ),
            actions=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("Guardar Cambios", on_click=lambda _:self.validarTelefonoLi(pagee, self.selectTipoTelefono, self.entryTelefono, "SELECT lideres.nombre, lideres.apellido FROM lideres WHERE lideres.telefono = ?", "UPDATE lideres SET telefono = ? WHERE id = ?")),
                        ElevatedButton("Cancelar", on_click=lambda _:self.cerrarAlertJornada(pagee, self.alertEditTelefono))
                    ]
                )
            ]
        )

        pagee.dialog = self.alertEditTelefono
        self.alertEditTelefono.open = True

        pagee.update()

    def validarNombreLi(self, pageee, campo, queryy):
        pageee = pageee
        campo = campo
        queryy = queryy

        if (campo.value == "") or (len(campo.value) in range(1, 3)):
            if campo.value == "":
                campo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(campo.value) in range(1, 3):
                campo.error_text = "Minimo de caracteres 3"
                pageee.update()
        else:
            logica.consulta(queryy, [campo.value, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.textoSlider.value = f"{campo.value}"
            self.volverCargarTusDatos(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditNombre)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El nombre se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarApellidoLi(self, pageee, campo, queryy):
        pageee = pageee
        campo = campo
        queryy = queryy

        if (campo.value == "") or (len(campo.value) in range(1, 4)):
            if campo.value == "":
                campo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()
            if len(campo.value) in range(1, 4):
                campo.error_text = "Minimo de caracteres 4"
                pageee.update()
        else:
            logica.consulta(queryy, [campo.value, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.apellidoLiderCalle = campo.value
            self.volverCargarTusDatos(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditApellido)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El apellido se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarCedulaLi(self, pageee, tipo, cedula, queryy, queryUpdate):
        pageee = pageee
        tipo = tipo
        cedula = cedula
        queryy = queryy
        queryUpdate = queryUpdate

        arregloCi = f"{tipo.value}-{cedula.value}"

        if (cedula.value == "") or (len(cedula.value) in range(1, 7)):
            if cedula.value == "":
                cedula.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if len(cedula.value) in range(1, 7):
                cedula.error_text = "Minimo de caracteres 7"
                pageee.update()

        elif logica.consulta(queryy, [arregloCi]):
            pageee.snack_bar = SnackBar(content=Text("Esta cedula ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloCi, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.volverCargarTusDatos(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditCedula)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("La cedula se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarCorreoLi(self, pageee, tipo, correo, queryy, queryUpdate):
        pageee = pageee
        tipo = tipo
        correo = correo
        queryy = queryy
        queryUpdate = queryUpdate

        arregloCorreo = f"{correo.value}{tipo.value}"

        if (correo.value == ""):
            if correo.value == "":
                correo.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

        elif logica.consulta(queryy, [arregloCorreo]):
            pageee.snack_bar = SnackBar(content=Text("Esta correo ya esta registrado"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloCorreo, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.volverCargarTusDatos(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditCcorreo)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El correo se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

    def validarTelefonoLi(self, pageee, codigo, telefono, queryy, queryUpdate):
        pageee = pageee
        codigo = codigo
        telefono = telefono
        queryy = queryy
        queryUpdate = queryUpdate

        arregloTelefono = f"{codigo.value}-{telefono.value}"

        if (telefono.value == "") or (len(telefono.value) in range(1, 7)):
            if telefono.value == "":
                telefono.error_text = "Campo vacio, por favor rellenelo para continuar"
                pageee.update()

            if len(telefono.value) in range(1, 7):
                telefono.error_text = "numero de telefono invalido"
                pageee.update()

        elif logica.consulta(queryy, [arregloTelefono]):
            pageee.snack_bar = SnackBar(content=Text("Esta numero de telefono ya esta registrada"))
            pageee.snack_bar.open = True
            pageee.update()
        
        else:
            logica.consulta(queryUpdate, [arregloTelefono, self.iDLiderCalle])
            #self.volverGenerarCartas(pageee)
            self.volverCargarTusDatos(pageee)
            self.cerrarAlertJornada(pageee, self.alertEditTelefono)
            pageee.snack_bar = SnackBar(bgcolor="GREEN", content=Text("El numero de telefono se modifico correctamente"))
            pageee.snack_bar.open = True
            pageee.update()

#SALIR
    def salir(self, pages):
        self.pages = pages

        fechaS = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        logica.consulta("UPDATE bitacora SET fechaSalida = ? WHERE fechaEntrada = ? AND usuarios_id = ?", [fechaS, self.fechaEntradaUser, self.idUsuario])
        self.pages.go("/")
        logica.datoUser.clear()