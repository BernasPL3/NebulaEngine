import os

PROJECT_PATH = "projects/my_game"

def run_cmd(cmd):
    print(f"[NEBULA] Executando: {cmd}")
    return os.system(cmd)
