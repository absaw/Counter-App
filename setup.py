from setuptools import setup
import os
import shutil

# Paths to libffi and the source of your app
LIBFFI_PATH = '/opt/homebrew/Cellar/libffi/3.4.6/lib'
APP_PATH = 'counter_app.py'
APP_NAME = 'counter_app'

# Remove old libffi.dylib if it exists
if os.path.exists(f'dist/{APP_NAME}.app/Contents/Frameworks/libffi.8.dylib'):
    os.remove(f'dist/{APP_NAME}.app/Contents/Frameworks/libffi.8.dylib')

# Setup.py configuration
APP = [APP_PATH]
DATA_FILES = [
    ('Frameworks', [os.path.join(LIBFFI_PATH, 'libffi.dylib')])
]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['rumps'],
    'plist': {
        'LSUIElement': True,  # This makes the app run in the background without showing up in the dock
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)


# from setuptools import setup

# APP = ['counter_app.py']
# DATA_FILES = []
# OPTIONS = {
#     'argv_emulation': True,
#     'packages': ['rumps'],
#     'plist': {
#         'LSUIElement': True,  # This makes the app run in the background without showing up in the dock
#     }
# }

# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
# )
