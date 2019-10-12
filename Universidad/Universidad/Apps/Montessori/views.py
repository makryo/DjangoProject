# Create your views here.
from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from django.views.generic import DetailView
from Universidad.Apps.Montessori.models import Alumno


class ReporteAlumno(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.MEDIA_ROOT + '/imagenes/logo_monte.png'

        pdf.drawImage(archivo_imagen, 40, 750, 120, 90, preserveAspectRatio=True)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='Universidad/Apps/Montessori/Migrations/Alumno.html')
        buffer = BytesIO()

        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        pdf.setFont("Helvetica", 16)

        pdf.drawString(230, 79, u"Colegio Montessori")
        pdf.setFont("Helvetica", 16)

        pdf.drawString(200, 770, u"Reporte de alumnos")
        return response

def tabla(self,pdf,y):

    encabezados=('Codigo', 'Primer Nombre', 'Segundo Nombre', 'Apellido Paterno', 'Apellido Materno',
                 'Fecha de Nacimiento', 'Genero')
    detalles = [(Alumno.Codigo, Alumno.Nombre1, Alumno.Nombre2, Alumno.ApellidoP,
                 Alumno.ApellidoM, Alumno.FechaNacimiento, Alumno.GENERO)]

    detalle_orden = Table([encabezados]+ detalles, colWidths=[2, 5, 5, 5])

    detalle_orden.setStyle(TableStyle(
        [
            ('ALIGN', (0, 0), (3, 0), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]

    ))

    detalle_orden.wrapOn(pdf, 800, 600)
    detalle_orden.wrapOn(pdf, 60, y)

