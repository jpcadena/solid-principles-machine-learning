# solid-principles-machine-learning

## Solid Principles applied to Machine Learning project in Python

SOLID is an acronym for the first five object-oriented design (OOD) principles
by Robert C. Martin (also known as Uncle Bob).

These principles establish practices that lend to developing software with
considerations for maintaining and extending as the project grows. Adopting
these practices can also contribute to avoiding code smells, refactoring code,
and Agile or Adaptive software development.

SOLID stands for:

S - Single-responsibility Principle
O - Open-closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle

![SOLID Principles](https://miro.medium.com/max/1200/1*li4XFQoUyRq4TGbu0Tm1bQ.jpeg)

### Requirements

Python 3.10+

### Git

+ First, clone repository:

```
git clone https://github.com/jpcadena/solid-principles-machine-learning.git
```

+ Change directory to root project with:

```
  cd solid-principles-machine-learning
```

+ Create your git branch with the following:

```
git checkout -b <new_branch>
```

For *<new_branch>* use some convention as following:

```
yourgithubusername
```

Or if some work in progress (WIP) or bug shows up, you can use:

```
yourgithubusername_feature
```

+ Switch to your branch:

```
git checkout <new_branch>
```

+ **Before** you start working on some section, retrieve the latest changes
  with:

```
git pull
```

+ Add your new files and changes:

```
git add .
```

+ Make your commit with a reference message about the fix/changes.

```
git commit -m "Commit message"
```

+ First push for remote branch:

```
git push --set-upstream origin <new_branch>
```

+ Latter pushes:

```
git push origin
```

### Environment

+ Create a **virtual environment** 'sample_venv' with:

```
python3 -m venv sample_venv
```

+ Activate environment in Windows with:

```
.\sample_venv\Scripts\activate
```

+ Or with Unix or Mac:

```
source sample_venv/bin/activate
```

### Installation of libraries and dependencies

```
pip install -r requirements.txt
```

### Execution

```
python main.py
```

### Environment credentials

Rename **sample.env** to **.env** and replace your credentials.

### Documentation

Use docstrings with **reStructuredText** format by adding triple double quotes
**"""** after function definition.\
Add a brief function description, also for the parameters including the return
value and its corresponding data type.

### Additional information

If you want to give more style and a better format to this README.md file,
check documentation
at [GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).\
Please use **linting** to check your code quality
following [PEP 8](https://peps.python.org/pep-0008/). Check documentation
for [Visual Studio Code](https://code.visualstudio.com/docs/python/linting#_run-linting)
or
for [Jetbrains Pycharm](https://github.com/leinardi/pylint-pycharm/blob/master/README.md).\
Recommended plugin for
autocompletion: [Tabnine](https://www.tabnine.com/install)
