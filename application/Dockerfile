FROM python:alpine3.18

RUN apk add --no-cache build-base libpq-dev 

RUN addgroup -S app_group
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/app_user/" \
    --ingroup "app_group" \
    --no-create-home \
    --uid "1000" \
    "app_user"

USER app_user

WORKDIR /home/app_user/
ENV PATH="/home/app_user/.local/bin:${PATH}"

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "controller.main:app", "--reload", "--host", "0.0.0.0", "--app-dir", "app", "--log-level", "debug"]