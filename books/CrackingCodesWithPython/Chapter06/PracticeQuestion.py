# Break the following ciphertext one line at a time because each line has a different key.
# Remember to escape any quote characters
# SPOILER for chapter 7 (functions)


from books.CrackingCodesWithPython.Chapter01.caesarHacker import hackCaesar

ciphertext = ["qeFIP?eGSeECNNS,",
              "5coOMXXcoPSZIWoQI,",
              "avnl1olyD4l'ylDohww6DhzDjhuDil,",
              "z.GM?.cEQc. 70c.7KcKMKHA9AGFK,",
              "?MFYp2pPJJUpZSIJWpRdpMFY,",
              "ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K",
              "Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA"]  # ROFL

for line in ciphertext:
    print(hackCaesar(line))
    input("Press enter to continue\n")
