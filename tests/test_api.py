
def test_jpeg_status_code(my_api):
    jpeg_status_code = my_api.download_image("jpeg")
    assert jpeg_status_code == 200


def test_webp_status_code(my_api):
    webp_status_code = my_api.download_image("webp")
    assert webp_status_code == 200


def test_svg_status_code(my_api):
    svg_status_code = my_api.download_image("svg")
    assert svg_status_code == 200


def test_png_status_code(my_api):
    png_status_code = my_api.download_image("png")
    assert png_status_code == 200
