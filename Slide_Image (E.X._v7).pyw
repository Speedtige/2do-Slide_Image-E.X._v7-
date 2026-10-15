


# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Desarrollado por: 👉 Cristian M. Veliz Cano ✔
Versión del Soft: 👉 V-07 (E.X._v7)
Nombre del Soft: ✨ Slide Image Viewer ✨
✨ Visor Universal de Imágenes Multi-Formato ✨

✨ Slide Image Viewer ✨
✨ FRONTEND MODERNO CON PANEL DE MINIATURAS ✨

✅ Este Soft-Ware fue diseñado para facilitar la visualización,
navegación y gestión de imágenes desde múltiples fuentes de datos
en una interfaz gráfica limpia, minimalista y altamente funcional.

⚙️ El funcionamiento del Programa es Directo:

📄 El Usuario puede cargar imágenes desde archivos locales,
bases de datos SQLite BLOB, recursos QRC compilados de PyQt,
o archivos JSON con datos Base64, todo desde una única ventana.

⭐ El Soft-Ware permite trabajar con:

✔ Archivos Individuales de Imagen (Drag & Drop soportado)
✔ Directorios Completos (incluyendo subcarpetas recursivas)
✔ Bases de Datos SQLite (detección automática de tablas BLOB)
✔ Recursos QRC de PyQt (resources_rc.py + .qrc sin extraer)
✔ Archivos JSON (Base64, URLs remotas o rutas locales)
✔ Slideshow automático con temporizador configurable (5s)
✔ Navegación intuitiva (teclado, botones y rueda del mouse)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Nota Importante:

➜ Este Soft-Ware trabaja completamente de forma Local.

✔ No requiere conexión a Internet (excepto para URLs en JSON).
✔ No utiliza Servicios Externos obligatorios.
✔ No transmite Información.
✔ No realiza Sincronizaciones Remotas.

💯% OFF-LINE para todas las funciones principales.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 Ejemplos de JSON Soportados
{
    "galeria": [
        {
            "nombre": "foto_normal.png",
            "data": "iVBORw0KGgoAAAANSUhEUgAA..."
        },
        {
            "nombre": "comprimida.jxl",
            "data": "/woAASsKGgoBAEBCDg4OHwAA..."
        },
        {
            "path": "imagenes/local/foto.jpg"
        },
        {
            "path": "imagenes/local/comprimida.jxl"
        },
        {
            "url": "https://ejemplo.com/imagen.webp"
        }
    ]
}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ Atajos del Teclado:

📎 F1
• Para mostrar información del software.

📎 CTRL+I
• Cargar archivos de imagen individuales.

📎 CTRL+C
• Cargar imágenes desde una carpeta.

📎 CTRL+D
• Cargar imágenes desde directorio (recursivo).

📎 CTRL+B
• Cargar imágenes desde Base de Datos SQLite BLOB.

📎 CTRL+R
• Explorar y cargar recursos QRC de PyQt5/6.

📎 CTRL+J
• Cargar imágenes desde archivo JSON (Base64/URLs).

📎 CTRL+C (sobre imagen)
• Copiar la imagen actual al portapapeles.

📎 ← → (Flechas)
• Navegar entre imágenes (anterior/siguiente).

📎 Rueda del Mouse
• Navegación rápida (arriba=anterior, abajo=siguiente).

📎 Click Mouse / Espacio
• Pausar/Reanudar el slideshow automático.

📎 ESC
• Cierra inmediatamente el Soft-Ware.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Licencia:

MIT License

Copyright (c) 2026 Cristian M. Veliz Cano

Se concede permiso, de forma gratuita, a cualquier persona
que obtenga una copia de este software y de los archivos de
documentación asociados, para utilizar el Software sin
restricción, incluyendo sin limitación los derechos de uso,
copia, modificación, fusión, publicación, distribución,
sublicencia y/o venta de copias del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL",
SIN GARANTÍA DE NINGÚN TIPO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 De Caracter Gratuito, Portable,
🎭 Open-Source, Didáctico y Free-Code.

🛠️ Diseñado para Visualización Rápida,
Desarrollo de Software, Testing de Recursos
y Administración de Assets Gráficos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Estructura Interna de Datos:

➜ Tupla de Imagen: (tipo, nombre, datos)
➜ • tipo: 'file' | 'blob' | 'qrc' | 'json'
➜ • nombre: str (nombre de archivo para mostrar)
➜ • datos: str (ruta) | bytes (BLOB) | str (recurso Qt)

➜ Sistema de Renderizado Unificado:
➜ • Soporte QPixmap nativo de Qt
➜ • Escalado automático manteniendo aspecto
➜ • Cacheo en memoria de pixmaps actuales

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Un Visor Universal que une Archivos Locales, Bases de Datos,
Recursos Compilados y JSON en una sola ventana fluida."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 class ImageSlider:
   ├── def initUI(self)...
   ├── def load_from_blob(self)...
   ├── def load_from_qrc(self)...
   ├── def load_from_database(self)...
   ├── def load_from_qrc_list(self)...
   ├── def update_image(self)...
   ├── def next_image(self)...
   ├── def previous_image(self)...
   ├── def add_images(self)...
   ├── def add_images_carpeta(self)...
   ├── def add_images_directorys(self)...
   ├── def In_Im_Extern_Path(self)...
   ├── def create_context_menu(self)...
   ├── def prompt_load_database(self)...
   ├── 
   ├── def prompt_load_qrc(self):
   │     """Explorador de QRC..."""
   │     # ... código completo ...
   │
   └── def dragEnterEvent(self)...

