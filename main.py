from src.tools import PdfHandler
from src.tools import FigureHandler
from src.tools.text_handler import TextHandler()
import os


if __name__ == "__main__":

    file_path = r"/Users/christian.horvat@fhnw.ch/Documents/2D_3D/plan_handler/pdf_handler/plans/04_EFH PW_1-50_Umbau"

    figure_handler = FigureHandler()
    text_handler = TextHandler()
    pdf_handler = PdfHandler(file_path,
                             figure_handler=figure_handler,
                             text_handler=text_handler)

    #### STEP 1
    # Creating PNG folder of PDF pages
    figure_handler.convert_pdf(file_path)

    #### STEP 2
    # TODO: Automatic Segmentation of PNG images
    image_path = os.path.join(file_path,"pdf_to_image")
    """ Loops through each image in pdf_to_image folder and creates
        label_me type .json output
        png_segmenter.segment_images(imaga_path)
    """


    ### STEP 3 inverse segmentation
    """
        Based on .json files, we create a folder for each class
        Each folder consists of cropped version of original PDF        
    """

    figure_handler.crop_pdf_based_on_boxes_and_labels(image_path)
