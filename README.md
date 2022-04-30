# book-bot
A bot that can pull textbooks from the GMU bookstore and allows users to sell their textbooks under the Discord interface.

To install and initialize a virtual environment follow these commands

Install
```pip install virtualenv```

Test Installation
```virtualenv --version```


Enter Root Project Directory
```cd book-bot```

Create virtual environment
```virtualenv env```

To start
```source env/bin/activate``` (For Mac)
```env\Scripts\Activate.ps1``` (For Windows)

Once in the virtual environment enter
```pip install -r requirements.txt``` to install system dependencies

Once the dependencies are installed and the env is activated you can run the app with 
```python3 app/app.py```
