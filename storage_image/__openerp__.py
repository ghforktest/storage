# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Storage Image",
    "summary": "Store image and resized image in a storage backend",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "website": "www.akretion.com",
    "author": " Akretion",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "storage_file",
        "base",
        'product',
    ],
    "data": [
        'views/storage_thumbnail_view.xml',
        'views/storage_image_view.xml',
        'views/partner.xml',
        'views/product.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
