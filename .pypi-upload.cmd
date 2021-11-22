@echo off
call .env.cmd
del /F /Q dist\*
py ./setup.py sdist
py -m build -w
py -m twine upload -u __token__ dist\*
rmdir /S /Q build
