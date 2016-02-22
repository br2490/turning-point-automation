## LETS DEBUG THIS SHIT!
Debug.on(2)
# Settings.ObserveScanRate = 0.1

## configure our patterns.
poll_closed_no_response = Pattern("poll_closed_no_response.png").exact() # STEP 0, we need to open polling.
poll_opened_no_response = Pattern("poll_open_no_response.png").exact() # STEP 2, we need to wait for a response.
poll_opened_has_response = Pattern("poll_opened_has_response.png").exact() # STEP 3, we have a response, close polling.
poll_closed_has_response = Pattern("poll_closed_has_response.png").exact() # STEP 4 -> 1, saved response.


def weWatchAndWait(trigger):
    print(trigger)

def open_polling(trigger):
    print(trigger)

def do_nothing(trigger):
    print(trigger)

def close_polling(trigger):
    print(trigger)


def next_slide_and_poll(trigger):
    print(trigger)

if exists(poll_closed_no_response, FOREVER):
    print("Ready")
else:
    print("Not Ready")

onAppear(poll_closed_no_response, open_polling) # open polling

onAppear(poll_opened_no_response, do_nothing) # just wait...

onAppear(poll_opened_has_response, close_polling) # we've got a response, close polling

onAppear(poll_closed_has_response, next_slide_and_poll) # we have 1 response and polling is closed, next slide

observe(10)

# test = exists(poll_closed_has_response, FOREVER)
# print(test)