from setuptools import setup

APP = ['counter_app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
