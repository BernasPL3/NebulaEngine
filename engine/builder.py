from exporters.android import build_android
from exporters.ios import build_ios
from exporters.n3ds import build_3ds

def build_project(platform):
    print(f"[NEBULA] Build iniciada para: {platform}")

    if platform == "android":
        build_android()

    elif platform == "ios":
        build_ios()

    elif platform == "3ds":
        build_3ds()

    elif platform == "all":
        build_android()
        build_ios()
        build_3ds()

    else:
        print("Plataforma não suportada")
