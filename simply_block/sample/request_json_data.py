from simply_block.simply_block.simply_sign import SimplySign

public_key = "hmac_pub_1"
private_key = "hmac_priv_1"

# Required Params
data = {"hash": "hash2"}
url = "https://testnet.simplyblock.io/v1/eth/verify_hash/"

# Request
response = SimplySign(private_key, public_key).gateway_request(url, data)

print(response)
print(response.text)