@echo off
title Noxius Token Checker ^| Developed by rotomicora#0001
echo [INFO] INSTALLING MODULES [INFO]
timeout 1 >nul
pip install -r requirements.txt
echo [OK] MODULES INSTALLED, STARTING NOXIUS TOKEN CHECKER
timeout 1 >nul
python main.py