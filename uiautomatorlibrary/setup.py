from distutils.core import setup

setup(
    name = 'robotframework-uiautomatorlibrary',
    packages = ['uiautomatorlibrary'],
    version = '0.1',
    author='ming060',
    author_email = 'lym060@gmail.com',
    url = 'https://github.com/ming060/robotframework-uiautomatorlibrary',
    description = 'Robot Framework Android Test Library',
    long_description = '',
    install_requires = ['uiautomator >= 0.1.28'],
    classifiers  = [
                    'Programming Language :: Python :: 2.7',
#                     'License :: ', #TODO
                    'Operating System :: Microsoft :: Windows :: Windows 7',
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Testing'
                    ]
)