# CSV2SQL
A handly python script which turns your csv dumps into SQL `INSERT` queries.

## Prerequisites
- Python installed. I am personally running `3.10.6`.
- `pip` installed compatible with the same python version as above.
- `venv` package will be run when creating virtual environments. If not, you will need to install it.

## How to use
- Clone the repo.
- Create a virtual env.
```
python -m venv venv
```
- Start the virtual environment (Unix or macos).
```
source venv/bin/activate
```
- If you are using windows, then run
```
venv\Scripts\activate.bat
```
This will now open a virtual environment. Next time you only need to start it, no need to create again.

- Install the required dependencies.
```
pip install -r requirements.txt
```
This will now install the required dependencies. This is a one time action.

- Now, Create a new folder called `data` in the root of the project. This folder will contain all your csv dumps from PhpMyAdmin/any other export. Make sure to name the file with the table name, case sensitive. Eg.-
```
data
├── comments.csv
├── posts.csv
├── users.csv
└── errors.csv
```

- At this point, your folder set up is done. One last configurational change is to open the config file at `src/config.py`. Here, you can add the below things:
  - The table name/name of the csv file.
  - The columns you want to ignore from the dump, like `id`, `created_at` which are mostly autogenerated from the DB.
  - Any rules. Like say for a column, you want to substitue `Doe` for every row which has the value `John`. The structure has to be strictly as per the existing sample. You may leave this field as an empty dictionary if you do not have such rules.

- Finally, run the script
```
python main.py
```

- After you're done, deactivate the virtual environment.
```
deactivate
```
