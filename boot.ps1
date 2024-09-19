param (
    [string]$VAR_CONTEXT = "development"
)

# Activar el entorno virtual
& "venv/Scripts/Activate"
Write-Output "Environment activated"

# Controlar el contexto del entorno
if ($VAR_CONTEXT -eq "production") {
    $VAR_CONTEXT = "production"
} elseif ($VAR_CONTEXT -eq "testing") {
    $VAR_CONTEXT = "testing"
} else {
    $VAR_CONTEXT = "development"
}

Write-Output "Environment set to: $VAR_CONTEXT"
$env:FLASK_CONTEXT = $VAR_CONTEXT

# Iniciar la aplicación Flask
python app.py
