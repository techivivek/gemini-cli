@echo off
:loop
set /p query=Search: 
if not "%query%"=="" python "D:\Programming\Python\gemini.py" %query%
goto loop