Soft´Ware:
https://mega.nz/file/28NGxSYC#jaeVW_Lf6iGnE6V0gwXSjFusVSLNVvtWlFbNpukOE3U
'''
##=========================================================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu, QAction, QFileDialog, QVBoxLayout, 
    QWidget, QPushButton, QMessageBox, QShortcut, QHBoxLayout, QSplitter, QListWidget, QListWidgetItem, 
    QSpinBox, QSlider, QFrame, QSizePolicy, QGridLayout, QProgressBar, QStatusBar, QToolButton, QStyle)
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QFont, QPalette, QIcon, QKeySequence, QColor
from PyQt5.QtCore import QTimer, Qt, QMimeData, QFile, QIODevice, QSize

import sys, os
import sqlite3
import xml.etree.ElementTree as ET
import json
import base64
import re
import urllib.request
import tempfile
import cv2
import numpy as np
from io import BytesIO

from PIL import Image
import pillow_jxl
from pillow_jxl import Decoder

##====================================================================================
# --- Clase para manejo de rutas de recursos ---
##====================================================================================
class Path:
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # =========================
    # ✨ Devuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================

    @staticmethod
    def resource_path_app():
        try:
            path_app = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
        except Exception as e:
            print(e)
        return path_app

##====================================================================================
# --- Clase Principal ---
##====================================================================================
class ImageSlider(QMainWindow):
    def __init__(self, in_im=None, master=None):
        super().__init__(master)
        self.in_im = in_im
        self.images = []
        self.current_index = 0
        self.current_pixmap = None
        self.original_pixmap = None  # Para efectos (saturación)
        self.paused = False
        self.Full_Screnn_Window = False
        self.Esconder = False
        self.resize_labl = True
        
        # Variables de tiempo
        self.Times_Stamp = 5000  # 5 segundos por defecto
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_image)
        self.timer.start(self.Times_Stamp)
        
        self.initUI()
        if self.in_im:
            self.In_Im_Extern_Path()

    def initUI(self):
        self.setWindowTitle('Slide_Image (E.X._v7)')
        self.setMinimumSize(1000, 600)
        self.center_on_screen()
        
        # Icono
        self.Ico_app = Path.resource_path('Ico\\1.png')
        self.setWindowIcon(QtGui.QIcon(self.Ico_app))
        
        # ============================================
        # ESTILOS CSS MODERNOS (DARK THEME)
        # ============================================
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0d0d15;
            }
            QWidget {
                background-color: #0d0d15;
                color: #e0e0e0;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            /* Panel de miniaturas */
            QListWidget {
                background-color: #1a1a2e;
                border: none;
                border-right: 2px solid #0f3460;
                outline: none;
                padding: 5px;
            }
            QListWidget::item {
                background-color: #16213e;
                border: 2px solid transparent;
                border-radius: 8px;
                margin: 4px;
                padding: 4px;
            }
            QListWidget::item:selected {
                background-color: #0f3460;
                border: 2px solid #00c3ff;
            }
            QListWidget::item:hover {
                background-color: #1e3a5f;
            }
            QScrollBar:vertical {
                background-color: #1a1a2e;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #0f3460;
                border-radius: 6px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #00c3ff;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            /* Botones modernos */
            QPushButton {
                background-color: #0f3460;
                color: #00c3ff;
                border: 1px solid #00c3ff;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #00c3ff;
                color: #0d0d15;
            }
            QPushButton:pressed {
                background-color: #0099cc;
            }
            QPushButton:disabled {
                background-color: #1a1a2e;
                color: #555;
                border-color: #333;
            }
            
            /* Botón especial SLIDE SHOW */
            QPushButton#btn_slideshow {
                background-color: #00c3ff;
                color: #0d0d15;
                font-weight: bold;
                min-width: 180px;
            }
            QPushButton#btn_slideshow:hover {
                background-color: #33d1ff;
            }
            QPushButton#btn_slideshow[active="false"] {
                background-color: #ff4757;
                color: white;
            }
            
            /* SpinBox */
            QSpinBox {
                background-color: #16213e;
                border: 1px solid #0f3460;
                border-radius: 4px;
                padding: 5px;
                color: #00c3ff;
                font-weight: bold;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                background-color: #0f3460;
                border-radius: 2px;
                width: 20px;
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background-color: #00c3ff;
            }
            
			/* Slider horizontal (Saturación) */
            QSlider::groove:horizontal {
                background: #16213e;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #00c3ff;
                width: 18px;
                height: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QSlider::handle:horizontal:hover {
                background: #33d1ff;
            }
            QSlider::sub-page:horizontal {
                background: #0f3460;
                border-radius: 4px;
            }
            QSlider::add-page:horizontal {
                background: #16213e;
                border-radius: 4px;
            }
            
            /* Labels informativos */
            QLabel#info_label {
                color: #888;
                font-size: 11px;
                padding: 2px 10px;
            }
            QLabel#info_label_value {
                color: #00c3ff;
                font-size: 11px;
                font-weight: bold;
                padding: 2px 5px;
            }
            
            /* Barra de estado inferior */
            QFrame#status_frame {
                background-color: #1a1a2e;
                border-top: 2px solid #0f3460;
            }
            
            /* Botones de navegación flotantes */
            QPushButton#nav_btn {
                background-color: rgba(0, 195, 255, 0.3);
                color: white;
                border: 2px solid rgba(0, 195, 255, 0.6);
                border-radius: 25px;
                font-size: 20px;
                font-weight: bold;
                min-width: 50px;
                min-height: 50px;
            }
            QPushButton#nav_btn:hover {
                background-color: rgba(0, 195, 255, 0.6);
                border-color: #00c3ff;
            }
        """)
        
        # ============================================
        # WIDGET CENTRAL CON SPLITTER
        # ============================================
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        main_layout = QHBoxLayout(self.central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Splitter para redimensionar paneles
        self.splitter = QSplitter(Qt.Horizontal)
        
        # ============================================
        # PANEL IZQUIERDO: MINIATURAS
        # ============================================
        self.thumbnail_panel = QWidget()
        thumb_layout = QVBoxLayout(self.thumbnail_panel)
        thumb_layout.setContentsMargins(5, 5, 5, 5)
        
        # Label título del panel
        thumb_title = QLabel("📷 Miniaturas")
        thumb_title.setStyleSheet("color: #00c3ff; font-weight: bold; font-size: 12px; padding: 5px;")
        thumb_title.setAlignment(Qt.AlignCenter)
        thumb_layout.addWidget(thumb_title)
        
        # Lista de miniaturas
        self.thumbnail_list = QListWidget()
        self.thumbnail_list.setIconSize(QSize(120, 90))
        self.thumbnail_list.setSpacing(5)
        self.thumbnail_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.thumbnail_list.itemClicked.connect(self.on_thumbnail_clicked)
        thumb_layout.addWidget(self.thumbnail_list)
        
        # Contador de imágenes
        self.img_counter = QLabel("0 / 0 imágenes")
        self.img_counter.setStyleSheet("color: #888; font-size: 10px;")
        self.img_counter.setAlignment(Qt.AlignCenter)
        thumb_layout.addWidget(self.img_counter)
        
        self.splitter.addWidget(self.thumbnail_panel)
        self.thumbnail_panel.setFixedWidth(150)
        
        # ============================================
        # PANEL CENTRAL: VISOR + CONTROLES
        # ============================================
        center_panel = QWidget()
        center_layout = QVBoxLayout(center_panel)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)
        
        # --- Área de imagen ---
        self.image_container = QWidget()
        self.image_container.setStyleSheet("background-color: #0d0d15;")
        img_layout = QVBoxLayout(self.image_container)
        img_layout.setContentsMargins(0, 0, 0, 0)
        
        # Label para mostrar imagen
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: #0d0d15;")
        img_layout.addWidget(self.label)
        
        # Botones de navegación flotantes (posicionados en resizeEvent)
        self.left_button = QPushButton("◀", self.image_container)
        self.left_button.setObjectName("nav_btn")
        self.left_button.setFixedSize(50, 50)
        self.left_button.clicked.connect(self.previous_image)
        self.left_button.raise_()
        
        self.right_button = QPushButton("▶", self.image_container)
        self.right_button.setObjectName("nav_btn")
        self.right_button.setFixedSize(50, 50)
        self.right_button.clicked.connect(self.next_image)
        self.right_button.raise_()
        
        center_layout.addWidget(self.image_container, stretch=1)
        
        # ============================================
        # BARRA DE CONTROLES SUPERIOR (Botones de entrada)
        # ============================================
        controls_frame = QFrame()
        controls_frame.setStyleSheet("""
            QFrame {
                background-color: #1a1a2e;
                border-top: 2px solid #0f3460;
                border-bottom: 2px solid #0f3460;
            }
        """)
        controls_layout = QHBoxLayout(controls_frame)
        controls_layout.setContentsMargins(10, 5, 10, 5)
        controls_layout.setSpacing(8)
        
        # Botón SLIDE SHOW
        self.btn_slideshow = QPushButton("▶ SLIDE SHOW: ON")
        self.btn_slideshow.setObjectName("btn_slideshow")
        self.btn_slideshow.setProperty("active", "true")
        self.btn_slideshow.clicked.connect(self.toggle_slideshow)
        controls_layout.addWidget(self.btn_slideshow)
        
        # SpinBox para tiempo
        time_layout = QHBoxLayout()
        time_layout.setSpacing(3)
        time_label = QLabel("⏱️")
        time_label.setStyleSheet("font-size: 14px;")
        time_layout.addWidget(time_label)
        
        self.spin_time = QSpinBox()
        self.spin_time.setRange(1, 60)
        self.spin_time.setValue(5)
        self.spin_time.setSuffix(" s")
        self.spin_time.setToolTip("Segundos entre diapositivas")
        self.spin_time.valueChanged.connect(self.update_timer_interval)
        time_layout.addWidget(self.spin_time)
        
        controls_layout.addLayout(time_layout)
        controls_layout.addSpacing(20)
        
        # Separador
        line1 = QFrame()
        line1.setFrameShape(QFrame.VLine)
        line1.setStyleSheet("color: #0f3460;")
        controls_layout.addWidget(line1)
        controls_layout.addSpacing(10)
        
        # Botones de carga (IN DB, IN JS, IN RC, ONLY -IN-, CLEAN)
        self.btn_in_db = QPushButton("🗃️ IN DB")
        self.btn_in_db.setToolTip("Cargar desde Base de Datos (Ctrl+B)")
        self.btn_in_db.clicked.connect(self.prompt_load_database)
        controls_layout.addWidget(self.btn_in_db)
        
        self.btn_in_js = QPushButton("📄 IN JS")
        self.btn_in_js.setToolTip("Cargar desde JSON (Ctrl+J)")
        self.btn_in_js.clicked.connect(self.prompt_load_json)
        controls_layout.addWidget(self.btn_in_js)
        
        self.btn_in_rc = QPushButton("📦 IN RC")
        self.btn_in_rc.setToolTip("Cargar desde Recursos QRC (Ctrl+R)")
        self.btn_in_rc.clicked.connect(self.prompt_load_qrc)
        controls_layout.addWidget(self.btn_in_rc)
        
        self.btn_only_in = QPushButton("📂 ONLY -IN-")
        self.btn_only_in.setToolTip("Cargar archivos normales (Ctrl+I/C/D)")
        self.btn_only_in.clicked.connect(self.selectet_directory_or_file)
        controls_layout.addWidget(self.btn_only_in)
        
        self.btn_clean = QPushButton("🗑️ CLEAN")
        self.btn_clean.setToolTip("Limpiar todo (Ctrl+L)")
        self.btn_clean.setStyleSheet("""
            QPushButton {
                background-color: #ff4757;
                color: white;
                border-color: #ff6b7a;
            }
            QPushButton:hover {
                background-color: #ff6b7a;
            }
        """)
        self.btn_clean.clicked.connect(self.cleanear)
        controls_layout.addWidget(self.btn_clean)
        
        controls_layout.addStretch()

		# Slider de saturación con label (HORIZONTAL)
        sat_layout = QHBoxLayout()
        sat_layout.setSpacing(10)
        
        self.sat_label = QLabel("Saturación:")
        self.sat_label.setStyleSheet("color: #888; font-size: 11px;")
        sat_layout.addWidget(self.sat_label)
        
        self.Slide_Saturacion = QSlider(Qt.Horizontal)
        self.Slide_Saturacion.setRange(0, 200)
        self.Slide_Saturacion.setValue(100)
        self.Slide_Saturacion.setFixedWidth(83)
        self.Slide_Saturacion.setToolTip("Ajustar saturación (0-200%)")
        self.Slide_Saturacion.valueChanged.connect(self.on_saturation_changed)
        sat_layout.addWidget(self.Slide_Saturacion)
        
        self.sat_value = QLabel("100%")
        self.sat_value.setStyleSheet("color: #00c3ff; font-size: 11px; font-weight: bold; min-width: 40px;")
        sat_layout.addWidget(self.sat_value)
        
        controls_layout.addLayout(sat_layout)
        
        # Botón pantalla completa
        self.btn_fullscreen = QPushButton("⛶")
        self.btn_fullscreen.setToolTip("Pantalla completa")
        self.btn_fullscreen.setFixedSize(40, 40)
        self.btn_fullscreen.setStyleSheet("font-size: 16px;")
        self.btn_fullscreen.clicked.connect(self.Pantalla_Completa)
        controls_layout.addWidget(self.btn_fullscreen)
        
        center_layout.addWidget(controls_frame)
        
        # ============================================
        # BARRA DE INFORMACIÓN INFERIOR
        # ============================================
        self.status_frame = QFrame()
        self.status_frame.setObjectName("status_frame")
        self.status_frame.setFixedHeight(35)
        status_layout = QHBoxLayout(self.status_frame)
        status_layout.setContentsMargins(15, 5, 15, 5)
        status_layout.setSpacing(20)
        
        # Info: Origen
        self.info_source_label = QLabel("Origen:")
        self.info_source_label.setObjectName("info_label")
        status_layout.addWidget(self.info_source_label)
        
        self.info_source = QLabel("Ninguno")
        self.info_source.setObjectName("info_label_value")
        status_layout.addWidget(self.info_source)
        
        status_layout.addSpacing(30)
        
        # Info: Nombre
        self.info_name_label = QLabel("Archivo:")
        self.info_name_label.setObjectName("info_label")
        status_layout.addWidget(self.info_name_label)
        
        self.info_name = QLabel("---")
        self.info_name.setObjectName("info_label_value")
        status_layout.addWidget(self.info_name)
        
        status_layout.addStretch()
        
        # Info: Resolución
        self.info_res_label = QLabel("Resolución:")
        self.info_res_label.setObjectName("info_label")
        status_layout.addWidget(self.info_res_label)
        
        self.info_res = QLabel("---")
        self.info_res.setObjectName("info_label_value")
        status_layout.addWidget(self.info_res)
        
        status_layout.addSpacing(30)
        
        # Info: Tamaño
        self.info_size_label = QLabel("Tamaño:")
        self.info_size_label.setObjectName("info_label")
        status_layout.addWidget(self.info_size_label)
        
        self.info_size = QLabel("---")
        self.info_size.setObjectName("info_label_value")
        status_layout.addWidget(self.info_size)
        
        center_layout.addWidget(self.status_frame)
        
        self.splitter.addWidget(center_panel)
        
        main_layout.addWidget(self.splitter)

		# ============================================
        # BOTÓN TOGGLE PARA PANEL IZQUIERDO (SIMPLE)
        # ============================================
        self.btn_toggle_panel = QPushButton("◀", self.central_widget)
        self.btn_toggle_panel.setFixedSize(20, 60)
        self.btn_toggle_panel.setStyleSheet("""
            QPushButton {
                background-color: #0f3460;
                color: #00c3ff;
                border: 1px solid #00c3ff;
                border-left: none;
                border-radius: 0px 6px 6px 0px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #00c3ff;
                color: #0d0d15;
            }
        """)
        self.btn_toggle_panel.setToolTip("Ocultar/Mostrar panel")
        self.btn_toggle_panel.clicked.connect(self.toggle_thumbnail_panel)
        self.btn_toggle_panel.raise_()
        
        self.panel_visible = True
        self.panel_width = 150
        
        # Animación para el panel
        self.panel_animation = QtCore.QPropertyAnimation(self.thumbnail_panel, b"maximumWidth")
        self.panel_animation.setDuration(300)
        self.panel_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        
        self.panel_visible = True
        
        # ============================================
        # CONFIGURACIÓN INICIAL
        # ============================================
        self.splitter.setSizes([150, 850])
        
        # Drag & Drop
        self.setAcceptDrops(True)
        self.create_context_menu()
        self.create_shortcuts()
        self.info_app()
        
        # Posicionar botones de navegación
        QtCore.QTimer.singleShot(100, self.position_nav_buttons)
        
        # Posicionar botón toggle inicialmente  <-- AQUÍ VA, DENTRO DEL MÉTODO
        QtCore.QTimer.singleShot(100, self.update_toggle_button_position)

    def create_shortcuts(self):
        """Crear atajos de teclado"""

        # Atajo Ctrl + F ☑️ Ingresar Archivos Por Selección, en Boton Multiple
        QShortcut(QKeySequence('Ctrl+F'), self).activated.connect(self.selectet_directory_or_file)

        # Atajo Ctrl + I ☑️ Ingresar Archivos por Selección, Simple
        QShortcut(QKeySequence('Ctrl+I'), self).activated.connect(self.add_images)
        
        # Atajo Ctrl + C ☑️ Ingresar Archivos por Carpeta
        QShortcut(QKeySequence('Ctrl+C'), self).activated.connect(self.add_images_carpeta)
        
        # Atajo Ctrl + D ☑️ Ingresar Archivos por Directorio
        QShortcut(QKeySequence("Ctrl+D"), self).activated.connect(self.add_images_directorys)
        
        # Atajo Ctrl + B ☑️ Ingresar Archivos por Base de Datos
        QShortcut(QKeySequence("Ctrl+B"), self).activated.connect(self.prompt_load_database)
        
        # Atajo Ctrl + R ☑️ Ingresar Archivos por Explorar QRC
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(self.prompt_load_qrc)
        
        # Atajo Ctrl + J ☑️ Ingresar Archivos por Resources JSON
        QShortcut(QKeySequence("Ctrl+J"), self).activated.connect(self.prompt_load_json)
        
        # Atajo F1 ✔️ Información del Soft-Ware
        QShortcut(QKeySequence("F1"), self).activated.connect(self.info_app)
        
        # Atajo F11 ✔️ Expander | Contraer Pantalla
        QShortcut(QKeySequence("F11"), self).activated.connect(self.Pantalla_Completa)
        
        # Atajo Ctrl + K ✔️ Información Teclas de Atajos
        QShortcut(QKeySequence("Ctrl+K"), self).activated.connect(self.info_keys)
        
        # Atajo Ctrl + S ✔️ Guarda la Imagen
        QShortcut(QKeySequence("Ctrl+S"), self).activated.connect(self.Guardar_Imagen)
        
        # Atajo Ctrl + L ✔️ Limpia y Restaura
        QShortcut(QKeySequence("Ctrl+L"), self).activated.connect(self.cleanear)
        
        # Atajo Ctrl + E ✔️ Expande las Imagenes, dentro del Visor
        QShortcut(QKeySequence("Ctrl+E"), self).activated.connect(self.resize_label_image)

    # ============================================
    # MÉTODOS DE UI - NAVEGACIÓN Y CONTROLES
    # ============================================
    
    def position_nav_buttons(self):
        """Posicionar botones de navegación en los lados del visor"""
        container_rect = self.image_container.geometry()
        center_y = container_rect.height() // 2 - 25
        
        self.left_button.move(20, center_y)
        self.right_button.move(container_rect.width() - 70, center_y)

    def toggle_slideshow(self):
        """Alternar slideshow on/off"""
        if self.timer.isActive():
            self.timer.stop()
            self.paused = True
            self.btn_slideshow.setText("⏸ SLIDE SHOW: OFF")
            self.btn_slideshow.setProperty("active", "false")
        else:
            self.timer.start(self.Times_Stamp)
            self.paused = False
            self.btn_slideshow.setText("▶ SLIDE SHOW: ON")
            self.btn_slideshow.setProperty("active", "true")
        
        # Forzar actualización del estilo
        self.btn_slideshow.style().unpolish(self.btn_slideshow)
        self.btn_slideshow.style().polish(self.btn_slideshow)
        self.Actualizando_Title()

    def update_timer_interval(self, value):
        """Actualizar intervalo del timer"""
        self.Times_Stamp = value * 1000
        if self.timer.isActive():
            self.timer.stop()
            self.timer.start(self.Times_Stamp)

    def on_saturation_changed(self, value):
        """Manejar cambio de saturación"""
        self.sat_value.setText(f"{value}%")
        if self.original_pixmap is not None and not self.original_pixmap.isNull():
            self.apply_saturation(value)

    def apply_saturation(self, value):
        """Aplicar efecto de saturación usando OpenCV"""
        try:
            # Convertir QPixmap a numpy array (OpenCV)
            img = self.qpixmap_to_cv2(self.original_pixmap)
            
            if img is None:
                return
            
            # Convertir a HSV
            hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
            h, s, v = cv2.split(hsv)
            
            # Aplicar saturación (método del usuario)
            r = 255 - value
            s = s.astype(np.int16)
            s[s > r] = 255
            s[s <= r] += value
            s = s.astype(np.uint8)
            
            # Reconstruir imagen
            hsv_final = cv2.merge((h, s, v))
            img_result = cv2.cvtColor(hsv_final, cv2.COLOR_HSV2RGB)
            
            # Guardar temporal y mostrar
            self.image_final = img_result
            self.tmp = img_result.copy()
            
            # Convertir a QPixmap y mostrar
            self.current_pixmap = self.cv2_to_qpixmap(img_result)
            self.display_pixmap(self.current_pixmap)
            
        except Exception as e:
            print(f"Error aplicando saturación: {e}")
            # Si falla, mostrar original
            self.display_pixmap(self.original_pixmap)

    def set_image(self, img):
        """Método auxiliar para mostrar imagen desde array"""
        if img is not None:
            self.current_pixmap = self.cv2_to_qpixmap(img)
            self.display_pixmap(self.current_pixmap)

    def qpixmap_to_cv2(self, pixmap):
        """Convertir QPixmap a numpy array (OpenCV)"""
        qimage = pixmap.toImage()
        width = qimage.width()
        height = qimage.height()
        ptr = qimage.bits()
        ptr.setsize(qimage.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)
        return cv2.cvtColor(arr, cv2.COLOR_RGBA2RGB)

    def cv2_to_qpixmap(self, img):
        """Convertir numpy array (OpenCV) a QPixmap"""
        if len(img.shape) == 3:
            rgb_image = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
        else:
            rgb_image = cv2.cvtColor(img, cv2.COLOR_GRAY2RGBA)
        
        height, width, channels = rgb_image.shape
        bytes_per_line = channels * width
        qimage = QtGui.QImage(rgb_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGBA8888)
        return QPixmap.fromImage(qimage)

    def on_thumbnail_clicked(self, item):
        """Manejar click en miniatura"""
        index = self.thumbnail_list.row(item)
        if 0 <= index < len(self.images):
            self.current_index = index
            self.update_image()

    def update_thumbnails(self):
        """Actualizar panel de miniaturas con soporte JXL"""
        self.thumbnail_list.clear()
        
        for i, (img_type, name, data) in enumerate(self.images):
            item = QListWidgetItem()
            item.setText(name[:20] + "..." if len(name) > 20 else name)
            item.setToolTip(f"{name}\nTipo: {img_type.upper()}")
            
            # Generar icono con soporte JXL
            pixmap = None
            if img_type == 'file':
                if name.lower().endswith('.jxl'):
                    pixmap = self.load_from_jxl(data)
                else:
                    pixmap = QPixmap(data)
            elif img_type == 'blob':
                # ✅ Pasar el nombre para detectar JXL
                pixmap = self.load_from_blob(data, name)
            elif img_type == 'qrc':
                pixmap = self.load_from_qrc(data)
            elif img_type == 'json':
                pixmap = self.load_from_blob(data, name)
            
            if pixmap and not pixmap.isNull():
                scaled = pixmap.scaled(120, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                item.setIcon(QtGui.QIcon(scaled))
            
            self.thumbnail_list.addItem(item)
        
        self.img_counter.setText(f"{len(self.images)} imágenes")
        if self.images:
            self.thumbnail_list.setCurrentRow(self.current_index)

    def update_info_bar(self, img_type, name, pixmap):
        """Actualizar barra de información inferior"""
        # Origen
        origen_str = {
            'file': '📁 Archivo Local',
            'blob': '🗃️ Base de Datos',
            'qrc': '📦 Recurso QRC',
            'json': '📄 JSON'
        }.get(img_type, 'Desconocido')
        self.info_source.setText(origen_str)
        
        # Nombre
        self.info_name.setText(name[:40] + "..." if len(name) > 40 else name)
        
        # Resolución
        if pixmap and not pixmap.isNull():
            self.info_res.setText(f"{pixmap.width()} x {pixmap.height()} px")
            
            # Tamaño en memoria (aproximado)
            size_bytes = pixmap.width() * pixmap.height() * 4
            if size_bytes < 1024:
                size_str = f"{size_bytes} B"
            elif size_bytes < 1024 * 1024:
                size_str = f"{size_bytes / 1024:.2f} KB"
            else:
                size_str = f"{size_bytes / (1024 * 1024):.2f} MB"
            self.info_size.setText(size_str)
        else:
            self.info_res.setText("---")
            self.info_size.setText("---")

    def display_pixmap(self, pixmap):
        """Mostrar pixmap en el label central"""
        if pixmap and not pixmap.isNull():
            scaled = pixmap.scaled(
                self.label.width() - 20,
                self.label.height() - 20,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.label.setPixmap(scaled)

    # ============================================
    # MÉTODOS ORIGINALES (MODIFICADOS)
    # ============================================
    
    def selectet_directory_or_file(self):
        """Diálogo para seleccionar archivos de diferentes maneras"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('--> Selectet File´s <--')
        
        # Icono personalizado
        try:
            self.Aicon_App = Path.resource_path('Ico\\1.ico')
            msg_box.setWindowIcon(QIcon(self.Aicon_App))
        except:
            pass
        
        msg_box.setText('¿Cómo deseas agregar las imágenes?')
        
        btn_simple = msg_box.addButton('   Selección Simple   ', QMessageBox.YesRole)
        btn_carpeta = msg_box.addButton('   Por Carpeta   ', QMessageBox.YesRole)
        btn_directorio = msg_box.addButton('   Por Directorio   ', QMessageBox.YesRole)
        btn_cancelar = msg_box.addButton('  Cancelar  ', QMessageBox.NoRole)
        
        msg_box.exec_()
        
        if msg_box.clickedButton() == btn_simple:
            self.add_images()
        elif msg_box.clickedButton() == btn_carpeta:
            self.add_images_carpeta()
        elif msg_box.clickedButton() == btn_directorio:
            self.add_images_directorys()

    def Pantalla_Completa(self):
        """Alternar modo pantalla completa"""
        if not self.Full_Screnn_Window:
            self.Full_Screnn_Window = True
            self.showFullScreen()
            self.btn_fullscreen.setText("⛶")
            self.btn_fullscreen.setToolTip("Salir de pantalla completa (Esc)")
        else:
            self.Full_Screnn_Window = False
            self.Esconder = False
            self.showNormal()
            self.btn_fullscreen.setText("⛶")
            self.btn_fullscreen.setToolTip("Pantalla completa")
        
        # Reposicionar botones después de cambiar modo
        QtCore.QTimer.singleShot(100, self.position_nav_buttons)
    
    def load_from_blob(self, blob_data, name=""):
        """Carga imagen desde bytes, detectando JXL automáticamente"""
        try:
            # Detectar si es JXL por el nombre o magic bytes
            if name.lower().endswith('.jxl') or (blob_data[:2] == b'\xff\x0a'):
                return self._load_jxl_from_bytes(blob_data)

            pixmap = QPixmap()
            if pixmap.loadFromData(blob_data):
                return pixmap
        except Exception as e:
            print(f"Error BLOB: {e}")
        return None

    def _load_jxl_from_bytes(self, blob_data):
        """Carga JXL desde bytes (para BLOBs) - CORREGIDO"""
        try:
            decoder = Decoder(parallel=True)
            info, pixels = decoder(blob_data)
            
            if info.mode not in ("RGB", "RGBA", "L", "LA"):
                raise ValueError(f"Modo JXL no soportado: {info.mode}")
            
            imagen = Image.frombytes(info.mode, (info.width, info.height), pixels)
            
            buffer = BytesIO()
            imagen.save(buffer, format="PNG")
            datos_png = buffer.getvalue()
            
            pixmap = QPixmap()
            if pixmap.loadFromData(datos_png, "PNG"):
                return pixmap
        except Exception as e:
            print(f"Error JXL bytes: {e}")
        return None

    def _is_valid_image_blob(self, blob_data, filename=""):
        """Verifica si un BLOB es imagen válida (incluye JXL)"""
        try:
            # Detectar JXL por extensión o magic bytes
            if filename.lower().endswith('.jxl') or blob_data[:2] == b'\xff\x0a':
                try:
                    decoder = Decoder()
                    info, _ = decoder(blob_data)
                    return True
                except:
                    return False
            
            # Para otros formatos
            test_pixmap = QPixmap()
            if test_pixmap.loadFromData(blob_data):
                return True
        except:
            pass
        return False

    def load_from_qrc(self, resource_path):
        try:
            file = QFile(resource_path)
            if file.open(QIODevice.ReadOnly):
                data = file.readAll()
                file.close()
                pixmap = QPixmap()
                if pixmap.loadFromData(data):
                    return pixmap
        except Exception as e:
            print(f"Error QRC: {e}")
        return None

    def load_from_jxl(self, ruta):
        """Cargar imagen JXL desde archivo (wrapper)"""
        try:
            with open(ruta, "rb") as archivo:
                datos_jxl = archivo.read()
            return self._load_jxl_from_bytes(datos_jxl)
        except Exception as e:
            print(f"Error cargando JXL archivo: {e}")
        return None

    def update_image(self):
        if not self.images or self.current_index >= len(self.images):
            self.label.setText("Arrastra imágenes o usa los botones de carga")
            self.label.setStyleSheet("color: #666; font-size: 16px;")
            return
        
        img_type, name, data = self.images[self.current_index]
        self.Actualizando_Title()
        
        # Cargar según tipo
        if img_type == 'file':
            if name.lower().endswith('.jxl'):
                pixmap = self.load_from_jxl(data)
            else:
                pixmap = QPixmap(data)
        elif img_type == 'blob':
            # ✅ AQUÍ ESTÁ EL ERROR - Debe pasar 'name' para detectar JXL
            pixmap = self.load_from_blob(data, name)  # ← Pase 'name' aquí
        elif img_type == 'qrc':
            pixmap = self.load_from_qrc(data)
        elif img_type == 'json':
            pixmap = self.load_from_blob(data, name)  # ← Y aquí también
        else:
            pixmap = None
        
        if pixmap and not pixmap.isNull():
            self.original_pixmap = pixmap.copy()
            self.current_pixmap = pixmap
            
            # Aplicar saturación actual
            sat_value = self.Slide_Saturacion.value()
            if sat_value != 100:
                self.apply_saturation(sat_value)
            else:
                self.display_pixmap(pixmap)
            
            # Actualizar UI
            self.update_info_bar(img_type, name, pixmap)
            self.thumbnail_list.setCurrentRow(self.current_index)
        else:
            self.label.setText(f"❌ Error cargando: {name}")

    def next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.update_image()

    def previous_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.update_image()

    def add_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Seleccionar Imágenes", "", 
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif *.ico *.webp *.jxl)"
        )
        for f in files:
            self.images.append(('file', os.path.basename(f), f))
        self.update_thumbnails()
        self.update_image()

    def add_images_carpeta(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder:
            exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')
            for f in os.listdir(folder):
                if f.lower().endswith(exts):
                    full = os.path.join(folder, f)
                    self.images.append(('file', f, full))
            self.update_thumbnails()
            self.update_image()

    def add_images_directorys(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Directorio")
        if folder:
            exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')
            for dirpath, _, files in os.walk(folder):
                for f in files:
                    if f.lower().endswith(exts):
                        full = os.path.join(dirpath, f)
                        self.images.append(('file', f, full))
            self.update_thumbnails()
            self.update_image()

    def In_Im_Extern_Path(self):
        if not self.in_im:
            return
        folder = os.path.dirname(self.in_im) if os.path.isfile(self.in_im) else self.in_im
        exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if f.lower().endswith(exts):
                    full = os.path.join(folder, f)
                    self.images.append(('file', f, full))
        self.update_thumbnails()
        self.update_image()

    def Actualizando_Title(self):
        if not self.images:
            self.setWindowTitle("Slide_Image (E.X._v7)")
        else:
            status = "▶" if self.timer.isActive() else "⏸"
            self.setWindowTitle(f"Slide_Image (E.X._v7) || {status}")

    # ============================================
    # MÉTODOS RESTANTES (Sin cambios funcionales)
    # ============================================
    
    def create_context_menu(self):
        self.context_menu = QMenu(self)
        
        try:
            self.Ico_Menu = Path.resource_path('Ico\\jpeg.png')
            self.context_menu.addAction(QIcon(self.Ico_Menu), "📎 Archivos (Ctrl+I)", self.add_images)
            self.context_menu.addAction(QIcon(self.Ico_Menu), "📂 Carpeta (Ctrl+C)", self.add_images_carpeta)
            self.context_menu.addAction(QIcon(self.Ico_Menu), "📁 Directorio (Ctrl+D)", self.add_images_directorys)
        except:
            self.context_menu.addAction("📎 Archivos (Ctrl+I)", self.add_images)
            self.context_menu.addAction("📂 Carpeta (Ctrl+C)", self.add_images_carpeta)
            self.context_menu.addAction("📁 Directorio (Ctrl+D)", self.add_images_directorys)
        
        self.context_menu.addSeparator()
        
        try:
            self.context_menu.addAction(QIcon(self.Ico_Menu), "☁️ Base de Datos (Ctrl+B)", self.prompt_load_database)
            self.context_menu.addAction(QIcon(self.Ico_Menu), "☢️ Explorar QRC (Ctrl+R)", self.prompt_load_qrc)
            self.context_menu.addAction(QIcon(self.Ico_Menu), "☣️ Resources JSON (Ctrl+J)", self.prompt_load_json)
        except:
            self.context_menu.addAction("☁️ Base de Datos (Ctrl+B)", self.prompt_load_database)
            self.context_menu.addAction("☢️ Explorar QRC (Ctrl+R)", self.prompt_load_qrc)
            self.context_menu.addAction("☣️ Resources JSON (Ctrl+J)", self.prompt_load_json)
        
        self.context_menu.addSeparator()
        
        try:
            self.Ico_Menu2 = Path.resource_path('Ico\\2.png')
            self.context_menu.addAction(QIcon(self.Ico_Menu2), "📍 Información (F1)", self.info_app)
            self.context_menu.addAction(QIcon(self.Ico_Menu2), "📍 Atajos (Ctrl+K)", self.info_keys)
            self.context_menu.addSeparator()
            self.context_menu.addAction(QIcon(self.Ico_Menu2), "📥 Guardar Imagen (Ctrl+S)", self.Guardar_Imagen)
            self.context_menu.addAction(QIcon(self.Ico_Menu2), "💨 Limpiar (Ctrl+L)", self.cleanear)
        except:
            self.context_menu.addAction("📍 Información (F1)", self.info_app)
            self.context_menu.addAction("📍 Atajos (Ctrl+K)", self.info_keys)
            self.context_menu.addSeparator()
            self.context_menu.addAction("📥 Guardar Imagen (Ctrl+S)", self.Guardar_Imagen)
            self.context_menu.addAction("💨 Limpiar (Ctrl+L)", self.cleanear)
        
        self.context_menu.addSeparator()
        self.context_menu.addAction('O Solo Arrastra y Suelta...')
        self.context_menu.addSeparator()
        
        try:
            self.Ico_Salir = Path.resource_path('Ico\\Salir.png')
            self.context_menu.addAction(QIcon(self.Ico_Salir), "❌ Cerrar (ESC)", self.close)
        except:
            self.context_menu.addAction("❌ Cerrar (ESC)", self.close)
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(
            lambda pos: self.context_menu.exec_(self.mapToGlobal(pos))
        )

    def info_app(self):
        msn = '''

