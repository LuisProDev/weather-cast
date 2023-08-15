import os
import sys
from cx_Freeze import Executable, setup

files = ["./img.py", "images.qrc", "janela_secundaria.py", "icons8-cloud-64.ico"]

target = Executable(script="janela_principal.py", base="Win32GUI", icon="icons8-cloud-64.ico")

setup(name="Previsão do Tempo",
      version="1.0",
      description="Programa com interface simples de previsão do tempo",
      author="LuisProDev",
      options={'build_exe': {"include_files" : files}},
      executables=[target])

