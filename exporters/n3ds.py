from engine.core import run_cmd

def build_3ds():
    print("[NEBULA] Build 3DS CIA")

    run_cmd("make")
    run_cmd("makerom -f cia -o game.cia -target t")

    print("[NEBULA] CIA gerado em build_output/")
