from fpdf import FPDF
from flet import *
from datetime import datetime
import pathlib
import logica
import os
import shutil


class Pdf(FPDF):
        

    def __init__(self):
        self.Header()

    def Header(self):
        self.idPedidos = []
        resultadoPrecios = logica.consulta("SELECT costo FROM tamanos")
        #self.resultadosiDPedidos = logica.consulta("SELECT pedidos.id FROM pedidos JOIN jefesF_Cilindros ON pedidos.jefesF_Cilindros_id = jefesF_Cilindros.id JOIN jefesf ON jefesF_Cilindros.jefesf_id = jefesf.id JOIN cilindros ON jefesF_Cilindros.cilindros_id = cilindros.id JOIN empresas ON cilindros.empresas_id = empresas.id JOIN tamano ON cilindros.tamano_id = tamano.id JOIN picos ON cilindros.picos_id = picos.id WHERE liderCalle_id =? AND pedidos.fecha IS NULL", [logica.datoUser[0][0]])
        
        #------------------Definir tipo de hoja----------------
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        self.pdf.add_page()

        #---------------------Insertar Logo-------------------------------

        self.pdf.image(f"{logica.rutaactual}\img\clap.png", x = 45, y = 5, w = 120, h = 35)
        #self.pdf.image("SistemaClapFlet\img\clap.png", x = 45, y = 5, w = 120, h = 35)
        self.pdf.rect(x = 0, y = 45, w = 210, h = 0)

        #---------------------Título del Pdf---------------------------
        self.fecha = datetime.today().strftime('%d-%m-%Y')
        self.pdf.set_font("Times", "B", 25)
        self.pdf.set_y(55)
        self.pdf.cell(w = 0, h = 15, txt = "Reporte de cilindros", align = "C", border = 0, fill = 0, ln=1)
        self.pdf.set_font("Times", "U", 12)
        self.pdf.multi_cell(w = 0, h = 10, txt = f"{logica.datoUser[0][1]} {logica.datoUser[0][2]}", align = "C", border = 0, fill = 0)
        self.pdf.multi_cell(w = 0, h = 10, txt = f"{logica.datoUser[0][3]}", align = "C", border = 0, fill = 0)
        self.pdf.multi_cell(w = 0, h = 10, txt = f"Altagracia de Orituco {self.fecha}", border = 0, align = "C", fill = 0)
        self.pdf.multi_cell(w = 0, h = 10, txt = f"Precio Unitario:       Pequeñas={resultadoPrecios[0][0]}Bs    Medianas={resultadoPrecios[1][0]}Bs    Regulares={resultadoPrecios[2][0]}Bs    Grandes={resultadoPrecios[3][0]}Bs", align = "C", border = 0, fill = 0)
        
        self.Body()

    def Body(self):

        #---------------------Tabla-------------------------------
        self.pdf.set_font("Times", "", 14)
        self.pdf.set_y(115)
        self.pdf.set_fill_color(r = 239, g = 71, b = 71)
        self.pdf.cell(w = 27, h = 15, txt = "Cédula", border = 1, align = "C", fill = 1)
        self.pdf.cell(w = 27, h = 15, txt = "Nombre", border = 1, align = "C", fill = 1)
        self.pdf.cell(w = 27, h = 15, txt = "Apellido", border = 1, align = "C", fill = 1)
        self.pdf.cell(w = 27, h = 15, txt = "Empresa", border = 1, align = "C", fill = 1)
        self.pdf.cell(w = 27, h = 15, txt = "Pico", border = 1, align = "C", fill = 1) 
        self.pdf.cell(w = 27, h = 15, txt = "Tamaño", border = 1, align = "C", fill = 1) 
        self.pdf.multi_cell(w = 27, h = 15, txt = "Agregado", border = 1, align = "C", fill = 1)

        #----------------------------------Lista-------------------------------------

        queryy = "SELECT pedidos.id, jefesf.ci, jefesf.nombre, jefesf.apellido, empresas.empresa, picos.pico, tamanos.tamano, tamanos.costo, pedidos.fechaAgregada FROM pedidos JOIN jefesf ON jefesf_id = jefesf.id JOIN cilindros ON cilindros_id = cilindros.id JOIN empresas ON empresas_id = empresas.id JOIN tamanos ON tamanos_id = tamanos.id JOIN picos ON picos_id = picos.id WHERE lideres_id =? AND pedidos.archivos_id IS NULL ORDER BY jefesf.ci ASC"
        
        c = 0

        contP = 0
        contM = 0
        contR = 0
        contG = 0

        valorP = 0
        valorM = 0
        valorR = 0
        valorG = 0

        totalP = 0
        totalM = 0
        totalG = 0
        totalR = 0

        self.informacion = logica.consulta(queryy, [logica.datoUser[0][0]])
        #-----------------------------Cliclo For-----------------------------------------
        for ids, ci, nom, ape, emp, pic, tamn, cos, fech in self.informacion:
            
            if tamn == "Pequeña":
                contP = contP + 1
                totalP = valorP + cos
                valorP = totalP

            elif tamn == "Mediana":
                contM = contM + 1
                totalM = valorM + cos
                valorM = totalM

            elif tamn == "Regular":
                contR = contR + 1
                totalR = valorR + cos
                valorR = totalR

            elif tamn == "Grande":
                contG = contG + 1
                totalG = valorG + cos
                valorG = totalG
            else: pass
            

            c+=1
            if(c%2==0):self.pdf.set_fill_color(r = 209, g = 209, b = 209)
            else:self.pdf.set_fill_color(r = 255, g = 255, b = 255)

            self.pdf.set_font("Times", "", 12)
            self.pdf.set_draw_color(r = 239, g = 71, b = 71)
            self.pdf.cell(w = 27, h = 10, txt = str(ci), border = "TBL", align = "C", fill = 1)
            self.pdf.cell(w = 27, h = 10, txt = str(nom), border = "TB", align = "C", fill = 1)
            self.pdf.cell(w = 27, h = 10, txt = str(ape), border = "TB", align = "C", fill = 1)
            self.pdf.cell(w = 27, h = 10, txt = str(emp), border = "TB", align = "C", fill = 1)
            self.pdf.cell(w = 27, h = 10, txt = str(pic), border = "TB", align = "C", fill = 1) 
            self.pdf.cell(w = 27, h = 10, txt = str(tamn), border = "TB", align = "C", fill = 1) 
            self.pdf.multi_cell(w = 27, h = 10, txt = str(fech), border = "TBR", align = "C", fill = 1)

            self.idPedidos.append(ids)

        totalVenta = totalP + totalM + totalR + totalG
        self.pdf.multi_cell(w = 0, h = 10, txt = f"Cantidad:       Pequeñas={contP}    Medianas={contM}    Regulares={contR}    Grandes={contG} Monto Total: {totalVenta}Bs", align = "C", border = 0, fill = 2)

        self.pdf.multi_cell(w = 0, h = 10, txt = f"Observaciones:", align = "C", border = 0, fill = 3)

        self.Footer()

    def Footer(self):
        rutaActual = pathlib.Path(__file__).parent.absolute()
        nombreArchivo = f'jornada_venta_de_gas_{logica.datoUser[0][1]}_{self.fecha}.pdf'
        rutaEscritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), rf'Desktop\Reportes')

        self.fecha = datetime.today().strftime('%d-%m-%Y')

        if os.path.exists(rutaEscritorio) == True:
            pass
        else:
            os.mkdir(rutaEscritorio)

        #queryFormat = "DELETE FROM sqlite_sequence WHERE name = 'pedidos'"
        #--------------------------Pie de pagina------------------------------------

        self.pdf.output(rf'{rutaActual}\Reportes\{nombreArchivo}')
        self.pdf.output(rf'{rutaEscritorio}\{nombreArchivo}')

        logica.consulta("INSERT INTO archivos VALUES (NULL, ?, ?)", [rf'{rutaActual}\Reportes\{nombreArchivo}', self.fecha])
        resultadoIdArchivo = logica.consulta("SELECT id FROM archivos WHERE rutas = ? AND fechaGenerado = ?", [rf"{rutaActual}\Reportes\{nombreArchivo}", self.fecha])


        for i in self.idPedidos:
            logica.consulta(("UPDATE pedidos SET archivos_id = ? WHERE id = ?"), [resultadoIdArchivo[0][0], i])
        self.idPedidos.clear()

        #logica.consulta(queryFormat)