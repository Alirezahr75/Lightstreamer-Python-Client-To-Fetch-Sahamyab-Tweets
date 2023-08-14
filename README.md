# Lightstreamer-Python-Client
This project contains a Python script that fetch data from lightstreamer socket.

## Installation
Install lightstreamer_client using pip:

```bash
pip install lightstreamer-client
```

## Lightstreamer Client Object
```bash
LightstreamerClient(user, pass, "server_address", "adapter_set")

user: Lightstreamer username (None by default)
pass: Lightstreamer password (None by default)
server_address: The address of the Lightstreamer Server to which this LightstreamerClient will connect to.
adapter_set: The name of the Adapter Set mounted on Lightstreamer Server to be used to handle all requests in the Session associated with this LightstreamerClient.

Note: The "adapter_set" value could be find in .js files.
```

## Lightstreamer LightstreamerSubscription Object
```bash
LightstreamerSubscription(mode, items, fields, adapter)

mode: The subscription mode for the items, required by Lightstreamer Server. Permitted values are: [MERGE, DISTINCT, RAW, COMMAND]
items: An array of Strings containing a list of items to be subscribed to through the server. For example an item in Lightstreamer could represent an item on eBay, say, a pair of "Nike Air Jordan" shoes.
fields: An array of Strings containing a list of fields for the items to be subscribed to through Lightstreamer Server.
adapter: The Data Adapter name is configured on the server side through the "name" attribute of the "data_provider" element.

Note: The "adapter" value could be find in .js files.
```
