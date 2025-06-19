# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('estilos/style.qss', 'estilos'),
        (r'C:\Users\usuario\Desktop\Ciencia de Datos\Excursiones\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms\qwindows.dll', 'platforms'),
    ],
    hiddenimports=collect_submodules('widgets'),
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Excursiones',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,
    single_file=True  # 🔥 Esto activa el modo ONEFILE de verdad
)
