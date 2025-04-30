@echo off
:loop
set /p query=Search: 
if not "%query%"=="" python "Paste Here Gemini.py path" %query%
goto loop
