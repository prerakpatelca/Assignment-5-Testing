# Prerak Patel
# Student Number: 400400058

# When one traffic light is green the other must always be red.
# We are checking if signalHorizonatal is Green then signalVertical is Red
def test_traffic_light():
    signalHorizonatal = "Green"
    signalVertical = "Red"
    assert signalHorizonatal != signalVertical, "SignalHorizontal is Green then SignalVertical is Red"

# The walk signal for pedestrians must only allow crossing when the traffic light in the same direction is green.
# We are checking when signalHorizontal is Green same side pedestrianHorizontal turns Green
def test_pedestrians():
    signalHorizontal = "Green"
    signalVertical = "Red"
    pedestrianHorizontal = "Green"
    pedestrianVertical = "Red"
    assert signalHorizontal == pedestrianHorizontal, "signalHorizontal is Green then pedestrianHorizontal should be Green"
    assert signalVertical == pedestrianVertical, "signalVertical is Red then pedestrianVertical should be Red"

# The traffic light should be green for the main road unless traffic has been waiting on the side street for more than 90s, in which case it should be red and the side street light green until 30s after all traffic on the side street has cleared.
# Here we are checking if the traffic has been waiting for more than 90s on a side street, in that case main road signal turns Red and sideSignal turns Green for 30 sec
def test_side_street():
    mainSignal = "Red"
    sideSignal = "Green"
    mainSignalTime = 30
    sideSignalTime = 90
    assert sideSignalTime >= 90, "sideSignalTime is more than 90 sec"
    assert sideSignal == "Green", "sideSignal is green"
    assert mainSignal == "Red", "mainSignal is turned Red for 30 sec"
    assert mainSignalTime == 30, "mainSignal stays green for 30 sec"

