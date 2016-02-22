Debug.on(3)
# Settings.ObserveScanRate = 0.1

## configure our patterns.
# STEP 0, we need to open polling.
poll_closed_no_response = Pattern("poll_closed_no_response.png").exact() 
poll_closed_no_response_old = Pattern("poll_closed_no_response_old.png").exact()
poll_closed_no_response_zoom = Pattern("poll_closed_no_response_zoom.png").exact()
# STEP 2, we need to wait for a response.
poll_opened_no_response = Pattern("poll_open_no_response.png").exact() 
poll_open_no_response_old = Pattern("poll_open_no_response_old.png").exact()
poll_open_no_response_zoom = Pattern("poll_open_no_response_zoom.png").exact()
# STEP 3, we have a response, close polling.
poll_opened_has_response = Pattern("poll_opened_has_response.png").exact() 
poll_opened_has_response_old = Pattern("poll_opened_has_response_old.png").exact()
poll_opened_has_response_zoom = Pattern("poll_opened_has_response_zoom.png").exact()
# STEP 4 -> 1, saved response.
poll_closed_has_response = Pattern("poll_closed_has_response.png").exact() 
poll_closed_has_response_old = Pattern("poll_closed_has_response_old.png").exact()
poll_closed_has_response_zoom = Pattern("poll_closed_has_response_zoom.png").exact()

## This hotkey will both OPEN and CLOSE polling on Mac OSx.
def turning_point_hotkey():
    type("9", Key.ALT + Key.CMD)

## This will move PowerPoint forward one slide and trigger polling to reopen.
def next_slide_and_poll():
    print("next slide")

## First let's find the TurningPoint polling toolbar. This MATCH is saved as our region.
region = wait(poll_closed_no_response_zoom, FOREVER)
# Increase the speed at which we poll the region for changes. Where scanRate(n) is equal to queries per second.
region.setWaitScanRate(20)

## Open polling and wait for participant.
turning_point_hotkey()

# if exists(poll_closed_no_response_old, 10):
#     turning_point_hotkey()
#     wait(1)

# This is a SANITY check ~ we should se that polling is opened and waiting for input.
region = region.wait(poll_open_no_response_zoom, 10)
print("Waiting for input...")

# The participant has responded, wait, then close polling.
region = region.wait(poll_opened_has_response_zoom, FOREVER)
print("Participant has 1 second to change their answer")
sleep(10) # give the participant opportunity to change their response.
print("Participant no longer has time to change their answer.")
turning_point_hotkey()

if region.wait(poll_closed_has_response_zoom):
    print("WE HAVE A RESPONSE AND POLLING IS CLOSED!!!")
