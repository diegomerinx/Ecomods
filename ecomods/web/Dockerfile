# Usa la imagen base de Python
FROM python:3.12.6

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código de tu aplicación
COPY . /app/

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando por defecto para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]