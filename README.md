# loadingLine

## Idea
A simple module that can be used to any loading moment or waiting moment

## Launch
Activation of the venv

```bash
python -m venv venv
source venv/bin/activate
```

To launch the demo
```bash
cd src
./__main__.py
```

or 
```bash
python src
```

To deactivate the venv : 
```bash
deactivate
```

## API

```python
import loadingLine

loadingLine.loading(currentPositoin, finalPositon, lineSize)
```
