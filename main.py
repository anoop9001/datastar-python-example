import os
import time
import uvicorn
import uuid
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, StreamingResponse

app = Starlette()

# index.html route - send html
@app.route('/')
async def homepage(request):
    index_page = f'''
        <!doctype html>
        <html>
        <head>
            <title> Datastar </title>
            <script type="module" src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.1/bundles/datastar.js"></script>
        </head>
        <body style="background-color:#FFFFFF" data-signals-show="true">
            <h1> Datastar </h1>
            <h2> A live stream of random UUIDs sent from the server </h2>
            <div>
                <button data-on-click="$show=!$show">Show or Hide Live Stream</button>
                <div data-show="$show">
                    <span id="feed" data-on-load="@get('/feed')" style="font-size:30px;color:#0074D9"></span>
                </div>
            </div>
        </body>
        </html>
        '''
    return HTMLResponse(index_page)

# construct and send message
def send_event(fragment, merge=False):
    yield 'event: datastar-merge-fragments\n'
    if merge:
        yield 'data: mergeMode upsertAttributes\n'
    yield f'data: fragments {fragment}\n\n'
    

# what the stream should send
def send_stream():
    while True:
        # generate random uuid
        random_id = uuid.uuid4()
        # send the html fragment that gets added to the page every second
        fragment = f'<div id="feed"> <p id="feed_uuid" style="font-size:30px;color:#0074D9"> {random_id} </p> <p id="feed_time"> {time.ctime()} </p> </div>'
        yield from send_event(fragment)
        time.sleep(1)
        

# the SSE stream
@app.route('/feed')
async def feed(request):
    return StreamingResponse(
            send_stream(),
            headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
            media_type="text/event-stream"
        )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)