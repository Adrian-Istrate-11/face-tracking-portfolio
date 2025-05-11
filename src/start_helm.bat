@echo off
REM ────────────────────────────────────────────────────────────────
REM 1. Setează variabile de cale
SET REPO_DIR=%~dp0
SET CHART_DIR=%REPO_DIR%helm\face-tracking

REM ────────────────────────────────────────────────────────────────
REM 2. Instalează sau actualizează release-ul Helm
echo.
echo == Helm upgrade/install ==
cd /d "%CHART_DIR%"
helm upgrade --install ft-app .

REM ────────────────────────────────────────────────────────────────
REM 3. Pornește port-forward în ferestre separate
echo.
echo == Port-forward API (8080) ==
start cmd /k "kubectl port-forward svc/ft-app-api 8080:8080"

echo.
echo == Port-forward Web  (8050) ==
start cmd /k "kubectl port-forward svc/ft-app-web 8050:8050"

echo.
echo Chart-ul Helm a fost instalat/actualizat și port-forward rulează.
echo Accesează:
echo   - Dash UI : http://localhost:8050
echo   - Swagger : http://localhost:8080/docs
pause
