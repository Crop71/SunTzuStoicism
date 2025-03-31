@echo off
if "%1"=="install" pip install -r requirements.txt
if "%1"=="run" python generate_video.py
if "%1"=="clean" rmdir /s /q __pycache__
