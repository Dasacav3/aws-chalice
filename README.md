# Aws Chalice Lambda Function

This is an example of use about creation of aws lambda functions with python using chalice that is a microframework that allows create and REST API easy and quick.

## Requirements

You must have Python 3.7 or newer version.

## How to run

Remember put the values on the environment variables of the .config that is in .chalice folder.

Then you must execute the next commands in your terminal to run this project:

```bash
$ pip install chalice boto3
$ pip install -r requirements.txt
$ chalice local
```

## How to deploy chalice and create a lambda in aws

You have to execute the next commands:

```bash
$ pip install chalice boto3
$ pip install -r requirements.txt
$ chalice deploy --stage dev         # You can verify the name of the stages in .chalice/config.json file (dev, stable or prod)
```

