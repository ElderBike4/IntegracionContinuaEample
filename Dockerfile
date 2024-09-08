FROM node:14

WORKDIR /app

# Copiar el archivo package.json y package-lock.json primero
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el resto del código de la aplicación
COPY ./src /app

# Exponer el puerto en el que la aplicación escucha
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
