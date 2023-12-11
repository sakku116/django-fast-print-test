# Django product app practice

## Setup
- Buat virtual environment pada root directory dengan command:
    ```bash
    virtualenv venv
    ```
    >pastikan library virtualenv telah terinstall dengan cara `pip install virtualenv`
- Kemudian aktifkan virtual env yang telah dibuat:
    ```bash
    source venv/scripts/activate // windows bash
    // atau
    "venv/scripts/activate" // windows cmd
    ```
- Install semua requirements.
    ```bash
    pip install -r requirements.txt
    ```
- Buat file `.env` pada direktori `./fast_print_test`.
- Isi file `.env` dengan variable yang ada pada file `.env.example` dan sesuaikan nilai variablenya.
- Jalankan command:
    ```bash
    python manage.py migrate
    ```
- Jalankan data seeder dengan command:
    ```bash
    python manage.py seed_data
    ```
- Lalu jalankan server dengan command:
    ```bash
    python manage.py runserver
    ```
