FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN /bin/sh -c "cat requirements.txt"  
CMD ["/bin/sh"]  