✨ Slide Image Viewer v7 ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ Este soft es un visor universal de imágenes multi-formato:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Ingreso por Menú Contextual [Abrir con...]
✓ Drag & Drop (Arrastrar y Soltar) con soporte JXL
✓ Selección Simple de archivos con soporte JXL
✓ Por Carpeta (sin subdirectorios) con soporte JXL
✓ Por Directorio (con subdirectorios) con soporte JXL
✓ Desde Base de Datos SQLite BLOB con soporte JXL
✓ Desde Recursos QRC de PyQt
✓ Desde archivos JSON (Base64/URLs) con soporte JXL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ Atajos:
F1 = Info
Ctrl+K = Muestra los Atajos en Teclado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 Desarrollado por: Cristian M. Veliz Cano
📧 cristianvel2015mvc@gmail.com
        '''
        QMessageBox.information(self, "✓ INFO App", msn)

    def info_keys(self):
        msn = ''' 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 TECLAS DE ATAJO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ctrl+F → Selección, en Boton Multiple
Ctrl+I → Selección Simple
Ctrl+C → Por Carpeta
Ctrl+D → Por Directorio
Ctrl+B → Base de Datos
Ctrl+R → Explorar QRC
Ctrl+J → Resources JSON
F1 → Información
F11 → Expander | Contraer Pantalla
Ctrl+K → Esta ventana
Ctrl+S → Guardar imagen
Ctrl+L → Limpiar todo
Ctrl+E → Expande las Imagenes, en Visor
← → → Navegar imágenes
Rueda Mouse → Navegar
Click/Espacio → Pausar/Play
Esc → Cerrar app / Salir pantalla completa
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        '''
        QMessageBox.information(self, "✓ TECLAS DE ATAJO", msn)

    def prompt_load_database(self):
        db_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Base de Datos SQLite", "",
            "SQLite (*.db *.sqlite *.sqlite3);;Todos los archivos (*)"
        )
        if not db_path:
            return
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [t[0] for t in cursor.fetchall()]
            
            if not tables:
                QMessageBox.warning(self, "BD Vacía", "La base de datos no contiene tablas.")
                return
            
            tabla = None
            columnas = []
            candidatas = [t for t in tables if t.lower() in ['images', 'imagenes', 'fotos', 'pictures', 'gallery', 'photos']]
            tablas_revisar = candidatas if candidatas else tables
            
            for t in tablas_revisar:
                try:
                    cursor.execute(f"PRAGMA table_info({t})")
                    cols = cursor.fetchall()
                    tiene_blob = any('blob' in c[2].lower() or c[2].upper() == 'BLOB' for c in cols)
                    if tiene_blob:
                        tabla = t
                        columnas = cols
                        break
                except:
                    continue
            
            if not tabla:
                QMessageBox.warning(self, "Sin imágenes", "No se encontró tabla con datos BLOB.")
                conn.close()
                return
            
            col_nombre = None
            col_blob = None
            
            for col in columnas:
                col_name = col[1]
                col_type = col[2].upper()
                if any(k in col_name.lower() for k in ['name', 'nombre', 'filename', 'file', 'titulo', 'title']):
                    col_nombre = col_name
                elif 'BLOB' in col_type:
                    col_blob = col_name
            
            if not col_blob:
                for col in columnas:
                    if 'BLOB' in col[2].upper() or 'DATA' in col[1].upper():
                        col_blob = col[1]
                        break
            
            if not col_blob:
                QMessageBox.warning(self, "Error", "No se encontró columna BLOB.")
                conn.close()
                return
            
            if not col_nombre:
                col_nombre = col_blob
            
            cursor.execute(f"SELECT {col_nombre}, {col_blob} FROM {tabla}")
            registros = cursor.fetchall()
            conn.close()
            
            if not registros:
                QMessageBox.warning(self, "Sin Datos", "La tabla no contiene registros.")
                return
            
            self.images.clear()
            self.current_index = 0
            
            for nombre, blob_data in registros:
                if blob_data and isinstance(blob_data, (bytes, memoryview)):
                    display_name = str(nombre) if nombre else f"imagen_{len(self.images)+1}.jxl"
                    
                    # ✅ Usar validación que soporta JXL
                    if self._is_valid_image_blob(blob_data, display_name):
                        self.images.append(('blob', display_name, blob_data))
            
            if self.images:
                self.update_thumbnails()
                self.update_image()
                QMessageBox.information(self, "BD Cargada", 
                    f"🗃️ {len(self.images)} imágenes cargadas de '{tabla}'")
            else:
                QMessageBox.warning(self, "Sin Imágenes", "No se encontraron imágenes válidas.")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error:\n{str(e)}")

    def prompt_load_qrc(self):
        rc_file, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar resources_rc.py", "", "Python Module (*.py)"
        )
        if not rc_file:
            return
        
        base = os.path.splitext(rc_file)[0]
        qrc_file = base + ".qrc"
        
        if not os.path.exists(qrc_file):
            qrc_file, _ = QFileDialog.getOpenFileName(
                self, "Seleccionar archivo QRC", os.path.dirname(rc_file), "QRC Files (*.qrc)"
            )
        
        if not qrc_file or not os.path.exists(qrc_file):
            QMessageBox.warning(self, "Se necesita QRC", "Necesito el archivo .qrc")
            return
        
        try:
            tree = ET.parse(qrc_file)
            root = tree.getroot()
            resource_paths = []
            
            for qresource in root.findall('qresource'):
                prefix = qresource.get('prefix', '')
                if prefix and not prefix.startswith('/'):
                    prefix = '/' + prefix
                for file_elem in qresource.findall('file'):
                    file_path = file_elem.text
                    if file_path:
                        qt_path = f":{prefix}/{file_path}" if prefix else f":/{file_path}"
                        resource_paths.append(qt_path)
        except Exception as e:
            QMessageBox.critical(self, "Error QRC", f"No se pudo leer:\n{str(e)}")
            return
        
        if not resource_paths:
            QMessageBox.warning(self, "Vacío", "El QRC no contiene archivos.")
            return
        
        try:
            import importlib.util
            module_name = f"qrc_viewer_{os.path.basename(base)}"
            spec = importlib.util.spec_from_file_location(module_name, rc_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar:\n{str(e)}")
            return
        
        self.images.clear()
        self.current_index = 0
        image_exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.svg', '.tiff', '.jxl')
        
        for qt_path in resource_paths:
            ext = os.path.splitext(qt_path)[1].lower()
            if ext in image_exts:
                display_name = os.path.basename(qt_path)
                self.images.append(('qrc', display_name, qt_path))
        
        if self.images:
            self.update_thumbnails()
            self.update_image()
            QMessageBox.information(self, "QRC Cargado", f"📦 {len(self.images)} imágenes cargadas")
        else:
            QMessageBox.warning(self, "Sin imágenes", "No se encontraron imágenes.")

    def prompt_load_json(self):
        """Carga imágenes desde JSON: Base64, URLs locales, o Data URIs (CON VERIFICACIÓN JXL)"""
        
        json_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar JSON", "", "JSON (*.json)"
        )
        if not json_path:
            return
        
        base_dir = os.path.dirname(json_path)
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.images.clear()
            self.current_index = 0
            
            # Buscar imágenes recursivamente en cualquier estructura
            def buscar_imagenes(obj):
                """Busca imágenes en cualquier parte del JSON"""
                if isinstance(obj, dict):
                    # Caso 1: Base64 directo (formato Image JSON Manager)
                    if 'data' in obj and isinstance(obj['data'], str):
                        nombre = obj.get('nombre') or obj.get('name') or f"img_{len(self.images)+1}.png"
                        try:
                            b64 = obj['data']
                            # Limpiar Data URI si existe (data:image/png;base64,...)
                            if ',' in b64:
                                b64 = b64.split(',')[1]
                            
                            blob = base64.b64decode(b64)
                            
                            # ✅ VERIFICACIÓN CORREGIDA: Usa _is_valid_image_blob (soporta JXL)
                            if self._is_valid_image_blob(blob, nombre):
                                # Detectar si es JXL por magic bytes y corregir extensión
                                if blob[:2] == b'\xff\x0a' and not nombre.lower().endswith('.jxl'):
                                    nombre += '.jxl'
                                self.images.append(('json', nombre, blob))
                                
                        except Exception as e:
                            print(f"Error decodificando base64: {e}")
                    
                    # Caso 2: URL o Path local
                    for key in ['url', 'path', 'src', 'file', 'ruta']:
                        if key in obj and isinstance(obj[key], str):
                            img_path = obj[key]
                            
                            # Si es URL absoluta, descargar
                            if img_path.startswith(('http://', 'https://')):
                                try:
                                    img_data = urllib.request.urlopen(img_path, timeout=5).read()
                                    nombre = os.path.basename(img_path) or f"web_{len(self.images)}.jpg"
                                    
                                    # ✅ VERIFICAR con _is_valid_image_blob (soporta JXL)
                                    if self._is_valid_image_blob(img_data, nombre):
                                        self.images.append(('json', nombre, img_data))
                                except Exception as e:
                                    print(f"Error descargando URL: {e}")
                            
                            # Si es ruta relativa/absoluta local
                            else:
                                if not os.path.isabs(img_path):
                                    img_path = os.path.join(base_dir, img_path)
                                
                                if os.path.exists(img_path):
                                    nombre = os.path.basename(img_path)
                                    
                                    # ✅ Detectar JXL por extensión y verificar
                                    if img_path.lower().endswith('.jxl'):
                                        try:
                                            with open(img_path, 'rb') as f:
                                                jxl_data = f.read()
                                            if self._is_valid_image_blob(jxl_data, img_path):
                                                self.images.append(('jxl', nombre, img_path))
                                        except Exception as e:
                                            print(f"Error leyendo JXL local: {e}")
                                    else:
                                        # Verificar otros formatos con _is_valid_image_blob
                                        try:
                                            with open(img_path, 'rb') as f:
                                                file_data = f.read()
                                            if self._is_valid_image_blob(file_data, nombre):
                                                self.images.append(('file', nombre, img_path))
                                        except:
                                            pass
                    
                    # Recursión en sub-objetos
                    for v in obj.values():
                        buscar_imagenes(v)
                        
                elif isinstance(obj, list):
                    for item in obj:
                        buscar_imagenes(item)
            
            # Iniciar búsqueda
            buscar_imagenes(data)
            
            if self.images:
                self.update_thumbnails()
                self.update_image()
                
                # ✅ Contar tipos para mensaje detallado (como en BD)
                tipos = {}
                for tipo, _, _ in self.images:
                    tipos[tipo] = tipos.get(tipo, 0) + 1
                
                msg = f"📄 {len(self.images)} imágenes encontradas\n\n"
                msg += "Desglose:\n"
                for tipo, cantidad in sorted(tipos.items()):
                    emoji = {
                        'json': '📄 JSON Base64', 
                        'file': '📁 Archivo Local', 
                        'jxl': '🖼️ JXL Local', 
                        'blob': '💾 BLOB'
                    }.get(tipo, f'📎 {tipo.upper()}')
                    msg += f"  {emoji}: {cantidad}\n"
                
                QMessageBox.information(self, "JSON Cargado", msg)
            else:
                QMessageBox.warning(self, "Sin imágenes", 
                    "No se encontraron imágenes válidas.\n\n"
                    "Formatos soportados:\n"
                    "• Base64 PNG/JPG: {\"data\": \"iVBORw0KGgo...\", \"nombre\": \"img.png\"}\n"
                    "• Base64 JXL: {\"data\": \"/woAASsKGgo...\", \"nombre\": \"img.jxl\"}\n"
                    "• Archivo local: {\"path\": \"carpeta/imagen.png\"}\n"
                    "• Archivo JXL: {\"path\": \"carpeta/imagen.jxl\"}\n"
                    "• URL web: {\"url\": \"https://ejemplo.com/img.jpg\"}")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar JSON:\n{str(e)}")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            if url.isLocalFile():
                path = url.toLocalFile()
                if path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')):
                    self.images.append(('file', os.path.basename(path), path))
        self.update_thumbnails()
        self.update_image()

    def mousePressEvent(self, event=None):
        if event is None:
            return
        if self.timer.isActive():
            self.timer.stop()
            self.paused = True
            self.btn_slideshow.setText("⏸ SLIDE SHOW: OFF")
            self.btn_slideshow.setProperty("active", "false")
        else:
            self.timer.start(self.Times_Stamp)
            self.paused = False
            self.btn_slideshow.setText("▶ SLIDE SHOW: ON")
            self.btn_slideshow.setProperty("active", "true")
        
        self.btn_slideshow.style().unpolish(self.btn_slideshow)
        self.btn_slideshow.style().polish(self.btn_slideshow)
        self.Actualizando_Title()
        self.update_image()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.position_nav_buttons()
        if self.images:
            self.update_image()

    def center_on_screen(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(
        	(screen.width() - 1200) // 2, 
        	(screen.height() - 750) // 2, 
        	1200, 750)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            if self.Full_Screnn_Window:
                self.Pantalla_Completa()
            else:
                self.close()
        elif event.key() == Qt.Key_Left:
            self.previous_image()
        elif event.key() == Qt.Key_Right:
            self.next_image()
        elif event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
            if self.current_pixmap:
                QtWidgets.QApplication.clipboard().setPixmap(self.current_pixmap)
                QMessageBox.information(self, "Copiado", "📋 Imagen copiada al portapapeles")
        elif event.key() == Qt.Key_Space:
            self.toggle_slideshow()

    def Guardar_Imagen(self):
        if not self.images or self.current_index >= len(self.images):
            QMessageBox.warning(self, "Sin imagen", "No hay imagen para guardar")
            return
        
        nombre_path, _ = QFileDialog.getSaveFileName(self, "Guardar como", "",
            "PNG(*.png);;JPG(*.jpg);;BMP(*.bmp);;Todos los archivos(*.*)")
        
        if nombre_path and self.current_pixmap:
            self.current_pixmap.save(nombre_path)
            QMessageBox.information(self, "Guardado", "✅ Imagen guardada con éxito.")

    def cleanear(self):
        self.in_im = ""
        self.images = []
        self.current_index = 0
        self.current_pixmap = None
        self.original_pixmap = None
        self.paused = False
        
        self.thumbnail_list.clear()
        self.img_counter.setText("0 imágenes")
        self.label.clear()
        self.label.setText("Arrastra imágenes o usa los botones de carga")
        
        self.info_source.setText("Ninguno")
        self.info_name.setText("---")
        self.info_res.setText("---")
        self.info_size.setText("---")
        
        self.setWindowTitle('Slide_Image (E.X._v7)')

    def toggle_thumbnail_panel(self):
        """Ocultar o mostrar el panel de miniaturas (instantáneo)"""
        total_width = self.central_widget.width()
        
        if self.panel_visible:
            # OCULTAR - guardar ancho actual
            self.panel_width = self.thumbnail_panel.width()
            # Colapsar a 0
            self.splitter.setSizes([0, total_width])
            self.btn_toggle_panel.setText("▶")
            self.panel_visible = False
            
        else:
            # MOSTRAR - restaurar ancho
            self.splitter.setSizes([self.panel_width, total_width - self.panel_width])
            self.btn_toggle_panel.setText("◀")
            self.panel_visible = True
        
        # Actualizar posiciones
        self.update_toggle_button_position()
        self.position_nav_buttons()
    
    def update_toggle_button_position(self):
        """Actualizar posición del botón toggle - lo pone al borde del panel"""
        # Usar QTimer para esperar que el splitter termine de redibujar
        QtCore.QTimer.singleShot(50, self._do_update_button_position)
    
    def _do_update_button_position(self):
        """Posicionar real del botón"""
        if self.panel_visible:
            # Panel visible - botón al borde derecho del panel
            x = self.thumbnail_panel.width()
        else:
            # Panel oculto - botón al borde izquierdo (x=0)
            x = 0
        
        y = self.central_widget.height() // 2 - 30
        self.btn_toggle_panel.move(x, y)
    
    def position_nav_buttons(self):
        """Posicionar botones de navegación"""
        container_rect = self.image_container.geometry()
        center_y = container_rect.height() // 2 - 25
        
        self.left_button.move(20, center_y)
        self.right_button.move(container_rect.width() - 113, center_y)
    
    def resizeEvent(self, event):
        """Sobrescribir resize para actualizar posición del botón"""
        super().resizeEvent(event)
        self.position_nav_buttons()
        self.update_toggle_button_position()

    def resize_label_image(self):

    	if self.resize_labl:

    		self.label.setScaledContents(self.resize_labl)
    		self.resize_labl = False

    	else:

    		self.label.setScaledContents(self.resize_labl)
    		self.resize_labl = True

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    
    in_im = sys.argv[1] if len(sys.argv) > 1 else None
    ex = ImageSlider(in_im)
    ex.show()
    sys.exit(app.exec_())