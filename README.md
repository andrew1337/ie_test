## It took around 3 hours to implement

###install requirement 
```bash 
pip3 install requirements.txt
``` 

###Load data
```bash 
python3 data_loader.py
```
Reading the CSV every day
```bash
(crontab -l 2>/dev/null; echo "0 12 * * *  /path/to/python3 data_loader.py") | crontab -
```
Storing the updated data in a DB

###Run server
```bash 
python3 server.py
```
API to get a list of products by a producer 
Offset & limit pagination  
```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/?limit=3&offset=5&producer=%and%
curl http://127.0.0.1:5000/?limit=10&offset=0&producer=%Gislas_n%
curl http://127.0.0.1:5000/?limit=3&offset=0&producer=Bashirian_%
```
