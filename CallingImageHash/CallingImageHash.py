from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.Open(''))
