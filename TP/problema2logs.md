#Un servidor crea logs por cada acción que se realiza en él. El administrador desea
#un programa que todos los días borre todos los logs excepto si el log contiene la
#palabra "error"; si contiene esta palabra, se debe copiar el log al directorio "Errores"
#y se debe enviar un correo al administrador.

import os
import shutil
import smtplib

# Definir la ruta del directorio de logs y el directorio de errores
log_directory = "/ruta/al/directorio/de/logs"
error_directory = "/ruta/al/directorio/de/errores"

# Definir la palabra clave "error"
error_keyword = "error"

# Definir la dirección de correo electrónico del administrador
admin_email = "admin@ejemplo.com"

# Definir la función para enviar correos electrónicos
def send_email(subject, message):
    smtp_server = smtplib.SMTP("smtp.ejemplo.com", 587)
    smtp_server.starttls()
    smtp_server.login("usuario", "contraseña")
    email_message = "Subject: {}\n\n{}".format(subject, message)
    smtp_server.sendmail("admin@ejemplo.com", admin_email, email_message)
    smtp_server.quit()

# Definir la función para procesar los logs
def process_logs():
    # Obtener la lista de logs en el directorio
    log_list = os.listdir(log_directory)
    # Para cada log en la lista, hacer lo siguiente:
    for log_file in log_list:
        # Leer el contenido del archivo
        with open(os.path.join(log_directory, log_file), "r") as file:
            log_content = file.read()
        # Si el archivo contiene la palabra clave "error", entonces:
        if error_keyword in log_content:
            # Copiar el archivo al directorio de errores
            shutil.copy(os.path.join(log_directory, log_file), error_directory)
            # Enviar un correo electrónico al administrador con la información del error
            subject = "Error en el log"
            message = "Se encontró un error en el siguiente log:\n{}\n\n".format(log_file)
            message += "El contenido del log es:\n{}".format(log_content)
            send_email(subject, message)
        # Si el archivo no contiene la palabra clave "error", entonces:
        else:
            # Eliminar el archivo
            os.remove(os.path.join(log_directory, log_file))

# Definir el bucle principal
while True:
    process_logs()
    # Esperar 24 horas antes de volver a procesar los logs
    time.sleep(24 * 60 * 60)