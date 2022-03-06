import pyupbit

access = "YD38uw8t8nnEtTjqPoyTmNxIcVduLxFD1nx0chGY"          
secret = "JwoxM4qhMxCxx4PMzJWiVW7pZ0J2cwhWmTxBKn19"         
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-btc"))     #sibal
print(upbit.get_balance("KRW"))         #sibal
