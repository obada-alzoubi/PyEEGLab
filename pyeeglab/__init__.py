import logging

from mne.utils import set_config
from importlib.util import find_spec

from .dataset import TUHEEGCorpusDataset, TUHEEGCorpusLoader
from .database import File, Metadata
from .io import RawEDF
from .preprocessing import GraphGenerator, Preprocessor
from .text import TextMiner

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)

if find_spec('cupy') is not None:
    set_config('MNE_USE_CUDA', 'true')