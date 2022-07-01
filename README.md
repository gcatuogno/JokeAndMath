# JokeAndMath

This is a small project that collects jokes from apis and does math calculations. Why not?

## Install.
  
  Windows
  py -m pip install -r requirements.txt 
  
  MacOS/Linux
  python -m pip install -r requirements.txt
  
## DataBase.

You need install and config postgreSQL, and and replace the values in the file "config.py".

## Testing.

After each test you must delete the database.


# Execution process.

First, analyze the responses of the supplied joke apis, once the endpoint was obtained, proceed to make the connection from Flask and return the joke as a response. After this, generate functions that perform the queries to each api separately and a function that generates the queries randomly. Also, in case of indicating the type of joke, I verify that the parameters are exactly the ones indicated "Chuck" and "Dad".

For the creation of new jokes, I generated a basic joke model, then I added the corresponding methods (POST, PUT, DEL) and configured them to receive the parameters as I needed.

With the mathematical part, the first thing was to find out if there was a function that would automatically calculate the LCM for me, once I found it, I applied it, performing the checks so that it only accepts integers. As for the addition method, I verify that the value I receive is a number and if so, the function is executed.

In the unit tests part, quick validations of each of the created functions are performed.
