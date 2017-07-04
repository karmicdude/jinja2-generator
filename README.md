# About

Simple script which generates the output file based on [Jinja2](http://jinja.pocoo.org/) template and config file


## Install
```bash
pip install -r requirements.txt
```

## Usage
```bash
./generate.py --help
./generate.py -c sample_config.ini -t dockerfile_template.j2 -o Dockerfile -s dev
```

## Example
```bash
# Sample config
[dev]
OS=debian:latest
MAINTAINER=User Name <user@example.com>
ARG1=azaza

[production]
OS=centos:latest
MAINTAINER=User Name <user@example.com>
ARG1=ouchouch
```

```bash
# Sample template
FROM {{ OS }}
MAINTAINER {{ MAINTAINER }}

ARG {{ ARG1 }}
```

```bash
# Output
FROM debian:latest
MAINTAINER User Name <user@example.com>

ARG azaza
```
