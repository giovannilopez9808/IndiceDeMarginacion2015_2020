import moviepy.video.io.ImageSequenceClip as Movie_maker
from os import system as terminal
from os import listdir as ls
from os.path import join


def create_animation(path: str, path_pictures: str, name: str, delete: bool, fps: int):
    """
    Funcion que ejecuta la creacion de la animacion
    """
    filenames = sorted(ls(path_pictures))
    filenames = [join(path_pictures, filename) for filename in filenames]
    output_file = "{}.mp4".format(name)
    output_file = join(path, output_file)
    movie = Movie_maker.ImageSequenceClip(filenames,
                                          with_mask=False,
                                          fps=fps,)
    movie.write_videofile(output_file,
                          logger=None)
    if delete:
        terminal("rm {}*.png".format(path_pictures))
