# About

Simple script which generates the output file based on Jinja2 template and config file


## Install
```bash
pip install -r requirements.txt
```

## Usage
```bash
./generate.py --help
./generate.py -c sample.config -t template.j2 -o Dockerfile -s dev

# Sample config
[dev]
OS=debian:latest
MAINTAINER=User Name <user@example.com>
ARG1=azaza

# Sample template
FROM {{ OS }}
MAINTAINER {{ MAINTAINER }}

ARG {{ ARG1 }}

# Output
FROM debian:latest
MAINTAINER User Name <user@example.com>

ARG azaza
```
