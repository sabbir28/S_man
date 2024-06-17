from cx_Freeze import setup, Executable

# List of packages to include
packages = ["os", "sys", "argparse", "requests", "json", "colorama", "importlib", "subprocess"]

# Exclude tkinter which is not needed for a command-line tool
excludes = ["tkinter"]

# Build options
build_exe_options = {
    "packages": packages,
    "excludes": excludes,
    "include_files": [],  # You can add additional files or directories here if needed
    "optimize": None  # Disable optimization if you have issues with the build
}

# Executable options
exe_options = {
    "script": "sman.py",  # The main Python script to convert to executable
    "base": None  # None means auto-detect the appropriate base (Console on Windows, POSIX on Linux/macOS)
}

setup(
    name="sman",
    version="0.1",
    description="A command-line tool for making HTTP requests.",
    long_description="""
        sman is a command-line tool that allows users to perform HTTP requests 
        with various options for methods, headers, data, and more. 
        It supports GET and POST requests and provides an option to save 
        the response to a file.
    """,
    author="SABBIR28",
    author_email="sabbirb228@gmail.com",
    url="http://sabbir28.github.io/",
    options={
        "build_exe": build_exe_options
    },
    executables=[
        Executable(**exe_options)
    ]
)
