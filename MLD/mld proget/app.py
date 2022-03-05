import zipfile
with zipfile.ZipFile("mldproject.zip","r") as zip_ref:
    zip_ref.extractall("")