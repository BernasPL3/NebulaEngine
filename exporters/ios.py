from engine.core import run_cmd

def build_ios():
    print("[NEBULA] Build iOS IPA")

    run_cmd("xcodebuild -scheme MyGame -configuration Release")

    print("[NEBULA] IPA precisa ser assinado manualmente ou via codesign")
