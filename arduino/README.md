# Arduino code and documentation

Project was created by Platformio. Process for creating the project:
- Create vm at repo root `python3 -m venv <venv name>`
- Source the venv `source <venv name>/bin/activate`
- Install PlatformIO `python3 -m pip install platformio`
- Create project with platformio:
    - `platformio project init --board <board> --project-dir arduino`
    - To find the list of board names as recognized by platformio: `platformio boards arduino | grep <short board name>`
- Run with `pio run --target upload`