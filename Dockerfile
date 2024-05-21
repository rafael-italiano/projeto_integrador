FROM nginx:alpine

COPY /web /usr/nginx/html

EXPOSE 80