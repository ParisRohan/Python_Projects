from pathlib import Path

path=Path()
for file in path.glob(".vscode\*.py"):
    print(file)
