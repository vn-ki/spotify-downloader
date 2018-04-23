from spotify_downloader.core import const
from spotify_downloader.core import handle
import spotify_downloader.spotdl as spotdl
import pytest


def load_defaults():
    const.args = handle.get_arguments(raw_args='', to_group=False, to_merge=False)
    const.args.overwrite = 'skip'
    const.args.log_level = 10

    spotdl.args = const.args
    spotdl.log = const.logzero.setup_logger(formatter=const._formatter,
                                      level=const.args.log_level)
