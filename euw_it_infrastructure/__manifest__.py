# -*- coding: utf-8 -*-
{
    "name": "IT Infrastructure Manager",
    "version": "16.0.1.1.1",
    "summary": "Manage servers, network interfaces and DNS infrastructure by customer",
    "category": "Services/IT",
    "author": "Álvaro Martínez",
    "website": "https://eligeunaweb.es",
    "support": "soporte@eligeunaweb.com",
    "license": "LGPL-3",
    "price": 19.90,
    "currency": "EUR",
    "depends": ["contacts", "mail"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/server_views.xml",
        "views/dns_views.xml",
        "views/zone_views.xml",
        "views/partner_views.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "euw_it_infrastructure/static/src/css/infrastructure.css",
        ],
    },
    "images": ["static/description/banner.png"],
    "application": True,
    "installable": True,
}
