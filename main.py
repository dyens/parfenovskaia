
from parfenovskaia.dulux import Dulux
from pathlib import Path

dulux = Dulux()

# dulux.save_colors_page_file()


kaiku = (221, 231, 238)
ladylike = (199, 206, 222)
chablis = (235, 233, 193)
neva = (194, 195, 176)
huntu = (215, 219, 229)

print('kaiku', dulux.find_best_color(kaiku))
print('ladylike', dulux.find_best_color(ladylike))
print('chablis', dulux.find_best_color(chablis))
print('huntu', dulux.find_best_color(huntu))


# Tikkurila colors
# https://tikkurila.ru/dlya-professionalov/cveta/ekho-f351
# https://tikkurila.ru/dlya-professionalov/cveta/ledilayk-x348
# https://tikkurila.ru/dlya-professionalov/cveta/shabli-x388
# https://tikkurila.ru/dlya-professionalov/cveta/top-v446

# Delux colors 
# https://colour.dulux.ca/blues/first-frost
# https://colour.dulux.ca/purples/sweet-emily
# https://colour.dulux.ca/purples/orchid-whisper
# https://colour.dulux.ca/greens/oh-dahling
# https://colour.dulux.ca/greens/pine-crush
