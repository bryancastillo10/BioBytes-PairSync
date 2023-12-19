from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.max_value = 100
        self.progress_color = QColor(qRgb(80, 250, 123))

        # TEXT
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = QColor(qRgb(80, 250, 123))

        # BG
        self.enable_bg = True
        self.bg_color = QColor(qRgb(54, 54, 54))

        # SET DEFAULT SIZE WITHOUT A LAYOUT
        self.resize(self.width, self.height)

    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    def set_value(self, value):
        """SET VALUE"""
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        """SET PROGRESS PARAMETERS"""
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = int(self.progress_width / 2)
        value = int(self.value * 360 / self.max_value)
        alen = int(-value * 16)

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        # ROUNDED CAP
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 5760)

        # CREATE ARC / CIRCULAR PROGRESS
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, alen)

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # END
        paint.end()
