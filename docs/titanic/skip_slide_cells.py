from nbconvert.preprocessors import Preprocessor

class SkipSlideCellsPreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        slide_type = cell['metadata'].get('slideshow', {}).get('slide_type', '')
        if slide_type == 'fragment':
            cell['metadata']['attributes'] = cell['metadata'].get('attributes', '') + ' data-fragment'
        return cell, resources

    def preprocess(self, nb, resources):
        new_cells = []
        for cell in nb.cells:
            slide_type = cell['metadata'].get('slideshow', {}).get('slide_type', '')
            if slide_type != 'skip':
                new_cells.append(cell)
        nb.cells = new_cells
        return nb, resources