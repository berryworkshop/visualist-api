FROM nginx:1.13.1
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY visualist.conf /etc/nginx/conf.d/
