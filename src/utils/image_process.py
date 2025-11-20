import os
import base64

import aiofiles

from utils.exceptions import ImageEncodeError

async def encode_image(image_path: str, prefix_path: str = ""):
    tmp_image_path = os.path.join(prefix_path, image_path)
    if not os.path.exists(tmp_image_path):
        raise FileExistsError(tmp_image_path)
    try:
        async with aiofiles.open(tmp_image_path, "rb") as image_file:
            image_data = await image_file.read()
            return base64.b64encode(image_data).decode('utf-8')
    except:
        raise ImageEncodeError(tmp_image_path)