@echo off
setlocal

:: Buscar el ID del contenedor basado en la imagen
for /f "tokens=*" %%i in ('docker ps -a -q --filter "ancestor=operaciones-app"') do set containerId=%%i

if defined containerId (
    echo Contenedor encontrado con ID: %containerId%

    :: Detener el contenedor
    docker stop %containerId%

    :: Eliminar el contenedor
    docker rm %containerId%
) else (
    echo No se encontró ningún contenedor para la imagen 'operaciones-app'.
)

endlocal
