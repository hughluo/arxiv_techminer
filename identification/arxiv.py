# import urllib.request
# url = 'http://export.arxiv.org/api/query?search_query=all:machine+learning&start=0&max_results=100'
# data = urllib.request.urlopen(url).read()
# print(data)

import xml.etree.ElementTree as et


def xml2list(filename):
    tree = et.parse(filename)
    root = tree.getroot()
    summary = []
    title = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        t = entry.find('{http://www.w3.org/2005/Atom}title')
        s = entry.find('{http://www.w3.org/2005/Atom}summary')
        # del all '/n' to prepare for HLTA in future
        summary.append(s.text.replace('\n', ''))
        title.append(t.text)
    return summary, title


def list2txt(my_list, filename):
    with open(filename, 'w') as f:
        for item in my_list:
            f.write('{}\n'.format(item))


def file_lines(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def xml2txt(xml_filename, txt_filename):
    # drop title for now, it may help for further performance analysis though
    my_summary, _ = xml2list(xml_filename)
    list2txt(my_summary, txt_filename)
    print('Done. \n{} contains {} lines(documents).\n'.format(txt_filename, file_lines(txt_filename)))


def main():
    xml2txt('machine_learning.xml', 'machine_learning.txt')


if __name__ == '__main__':
    main()
