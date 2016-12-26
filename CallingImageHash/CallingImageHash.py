import PIL.Image
from pprint import pprint as pp
import imagehash

hash1 = imagehash.dhash(PIL.Image.open('images/a.jpg'))
hash2 = imagehash.dhash(PIL.Image.open('images/b.jpg'))

print("hash1 = {}, hash2 = {}, hash1 - hash2 = {}".format(hash1, hash2, hash1 - hash2))

