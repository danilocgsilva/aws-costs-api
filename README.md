# Api for analises the AWS Costs#

This script is created solely to be used by third party script, like [cli for fetching costs data](https://github.com/danilocgsilva/aws-costs-cli) from https://github.com/danilocgsilva/aws-costs-cli.


## Installation

Go to the project root folder. Then:
```
pip install .
```

## Usage

After you have installed your script in your environment, you will import in your own python script by:

```
from aws_costs_api.AWSCosts import AWSCosts
```
Go to [README.md](aws_costs_api/README.md) from api folder for more details.

## Storing results

The application is ready to save data in some storage. For this, you must provides the connection string when using `getCosts` from `AWSCosts` class. The available stores until now is SQLite and MySQL.

The connection string must obey the following format:

```
<connection_type>:<connection_string>
```

* `<connection_type>`: until now there are two types: `sqlite` or `mysql`.
* `<connection_string>`: is the connection string in the format required by the storage type. If the storage type is of type `sqlite`, them the script is just a local path to a file in the system, which will be ten file for sqlite. If the type os storage is `mysql`, then the connection string must be the credentials members upercased, having its value assigned by `=`, and separated by semicolon (`;`). Example:

```
USER=my_user_name;PASSWORD=the_secret_passowrd;HOST=database_host;DATABASE_NAME=the_database_name;PORT=the_port_which_is_optional
```
