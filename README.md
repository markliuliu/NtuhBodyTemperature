# NTUH Body Temperature
This repo is used to fill the body temperature form automatically.

# How to run?
## 1. settings.yaml
add `resource/settings.yaml`
```yaml
base_url: https://rc2.ntuh.gov.tw/surveys/?sq=
queue:
  - XXXXXXXXXX (replace with your's)
```
## 2. Setup for your env
Support `Windows` and run in `Docker`, recommend you to run this in docker, it trys to fill the form every 30 minutes, 
but windows will be easier to test.  

#### in windows
1. install python3
2. download selenium `chromedriver.exe` ([link](https://chromedriver.chromium.org/downloads)), put it in `resource/` folder 
3. **(Optional)** create a venv
4. pip install -r requirements.txt
5. python src/main.py
#### in docker
1. install docker and docker compose
1. dokcer-compose up