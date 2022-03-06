# Comics Project

Just a skeleton Django project I use as a starting point.

## Updating dependencies

Install pip-tools.

Run:

```shell
pip-compile --generate-hashes --upgrade --output-file=requirements.txt requirements.in
python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.txt && python -m pip install --upgrade -r requirements-dev.txt
```
