import os
import shutil

def ordenar_descargas():
    for archivo in os.listdir("C:/Users/Alumno-14/Downloads"):
        if archivo.endswith((".doc", ".docx", ".txt", ".pdf", ".xls", ".ppt", ".xlsx", ".pptx")):
            shutil.move(f"C:/Users/Alumno-14/Downloads/{archivo}", "C:/Users/Alumno-14/Documents/doc_types/")
        elif archivo.endswith((".jpg", ".jpeg", ".png", ".svg", ".gif")):
            shutil.move(f"C:/Users/Alumno-14/Downloads/{archivo}", "C:/Users/Alumno-14/Documents/img_types")
        elif archivo.endswith((".exe", ".py", ".ipynb")):
            shutil.move(f"C:/Users/Alumno-14/Downloads/{archivo}", "C:/Users/Alumno-14/Documents/software_types/")
        else:
            shutil.move(f"C:/Users/Alumno-14/Downloads/{archivo}", "C:/Users/Alumno-14/Documents/others/")
    print("Tus archivos se han movido a Documentos")