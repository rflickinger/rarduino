# Raspberry Pi code and documentation

## Prerequisites
Hardware
- Raspberry pi X+ (I assume X is 3, but I'm unsure of the requirements at this time)
- Jumpers for connecting raspi and arduino

Apt Packages:
- python3.XX (Unsure, waiting to find all libraries for compatibility)
- pyserial

Python:
- Set up a venv to isolate packages and python version (probably not even going to do this eventually, if this pans out it'll be podman or k8s): `python3 -m venv garduino`
- Install pip requirements: `pip install -r requirements.txt`

Postgres:
- Install postgres (and yq) from apt `sudo apt install postgresql postgresql-contrib yq`
- Create a postgres service account. To do this, run `sudo userAdd postgres --shell=/sbin/nologin`
    - This should already be done when postgres is installed from apt
- Run the postgres install script `sudo ./postgres_install.sh`