# data/coordinates.py
"""
Koordinatlar + Geocoding yardımcıları
- KOY_CONFIG: durak isimleri ve Google sorguları
- fetch_and_store_coordinates(api_key) -> KOY_CONFIG içine lat/lng ekler (hata korumalı)
- parse_coordinates() -> kesinlikle None dönmez, mantıklı default kullanır
- get_location_names() -> isim listesi
"""

import os
import requests

KOY_CONFIG = [
    {"name": "Isparta Merkez", "query": "Isparta Merkez"},
    {"name": "Sav", "query":"Sav Köyü, Isparta "},
    {"name": "Kuleönü", "query":"Kuleönü Köyü, Isparta "},
    {"name": "Deregümü", "query":"Deregümü Köyü, Isparta "},
    {"name": "Kadılar", "query":"Kadılar Köyü,Isparta "},
    {"name": "Senirce", "query":"Senirce Köyü, Isparta "},
    {"name": "Yakaören", "query":"Yakaören öyü, Isparta "},
    {"name": "Ayazmana", "query":"Ayazmana Köyü, Isparta "},
    {"name": "Küçük Hacılar", "query":"Küçük Hacılar Köyü, Isparta "},
    {"name": "Büyük Gökçeli", "query":"Büyük Gökçeli,Isparta "},
    {"name":"Bozanönü", "query":"Bozanönü Köyü,Isparta "},
    {"name": "Darı Deresi", "query":"Darı Deresi,Isparta "},
    {"name": "Direkli", "query":"Direkli Köyü,Isparta "},
    {"name": "Gelincik", "query":"Gelincik,Isparta "},
    {"name": "Aliköy", "query":"Aliköy Köyü,Isparta "},
    {"name": "Yukarıgökdere", "query":"Yukarıgökdere,Isparta "},
]

# Mantıklı default koordinat (Isparta merkezi)
DEFAULT_COORD = (37.7641, 30.5566)


def get_location_names():
    return [item["name"] for item in KOY_CONFIG]


def get_location_queries():
    return [item["query"] for item in KOY_CONFIG]


def geocode_place(query: str, api_key: str, language: str = "tr"):
    """Google Geocoding ile tek sorgunun lat,lng'sini döndürür. Hata durumunda default döner."""
    if not api_key:
        # API yoksa default döndür
        return DEFAULT_COORD

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": query, "key": api_key, "language": language}

    try:
        resp = requests.get(url, params=params, timeout=8)
        data = resp.json()
    except Exception:
        return DEFAULT_COORD

    if data.get("status") != "OK" or not data.get("results"):
        return DEFAULT_COORD

    loc = data["results"][0]["geometry"]["location"]
    return float(loc.get("lat", DEFAULT_COORD[0])), float(loc.get("lng", DEFAULT_COORD[1]))


def fetch_and_store_coordinates(api_key: str = None, force: bool = False):
    """
    KOY_CONFIG içine 'lat' ve 'lng' ekler.
    - api_key varsa Geocoding kullanır,
    - yoksa veya hata olursa DEFAULT_COORD atar.
    - force=True ise var olan lat/lng değerlerini yeniden yazar.
    """
    for item in KOY_CONFIG:
        if not force and ("lat" in item and "lng" in item and item["lat"] is not None and item["lng"] is not None):
            continue
        lat, lng = geocode_place(item["query"], api_key)
        item["lat"] = lat
        item["lng"] = lng


def parse_coordinates():
    """
    KOY_CONFIG'ten (lat,lng) tuple listesi döndürür.
    Kesinlikle None içermez; eksik durumda DEFAULT_COORD kullanır.
    """
    coords = []
    for item in KOY_CONFIG:
        lat = item.get("lat")
        lng = item.get("lng")
        if lat is None or lng is None:
            coords.append(DEFAULT_COORD)
        else:
            coords.append((float(lat), float(lng)))
    return coords
