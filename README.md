# Pytest Snippets
This repo contains example code snippets for using pytest. You can find the original article [here](https://www.scottcampit.com/pytest-for-test-driven-development/).

To run the tests, you need to have `pytest` installed. First, create a virtual environment in the repo and activate it. We'll name ours `pyetst-example` under the directory `.env`.

```bash
python3 -m venv .env/pytest-example
source .env/pytest-example/bin/activate
```

Next, install `pytest`.

```bash
pip3 install pytest
```

Finally, if you want to all files in the example (`tests/unit`), you can run:

```bash
pytest tests/unit
```

If you have any comments,  questions, or just want to say hi, please contact me at scottcampit@gmail.com.
