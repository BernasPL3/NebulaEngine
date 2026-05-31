from engine.core import run_cmd

def build_android():
    print("[NEBULA] Build Android APK")

    run_cmd("./gradlew assembleRelease")

    print("[NEBULA] APK gerado em app/build/outputs/")
