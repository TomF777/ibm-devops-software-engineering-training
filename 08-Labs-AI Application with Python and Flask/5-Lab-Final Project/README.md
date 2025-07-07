
```
cd ./xzceb-flask_eng_fr/final_project
```

Create a virtual enivronment:

```
pip install virtualenv
virtualenv virtualenv_name
source virtualenv_name/bin/activate         # for Linux
source virtualenv_name/Scripts/activate     # for Windows
```

Create folder named `machinetranslation` and change to that directory:

```
mkdir machinetranslation
cd machinetranslation
```
Check Python version:
```
python--version
```
Should be > `Python 3.8.0`

Install packages neede for this lab:
```
python -m pip install deep_translator
python -m pip install Flask
```
Go to the `machinetranslation` directory and create a new file called `translator.py`.

Add function `englishToFrench` which takes in the englishText as a string argument, in translator.py.

Add function `frenchToEnglish` which takes in the frenchText as a string argument, in translator.py.

### Write unit test for for English to French translator and French to English translator function in tests.py

Run tests:
```
python tests.py
```

### Package the above functions and tests as a standard Python package
Created in folder `tests`

### Endpoint implementation on server.py
Available under ./final_project/server.py