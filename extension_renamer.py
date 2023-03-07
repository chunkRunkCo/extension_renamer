import pathlib as pl

path: str = str(input("Enter full file path: "))
extension: str = str(input("Enter the name of the new extension (Ex: .txt): "))

for file in pl.Path(path).iterdir():
    file.rename(pl.Path(file).with_suffix(extension))
