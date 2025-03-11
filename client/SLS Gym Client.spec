# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Student_Main.py'],
    pathex=[],
    binaries=[],
    datas=[('Student_Libs.py', 'Student_Libs'), ('.env', '.')],
    hiddenimports=['mysql.connector', 'mysql.connector.plugins.mysql_native_password', 'cryptography'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SLS Gym Client',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['GMC.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SLS Gym Client',
)
app = BUNDLE(
    coll,
    name='SLS Gym Client.app',
    icon='GMC.icns',
    bundle_identifier=None,
)
