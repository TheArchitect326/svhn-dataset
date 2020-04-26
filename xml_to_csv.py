import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path, adj=0):
    xml_list = []
    print(path)
    print(os.path.exists(path))
    for xml_file in glob.glob(os.path.join(path, '*.xml')):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (str(int(root.find('filename').text.split('.')[0]) + adj) + '.png',
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[1][0].text),
                     int(member[1][1].text),
                     int(member[1][2].text),
                     int(member[1][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for c, i in enumerate(['test', 'train']):
        image_path = os.path.join(os.getcwd(), 'annotations/{}'.format(i))
        print(image_path)
        xml_df = xml_to_csv(image_path, c * 33402)
        xml_df.to_csv('data/{}_labels.csv'.format(i), index=None)

    print('Successfully converted xml to csv.')


main()