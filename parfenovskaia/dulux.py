import requests
from pathlib import Path
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Tuple
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

@dataclass
class Color:

    name: str
    rgb: Tuple[int, int, int]
    href: str


class Dulux:
    COLORS_PAGE = 'https://colour.dulux.ca/all-colors'
    ROOT_PAGE = 'https://colour.dulux.ca'

    def __init__(self) -> None:
        self._colors_page_file = Path(__file__) \
            .parents[1] \
            .resolve() \
            .joinpath('colors_page.html')

    def _get_colors_page(self):
        response = requests.get(self.COLORS_PAGE)
        if response.status_code != 200:
            raise RuntimeError(response.text)
        return response.text

    def save_colors_page_file(self):
        self._colors_page_file.write_text(self._get_colors_page())

    def get_colors(self):
        if not self._colors_page_file.exists():
            self.save_colors_page_file()

        soup = BeautifulSoup(self._colors_page_file.read_text(), 'html.parser')
        a_colors = soup.findAll('a', class_='all-color-tile')
        colors = {}
        for color in a_colors:
            href = color['href']
            c_id = color['id']
            style = color['style']

            href = self.ROOT_PAGE + href
            name = c_id[5:]
            rgb = tuple(int(i) for i in style[21:-1].split(','))
            colors[rgb] = Color(name=name, rgb=rgb, href=href)
        return colors

    def get_color_difference(self, c1, c2):
        color1_rgb = sRGBColor(*c1)
        color2_rgb = sRGBColor(*c2)
        color1_lab = convert_color(color1_rgb, LabColor)
        color2_lab = convert_color(color2_rgb, LabColor)
        delta_e = delta_e_cie2000(color1_lab, color2_lab)
        return delta_e


    def find_best_color(self, color):
        colors = self.get_colors()

        distances = {}
        for c_rgb, c in colors.items():
            distances.setdefault(self.get_color_difference(c_rgb, color), []).append(c)

        min_distance = min(distances)
        return distances[min_distance]
