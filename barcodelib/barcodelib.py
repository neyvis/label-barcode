# -*- coding: utf-8 -*-
import os

from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.para import Paragraph
from reportlab.graphics.barcode import createBarcodeDrawing


class BarCode(object):

    def generate_barcode(
            self,
            value,
            left_margin,
            bottom_margin,
            out_dir,
            logo_path,
            description,
            page_size=(200, 100,)
    ):
        """
        Generates a barcode from a value and save it on a PDF file.

        e.g
        >> from barcodelib import BarCode
        >> BarCode().generate_barcode('SBLS12-12', 2.8, 2, '.', logo_path=logo_dir, description="Stailess Style Standoff Diameter: 1/2, Standoff: 1/2 Satin Finish (For Inside Use Only)")

        :param left_margin:
        :param bottom_margin:
        :param out_dir:
        :return:
        """
        width, height = page_size
        value = str(value)
        filename = 'barcode_%s.pdf' % value
        file_path = os.path.join(out_dir, filename)
        c = canvas.Canvas(file_path, pagesize=page_size)
        c.drawImage(logo_path, 5, height-35, height=30, width=30)
        # stamp the bar code
        # drawOn puts the barcode on the canvas at the specified coordinates
        # stamp the bar code
        d = Drawing(50, 10)
        d.add(createBarcodeDrawing(
            'Standard39',
            value=value,
            barHeight=10 * mm,
            humanReadable=True,
            checksum=0
        ))
        # drawOn puts the barcode on the canvas at the specified coordinates
        d.drawOn(c, left_margin * cm, bottom_margin * cm)

        styles = getSampleStyleSheet()
        p = Paragraph(
            '<font size="10">{}</font>'.format(description),
            styles["Normal"]
        )
        p.wrapOn(c, width - 85, height)
        p.drawOn(c, 51, 10)

        # now create the actual PDF
        c.showPage()
        c.save()
        return file_path
