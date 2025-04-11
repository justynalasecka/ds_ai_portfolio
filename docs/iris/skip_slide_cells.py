from nbconvert.preprocessors import Preprocessor

class SkipSlideCellsPreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        slide_type = cell['metadata'].get('slideshow', {}).get('slide_type', '')
        if slide_type == 'skip':
            cell['source'] = ''
            cell['outputs'] = []
        elif slide_type == 'fragment':
            pass # zachowaj komórkę
        else:
            pass # zachowaj komórkę
        return cell, resources