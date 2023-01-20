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



# Bot commands and examples


```!bot help``` - Brings up the help menu

```!bot check <dep> <num> <section>``` - Checks the GMU bookstore site for the textbook for the given fields. Example: !bot check ACCT 203 005

```!bot add <dep> <num> <section> <email> <sell> <rent>``` -Adds yourself as a seller of the textbook along with your price for renting and selling. Example: !bot add ACCT 203 005 netid@gmu.edu 49.95 5.99

<img width="516" alt="Screen Shot 2023-01-20 at 1 27 00 AM" src="https://user-images.githubusercontent.com/56946868/213634621-d2f80147-581a-4c8c-ab6c-a527710bb4b0.png">
<img width="502" alt="Screen Shot 2023-01-20 at 1 27 33 AM" src="https://user-images.githubusercontent.com/56946868/213634620-681f0cfd-d705-4f2f-9c49-103f0af24590.png">
<img width="468" alt="Screen Shot 2023-01-20 at 1 28 13 AM" src="https://user-images.githubusercontent.com/56946868/213634616-b09a1583-9d2d-4e71-8e08-7bb70d493e2e.png">
<img width="575" alt="Screen Shot 2023-01-20 at 1 49 27 AM" src="https://user-images.githubusercontent.com/56946868/213635024-c413be89-2297-443a-af80-4f968ffff56a.png">


