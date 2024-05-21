FROM nginx:alpine

COPY /web /usr/nginx/html

EXPOSE 8080
EXPOSE 80 