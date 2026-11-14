# Blue Ancient Debris

A Minecraft Java Edition resource pack that recolors Ancient Debris bright blue so it stands out against netherrack, basalt and blackstone.

**Supports:** 26.1 – 26.3 (resource pack formats 84 – 97).

## Install
1. Download `Blue-Ancient-Debris.zip` (or zip `pack.mcmeta`, `pack.png` and `assets/`).
2. Drop it into `.minecraft/resourcepacks/`.
3. Enable it in *Options → Resource Packs*.
4. If you use another ore pack (e.g. a glowing-ores pack), move this pack **above** it in the list so its block model and textures take priority.

## Rebuilding the textures
```
pip install pillow
python tools/recolor.py path/to/.minecraft/versions/26.2/26.2.jar
```
