import os
import sys
import random

listImages = os.environ.get('DOCKER_IMAGES')
if listImages is None or len(listImages) == 0:
    sys.exit("Docker images not found")
listImages = listImages.split(',')

print("Running Docker")
os.mkdir(os.path.join(os.getcwd(), "images"))
for i in listImages:
    randomString = ''.join(random.choice(
        'abcdefghijklmnopqrstuvwxyz') for i in range(10))

    with open(os.path.join(os.getcwd(), "images", randomString), "a+") as f:
        f.write(f"""
FROM {i}

RUN echo 'Hello World'
        """)

    os.system(f'cat {os.path.join(os.getcwd(), "images", randomString)}')  

    # generate random string
    os.system(f"docker build -t {randomString} -f ./images/{randomString} ./images")
    os.system("docker prune --all --force")
print("Docker Run Complete")
