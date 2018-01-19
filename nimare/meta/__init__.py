# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Top-level namespace for meta-analyses.
"""

from .cbma import ALE, SCALE, MKDA
from .ibma import (MFX_GLM, RFX_GLM, FFX_GLM, Stouffers, StouffersRFX,
                   WeightedStouffers, Fishers)
