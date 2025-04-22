#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main for inquire based learning slide generator

@author: chrvt
"""
import os
import json
import pathlib
from pathlib import Path
import pdb  # noqa
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import configargparse
from dotenv import load_dotenv, find_dotenv

# paths
from src.project_paths import (LITERATURE_PATH,
                           DATA_PATH,
                           CONFIG_PATH,
                           RESULTS_PATH,
                           LOGGER_CONFIG_PATH,
                           )
# LLM
from langchain_community.chat_models import ChatOpenAI

from src.classes import GrundrissHandler
from src.tools import PymupdfFigureHandler
import warnings
import logging

import logging.config
logging.config.fileConfig(LOGGER_CONFIG_PATH)
logger = logging.getLogger("Script")

warnings.filterwarnings("ignore")

# gpt-4-32k-0613
LLM = ["gpt-4o-2024-05-13",
       "gpt-4-1106-preview",
       "gpt-3.5-turbo-1106",
       "gpt-3.5-turbo-0613"]

def parse_args():
    """Parses command line arguments for the training."""

    parser = configargparse.ArgumentParser()

    # What what what
    parser.add_argument("--dir", type=str,
                        default="/Users/chrvt/Documents/Python"
                                "/NLP/IQL_generator/IQL/IQL",
                        help="Base directory of repo")
    parser.add_argument("--tag",
                        type=str,
                        default="",
                        help="Adds tag to module folder.")
    parser.add_argument("--debug",
                        action="store_true",
                        help="Debug mode (more log output, "
                             "additional callbacks)")

    # LLM settings
    parser.add_argument("--model",
                        type=str,
                        default="gpt-3.5-turbo-0613",
                        choices=LLM,
                        help="Which LLM-model to use?")
    parser.add_argument("--temperature",
                        type=float,
                        default=0.2,
                        help="Default LLM temperature "
                             "(degree of creativity or so).")

    args = parser.parse_args()
    return args

from langchain_ollama import ChatOllama
def analyse_grundriss():
    args = parse_args()

    # define LLM
    llm = ChatOllama(model="llama3.2", temperature=0)

        # ChatOpenAI(model_name=args.model, temperature=args.temperature))


    grundriss_handler = GrundrissHandler(llm)

    # file_path = r'/Users/christian.horvat@fhnw.ch/Documents/2D_3D/plan_handler/pdf_handler/plans/04_EFH PW_1-50_Umbau/cropped_pdfs/grundriss_cropped.pdf'
    file_path = (r'/Users/christian.horvat@fhnw.ch/Documents/2D_3D/plan_handler/pdf_handler/plans/annot/04_EFH PW_1-50_Umbau/cropped_pdfs/grundriss/'
                 r'1_cropped.pdf')

    grundriss_handler.detect_interior_exterior(file_path)
    answer = grundriss_handler.analyse_text_in_page(file_path)

    pdb.set_trace()

    return answer


if __name__ == "__main__":
    # load OpenAI key
    load_dotenv(find_dotenv(CONFIG_PATH / "openai.env"))
    crop = False
    if crop:
        base_path = r"/Users/christian.horvat@fhnw.ch/Documents/2D_3D/plan_handler/pdf_handler/plans/annot/04_EFH PW_1-50_Umbau"
        pdf_name = r'Alle Pläne BE'
        file_path = os.path.join(base_path,pdf_name+".pdf")
        # create cropped PDFs
        pdf_hadler = PymupdfFigureHandler()
        pdf_hadler.crop_pdf_based_on_boxes_and_labels(file_path, pdf_name, {})

    analyse_grundriss()
