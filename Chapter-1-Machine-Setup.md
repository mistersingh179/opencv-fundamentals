# Machine Setup

Reference: https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/

## Install Python @ System level

Ensure that you have Python 3.X.X & get pip

```python
python3 -V # 3.7.7
sudo python3 get-pip.py
brew switch python 3.7.7
```

A Common issue is an SSL issue where it needs openSSL and not openSSL@1.1: 

```python
brew uninstall --ignore-dependencies openssl
brew install https://github.com/tebelorg/Tump/releases/download/v1.0.0/openssl.rb
```



## Setup `Pyenv` to manage Python at System Level

```bsah
brew update
brew install pyenv
```



It uses shims in the `PATH` directory to intercept and handle commands

```bash
echo $PATH

# /usr/local/Cellar/pyenv-virtualenv/1.1.5/shims:/Users/sandeeparneja/.pyenv/shims
```



It is installed in the versions dorectory as : `$(pyenv root)/versions.3.7.6`, `$(pyenv root)/versions.3.7.7` etc

Python version can be setup from:

- `PYENV_VERSION` env variable
- `.python-version` in the current directory or parent directories
- `pyenv` global version file – `$(pyenv root)/version`



## Setuup `pyenv-virtualenv` to manage various site-packages

```bash
pyenv virtualenv my-real-python-project-3.6.5 # creates a virtualenv
pyenv activate my-real-python-project-3.6.5 # uses it
echo "my-real-python-project-3.6.5" > .python-version # uses it when entering directory
```

Virtual subdirectories for the module are also placed under versions
```bash
~/.pyenv/versions/3.6.5/envs/my-real-python-project-3.6.5
```

## Instal OpenCV, Python, Pip, Numpy & Imutils



### Download, Compile & Install OpenCV



~~~python
```
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D PYTHON3_LIBRARY=`python -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
    -D PYTHON3_INCLUDE_DIR=`python -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
    -D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
```
~~~



### Symlink `cv2` from `/usr/local/lib` to `pyenv virtualenv`

Syntax: `ln -s source target`

here source is the existing file
and target is the name of the link or directory in which to place the link

In `.pyenv/versions/3.6.5/envs/my-real-python-project-3.6.5/lib/python3.6/site-packages`

```
ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.cpython-36m-darwin.so .pyenv/versions/3.6.5/envs/my-real-python-project-3.6.5/lib/python3.6/site-packages/cv2.so
```

This gives our virtualenv access to openCV which has been built and installed on the computer.
This is because when downloaded and built openCV it was install under /usr/local/lib.



