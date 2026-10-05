
# 0imports.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

init -1 python:
    # Gallery
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass