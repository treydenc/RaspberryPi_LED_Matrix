# RpiGPT

(Name to be changed) Visualization of trajectories and correlations with self-report surveys with speech and language use from users. 

1. Download data and put it in empathic_stories/
2. `python encode_data.py` creates a vector and text db of the stories for a station
3. `python run_agent.py` runs a LLM agent on the db for queries

## Open two terminals
1. for the server (local)
2. for the client (local)

## Running the Server - Flask
In one of the terminals run the server

create a virtual environment:

``` bash
python -m venv venv
```
Activate the virtual environment:

On Windows (PowerShell):
``` bash
.\venv\Scripts\Activate.ps1
```

On Unix or MacOS:
```bash
source venv/bin/activate
```
Next, install the required Python packages:
```bash
pip install -r requirements.txt
```
Finally, run the server
```bash
python server.py
```