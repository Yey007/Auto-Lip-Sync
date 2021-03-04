To start out, install aeneas. Below are the simplest instructions, if you run into any trouble, check [here](https://github.com/readbeyond/aeneas)

### Windows

Download and run the latest installer for your os from [here](https://github.com/sillsdev/aeneas-installer/releases).

Download and install [Microsoft Visual C++ Build Tools](https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2019)

In anaconda:

Swap to python 3.7

```
conda create -n py37 python=3.7 anaconda
conda activate py37
pip install -r requirements.txt
```

Install dependencies:

```

pip install numpy lxml BeautifulSoup4
conda install setuptools -y --no-deps
conda install beautifulsoup4 -y --no-deps
conda install lxml -y --no-deps
conda install numpy
pip install aeneas
```



### Linux

Follow the instructions [here](https://github.com/readbeyond/aeneas/blob/master/wiki/INSTALL.md#linux)

