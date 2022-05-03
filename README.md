# coltest

## Building

Tested in *Ubuntu 18.04.4 LTS*

### Backend

1. Generate virtual env

        python3 -m venv backend/virtual-env

2. Activate virtual env

        source backend/virtual-env/bin/activate

3. Install requirements

        pip install -r backend/requirements.txt

4. Run server

        PYTHONPATH=backend/ python3 backend/backend/main.py

### Frontend

1. Install dependencies

        (cd client/ && npm install)

2. Run client server

        (cd client/ && npm start)

## Testing

### Backend

        nosetests backend

### Frontend

        (cd client/ && npm run test)