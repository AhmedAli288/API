# OCR & KNN algorithm API

**Pre-requisites**

1. Install Python
    ```shell script
    sudo apt install python3
    ```

1. Install virtual environment utility
    ```shell script
    sudo apt install python3-venv
    ```
1. Create a virtual environment
    ```shell script
     python3 -m venv venv
    ```

1. Setup an environment and run project (Activate virtual environment and install requirements and run development server)
    ```shell script
    source .env
    ```
**How to test OCR**

1. To test OCR use postman and run the python server by following command "python manage.py runserver".
2. After running server use URL "127.0.0.1:8000/api/ocr/" on the postman.
3. Set the postman setting to "POST", "Body", "binary" and pass an image having text in it.
4. The image is converted into the text.

**How to test KNN**

1. To test KNN use postman and run the python server by following command "python manage.py runserver".
2. After running server use URL "127.0.0.1:8000/api/iris/" on the postman.
3. Set the postman setting to "POST", "Body", "raw" & format "json".
4. Now pass values like following:
      {
          "SL": your_value,
          "SW": your_value,
          "PL": your_value,
          "PW": your_value
      }
5. Now send and see the results.
