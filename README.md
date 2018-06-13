

A command-line Python application which processes user inputs and stock market data from the [AlphaVantage API](https://www.alphavantage.co) to provide stock purchase recommendations.



Install package dependencies using one of the following commands, depending on how you have installed Python and how you are managing packages:

```sh
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

## Setup

Obtain an [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key), which the app will supply when issuing requests to the API.

To prevent your secret API Key from being tracked in version control, the application looks for an environment variable named `ALPHAVANTAGE_API_KEY`. To set this environment variable, create a new file in this directory called ".env" and place inside the following contents:

    ALPHAVANTAGE_API_KEY="abc123" # use your own API Key instead of "abc123"

## Usage

If you are using Pipenv, enter a new virtual environment (`pipenv shell`) before running any of the commands below.

Run the recommendation script:

```sh
# Homebrew-installed Python 3.x on Mac OS, not using Pipenv:
python3 app/roboadviser.py

# All others, including Pipenv on Mac or Windows:
python app/roboadviser.py
```

## Getting

If the dotenv approach is not working for you, please use the echo command, as I did, below:

# Mac Terminal:

echo $NYU_INFO_2335 #> SecretPassword123

# Windows Command Prompt:

echo %NYU_INFO_2335% #> SecretPassword123
To access environment variables from within a Python program, use the os module.

## Running

Once the application is complete, you can run the script

```sh
#Windows command
python roboadviser.py
```

## Outputs

As the application is running, please only input one stock symbol at a time. When you have finished inputting stock symbols, input 'Done'. The program will create a csv file for each valid symbol you have requested data for.

## References
Please not that a lot of the content from this readme was derived from Professor Rossetti's starter app

## [License](LICENSE.md)
