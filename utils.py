from warnings import warn


def split_image(image):
    """Splits image in half"""

    if image.shape[1] % 2:
        warn("Warning: image has odd number of columns. Image split is not perfect.")

    image_1 = image[:, : int(image.shape[1] / 2)]
    image_2 = image[:, int(image.shape[1] / 2) :]

    return image_1, image_2

