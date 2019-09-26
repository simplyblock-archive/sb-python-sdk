from simply_block.simply_sign import SimplySign

# Token
public_key = "hmac_pub_1"
private_key = "hmac_priv_1"

# Required Params
url = "http://127.0.0.1:8000/v1/eth/contract/build/"
file_path = "/home/lenovo/Documents/simplyblock/ethereum-service/contracts/DappToken.sol"
data = {
        'contract_name': 'contract_22'
}
files = {
    'contract': file_path
}
# Request
response = SimplySign(private_key, public_key).gateway_request(url, data, files=files)

print(response)
print(response.text)
