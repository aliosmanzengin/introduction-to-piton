import image
from image import Pixel

import myconfıg

print(myconfıg.cfg)

for k, v in myconfıg.cfg.items():
    print(k, v)
img = image.Image("cy.png")
