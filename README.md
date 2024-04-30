# nasa-apod

#### 1. Creating PyPi package

    1.1 python virtual environment for this project   

    ```
    python3 -m venv venv
    ```

    1.2 activate venv

    ```
    source venv/bin/activate
    ```
    1.3 project structure

    nasa-apod  

        nasa_apod  
            __init__.py  
            apod.py  
        .gitignore  
        README.md  
        setup.py  
        pyproject.toml  

    1.4 Packaging

        install required packages to create pypi package 

        ```
        pip install setuptools --upgrade
        pip install wheel
        pip install twine
        ```
    1.5 Build distribution package 

        ```
        python3 setup.py sdist
        ```

    1.6 upload to pypi

        ```
        twine upload dist/*
        ```


#### 2. Installing & Using this package

    2.1 Installing this package 

    ```
    pip install nasa_apod
    ```
    2.2 Using this package

    export you NASA API KEY   to env  
    store your NASA_API_KEY  in  .env  file , and make sure  you add .env  to  .gitignore file.

    e.g   
    NASA_API_KEY=Your NASA API KEY  

    3.3 Usage

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

