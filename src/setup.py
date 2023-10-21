import cx_Freeze

executables = [cx_Freeze.Executable("SpaceInvaders.py")]

cx_Freeze.setup(
    name = "Space Invaders",
    options = {"build_exe": {"packages": ["pygame", "random", "math"],
                             "include_files": ["ufo.png", "background.png", "background.wav", "space-invaders.png", "enemy.png", "bullet.png", "laser.wav", "explosion.wav"]}},
    executables = executables
    )
