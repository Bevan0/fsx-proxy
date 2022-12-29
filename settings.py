# This is the settings file for FSX Proxy.
# Just change the stuff in "quotes" or numbers.

# If you are having issues, enabling this will display the settings found by the proxy.
# If this is enabled and the configuration is not sent in the terminal,
# this means the proxy couldn't find the configuration.
PRINT_CONFIG = True

# The IPv4 address and port of FSX.
# The IP 127.0.0.1 means your own machine, and 6112 is the default port.
FSX_LINK = ("127.0.0.1", 6112)

# The IPv4 address of the server you want to connect to.
# If you can't find a specific port, 6112 (the FSX default) works fine.
SERVER_LINK = ("123.123.123.123", 12345)

# Usually, you should leave this value at its default value (16384).
# This controls the buffer size of the packets in bytes.
# If your game uses packets larger than 16kB (the default), this will cause issues.
BUFFER_SIZE = 16384

# This will print the raw packet data into the terminal.
# This might cause performance problems and is not recommended for everyone.
# Setting the value to False will disable this, otherwise set it to True to enable it.
PRINT_PACKETS = False

if PRINT_CONFIG:
    print("PRINT_CONFIG is enabled. Printing the configuration:")
    print(f"FSX IP: {FSX_LINK}")
    print(f"Server IP: {SERVER_LINK}")
    print(f"Buffer Size: {BUFFER_SIZE}")
    print(f"Print Packets: {PRINT_PACKETS}")