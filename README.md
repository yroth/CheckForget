# CheckForget

To install oTree look [here](https://otree.readthedocs.io/en/latest/install-macos.html#install-macos)


1. Create "oTree" folder with basic settings and apps examples
```
otree startproject oTree
```

2. Go to oTree folder
```
cd oTree
```

3. To start a new app called **lottery** run
```
otree startapp lottery
```
A folder "lottery" will be created with auto-generated files

4. Replace `models.py`, `pages.py` with files from this repository

5. Replace `templates/lottery` with folder from this repository

6. Copy to the root folder `test-problems.csv` from this repository

7. Update in `settings.py`
```
SESSION_CONFIGS = [dict(
  name='lottery',
  num_demo_participants=3,
  app_sequence=['lottery']
)]
```

8. Run the project
```
otree devserver
```
