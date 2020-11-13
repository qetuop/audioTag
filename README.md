# audioTag
audioTag

scans dir and subdirs for audio files and reads tags.  Outputs to csv file.

uses eyeD3
https://eyed3.readthedocs.io/en/latest/eyed3.html

### Setup
Ensure all system packages are installed for the version of python you are using ex:
```
sudo apt-get install python3
sudo apt-get install python3-venv
sudo apt-get install python3-dev
```

### Build
```
git clone https://github.com/qetuop/audioTag.git
cd REPONAME
python3 -m venv venv  
source venv/bin/activate
pip install -r requirements.txt

```

### Run
```python3 tag.py``` 
