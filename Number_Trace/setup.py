from cx_Freeze import setup, Executable
setup(name = "Password_Gen",
        version = "1.0",
        description = "This is a password generator",
        executables = [Executable("Number_Trace.py")]
        )
