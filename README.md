# Datastar & Python (Minimal Example)

[Datastar](https://data-star.dev/) is a Hypermedia library similar to [HTMX](https://htmx.org/) that uses Server Sent Events (SSE). [(See MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)

Datastar can be used to provide client side interaction as well as server side interaction in a way that allows for an experience that has aspects of server side rendering as well as client side rendering.

Any backend technology can be used to power a Datastar site. This example uses Python (Starlette & Uvicorn) as the backend. 

This repository contains a minimal example that can be cloned, installed and run. 

---
### Overview

- Clone the Repository
- Use the installer script to install required packages
- Use the run script to run the server
- Open your browser to http://localhost:3000

## Install

- These instructions are for Mac and Linux (see below for Windows)
- Once the repository has been cloned, open a terminal in the folder
- Add execute permissions to the installer script with
```
   chmod +x ./installer.sh
```
- Run the installer with
```
   ./installer.sh
```
- This will create a new virtual environment and install the dependencies
- Add execute permissions to the run script (one time only) with
```
   chmod +x ./run.sh
```

## Run

- Run the server with
```
   ./run.sh
```
- Open a browser window to http://localhost:3000 to try it out


---

## Windows

- Create a virtual environment
- Install the packages in requirements.txt
- Run the server with 
``` 
   python main.py
```
- Open a browser window to http://localhost:3000


