# nasa-apod

#### Creating PyPi package

1. python virtual environment for this project   

```
python3 -m venv venv
```

activate venv
```
source venv/bin/activate
```
2. project structure

    nasa-apod  

        nasa_apod  
            __init__.py  
            apod.py  
        .gitignore  
        README.md  
        setup.py  
        pyproject.toml  

 3. Packaging

    install required packages to create pypi package 

    ```
    pip install setuptools --upgrade
    pip install wheel
    pip install twine
    ```
    build distribution package 

    ```
    python3 setup.py sdist
    ```

    upload to pypi

    ```
    twine upload dist/*
    ```


#### installing package 
pip install nasa_apod

#### export you NASA API KEY   to env
store your NASA_API_KEY  in  .env  file , and make sure  you add .env to  .gitignore file.

e.g  
NASA_API_KEY=Your NASA API KEY

#### usage

```
from nasa_apod import apod
import os

# Load environment variables from .env file
load_dotenv()

# Read API key from environment variable
api_key = os.getenv('NASA_API_KEY')

if api_key:
    # Initialize APODService with API key
    apod_service = apod.APODService(api_key)
    
    # Get today's picture
    picture_data = apod_service.get_picture()
    print(picture_data)
else:
    print("NASA_API_KEY environment variable not found.")

```

