# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import wificonf
import network

esp.osdebug(None)


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.connect(wificonf.WIFI_SSID, wificonf.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Network config: ', sta_if.ifconfig())


do_connect()
