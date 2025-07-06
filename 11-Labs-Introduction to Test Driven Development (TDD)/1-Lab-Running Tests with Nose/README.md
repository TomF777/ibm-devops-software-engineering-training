```
cd duwjx-tdd_bdd_PracticeCode
```
```
cd labs/01_running_tests_with_nose/
```
### Unittest

Run test with unittest:
```
python3 -m unittest
```

Run test with more verbose output:
```
python3 -m unittest -v
```
### Working with Nose
```
pip install nose
```

```
nosetests -v
```

Adding color with Pinocchio:
```
pip install pinocchio
```

To get nicer formatting and a colorful output:
```
nosetests --with-spec --spec-color
```

Adding test coverage:
```
pip install coverage
```

```
nosetests --with-spec --spec-color --with-coverage
```

### Create missing coverage report
```
coverage report -m
```

### Automating test parameters
Up until now you have typed out a lot of command parameters when running tests with nose. Alternatively, you can save all the parameters in a configuration file `setup.cfg` so that you don’t have to type them in every time.

Run nosetests with config:
```
nosetests
```



