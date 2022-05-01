# coltest

## Building

Tested in *Ubuntu 18.04.4 LTS*

### Backend

1. Generate virtual env

        python3 -m venv backend/virtual-env

2. Activate previous virtual env

        source backend/virtual-env/bin/activate

3. Install requirements

        pip install -r backend/requirements.txt

4. Run server

        PYTHONPATH=backend/ python3 backend/backend/main.py

## Testing

### Backend

        nosetests backend