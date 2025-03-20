FROM python:3.12-slim

RUN apt-get update

RUN apt-get install -y texlive-latex-base \
    texlive-latex-extra \
    texlive-latex-recommended \
    texlive-lang-cyrillic

RUN rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

COPY example_latex_generator/ ./example_latex_generator/

WORKDIR /app/example_latex_generator

RUN rm -rf dist && rm poetry.lock

RUN poetry lock && poetry install

CMD poetry run python example_latex_generator/main.py && \
    cd ../resources && \
    pdflatex example.tex && \
    rm example.tex && \
    rm example.aux && \
    rm example.log
