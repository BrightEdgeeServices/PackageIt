rd /S /Q d:\dropbox\projects\%1
rd /S /Q C:\ProgramData\PackageIt\%1
CALL venvremove %1
CALL venv packageit
