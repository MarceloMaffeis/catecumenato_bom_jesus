@echo off
title Catecumenato de Adultos - Bom Jesus dos Aflitos
echo ===================================================================
echo   PAROQUIA BOM JESUS DOS AFLITOS - SOROCABA/SP (FRANCISCANOS)
echo   Iniciando o Portal do Catecumenato de Adultos...
echo   Paz e Bem!
echo ===================================================================
cd /d "%~dp0"
streamlit run app.py
pause