import sys
from engine.builder import build_project

def main():
    if len(sys.argv) < 3:
        print("Uso: nebula build <platform>")
        return

    command = sys.argv[1]
    platform = sys.argv[2]

    if command == "build":
        build_project(platform)
    else:
        print("Comando inválido")

if __name__ == "__main__":
    main()
