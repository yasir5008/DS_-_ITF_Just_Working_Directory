import zipfile
with zipfile.ZipFile("recap.zip","r") as zip_ref:
    zip_ref.extractall("")