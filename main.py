import api
import distance
import machine
import time
import urequests


# initialize count from zero
count = 0

# initialize api key
key = api.API_KEY

try:
    while True:
        dist = distance.get_distance()
        dist_str = str(dist)
        if ((dist >= 10) and (dist <= 50)):
            print(dist_str)
            count += 1
            print(count)
            sensordata = {'value1': dist_str[:-3], 'value2': count}
            print(sensordata)
            request_headers = {'Content-Type': 'application/json'}
            request = urequests.post(
                'http://maker.ifttt.com/trigger/dog_is_drinking/with/key/' + key,
                json=sensordata,
                headers=request_headers
            )
            print(request.text)
            request.close()
        else:
            pass

        time.sleep(8)

except KeyboardInterrupt:
    pass
# except OSError as e:
    #print('Failed to read/publish sensor readings')
