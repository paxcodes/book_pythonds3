# Problem Solving with Algorithms and Data Structures using Python

By Brad Miller and David Ranum, Luther College.

Textbook provided for free by [Runestone Academy](https://runestone.academy/runestone/books/published/pythonds3/index.html). Consider [supporting them](https://runestone.academy/runestone/default/donate).

## Project Setup

### Jupyter Notebooks (*.ipynb files)

If you don't yet have an environment to run jupyter notebooks, you may choose to install `miniconda`. You can follow the instructions from [Vancouver DataJam](https://jenfly.github.io/datajam-python/SETUP) which will include installing the libraries needed for some of my solutions to the exercises (e.g. `pandas`, `matplotlib`).

After `conda` is installed, terminals will have the conda base environment activated by default. To disable this behaviour, run `conda config --set auto_activate_base false`.

#### Opening the Jupyter Notebooks

1. Activate the conda base environment, if not yet activated: `conda activate`
2. Run `jupyter notebook`
3. Navigate to the location of the notebook you want to open!
    - Searching the internet for `jupyter notebook basics` will give you lots of resources to get started on Jupyter notebooks.
4. When you're done, press `Control-C` to stop the notebook server
5. Deactivate conda: `conda deactivate`

### Virtual Environment

You don't need to use virtual environments to run the solutions as long as you have python paths set up, and the necessary packages installed (e.g. `pytest` if you are interested in running the tests)

I'm using a virtual environment because I prefer not to use a global installation of [pytest](https://docs.pytest.org/en/stable/contents.html), which is what I use to run my tests.

#### Workflow with the Virtual Environment

1. Create a virtual environment: `virtualenv --prompt "(pythonds3) " .venv

2. Activate environment: `source .venv/bin/activate`

3. pip-install all the things
   - `pip install [package]` OR
   - `pip install -r requirements.txt`

4. (noting for my own sake) After installing new packages, export current environment configuration file: `pip freeze > requirements.txt` 

4. Deactivate environment: `deactivate`

### Tests

I use [pytest](https://docs.pytest.org/en/stable/contents.html) to run my tests. 

![sample test](./_assets/sample_test.png)
