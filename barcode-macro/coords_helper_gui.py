import pyautogui
import keyboard
import json
import time
import os
import tkinter as tk
from tkinter import simpledialog

CONFIG_PATH = 'config.json'

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "mouse_clicks": [],
            "type_delay": 0.2,
            "paste_with_ctrl_v": True
        }

def save_config(cfg):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, indent=2)
    print("✅ 저장 완료:", CONFIG_PATH)

def ask_delay():
    root = tk.Tk()
    root.withdraw()
    try:
        delay = simpledialog.askfloat("지연 시간", "이 좌표 클릭 전 지연 시간(초):", minvalue=0.0)
        return delay if delay is not None else 0.5
    except:
        return 0.5

def main():
    print("🎯 좌표 저장 도우미 실행 중")
    print(" - [F8] → 현재 마우스 좌표 저장")
    print(" - [ESC] → 종료")

    config = load_config()

    while True:
        if keyboard.is_pressed('F8'):
            x, y = pyautogui.position()
            delay = ask_delay()
            print(f"📌 좌표 저장됨: x={x}, y={y}, delay={delay}s")

            config["mouse_clicks"].append({
                "x": x,
                "y": y,
                "delay": delay
            })

            save_config(config)
            time.sleep(1)

        if keyboard.is_pressed('esc'):
            print("👋 종료합니다.")
            break

if __name__ == "__main__":
    main()
