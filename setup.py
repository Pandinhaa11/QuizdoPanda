from cx_Freeze import setup, Executable

setup(
name="Seu Quiz",
version="1.0",
description="Um quiz criado por mim!",
executables=[Executable("main.py")]
)