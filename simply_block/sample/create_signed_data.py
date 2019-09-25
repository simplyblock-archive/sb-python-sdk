from simply_block.simply_block.simply_sign import SimplySign

# Token
public_key = "hmac_pub_1"
private_key = "hmac_priv_1"

# Required Data
data = {"address": "0x00390f23598C7B01ea4ab5dA509c5495a32CFB03"}

# Sign
signed_data = SimplySign(private_key, public_key).generate_signature(data)

print(signed_data)