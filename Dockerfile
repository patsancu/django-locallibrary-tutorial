FROM python
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
