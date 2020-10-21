import sys
import google_images_download.google_images_download as gid

path = sys.argv[1]
cfg = {
    'config_file': path
}

response = gid.googleimagesdownload()
paths = response.download(cfg)

print(paths)
