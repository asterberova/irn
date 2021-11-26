import os
import numpy as np
from PIL import Image
import xml.etree.cElementTree as ET

def print_annotation_xml(file_path, file_name, output_path):

    """
    <root>
        <doc>
            <field1 name="blah">some value1</field1>
            <field2 name="asdfasd">some vlaue2</field2>
        </doc>
    </root>

    """
    im = Image.open(os.path.join(file_path, file_name))
    imarray = np.array(im)

    annotation = ET.Element('annotation')

    folder = ET.SubElement(annotation, 'folder').text = file_path
    file_name = ET.SubElement(annotation, 'filename').text = file_name
    source = ET.SubElement(annotation, 'source')

    database = ET.SubElement(source, 'database').text = 'Cell data'
    annotation_source = ET.SubElement(source, 'annotation').text = '...'
    image = ET.SubElement(source, 'image').text = '...'

    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width').text = str(imarray.shape[0])
    height = ET.SubElement(size, 'height').text = str(imarray.shape[1])
    depth = ET.SubElement(size, 'depth').text = str(1)   #TODO

    segmented = ET.SubElement(annotation, 'segmented').text = str(0)
    object = ET.SubElement(annotation, 'object')
    obj_name = ET.SubElement(object, 'name').text = 'cell'

    tree = ET.ElementTree(annotation)
    file_name = os.path.splitext(file_name)[0]
    tree.write(os.path.join(output_path, file_name+'.xml'))



if __name__ == "__main__":

    file_path = 'data_cy3'
    output_path = 'annotation'

    # prepare directory for annotation
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)
    #
    # for filename in os.listdir(file_path):
    #     print_annotation_xml(file_path, filename, output_path)

    lists = ['train.txt', 'train_aug.txt', 'val.txt', 'test.txt']
    for l in lists:
        a = open(l, 'w')
        for filename in os.listdir(file_path):
            a.write(str(filename) + os.linesep)


