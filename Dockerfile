FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir numpy==1.26.4

CMD ["python", "-c", "import numpy as np; print('Doubled:', np.array([1, 2, 3]) * 2)"]