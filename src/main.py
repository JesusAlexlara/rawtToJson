import json, io
import glob, os

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

path = 'raw_files/'


def main():
    datos = {}
    cont = 0
    cout_line = 0
    while cont < 100:
        cout_line = 0
        strNum = str(cont).zfill(2)
        pathNameFile = path + 'u_' + strNum + '.dat'
        raw_file = open(pathNameFile, 'r')
        if cont == 0:
            for line in raw_file.readlines():
                line = line.replace(' ', '').replace('\n', '')
                data = line.split(',')
                strName = 'nodo_{}'.format(cout_line)
                datos[strName] = {}

                ptrDatos = datos[strName]

                ptrDatos['coord'] = data[0:3]
                ptrDatos['edos'] = []
                ptrDatos['edos'].append(data[3])
                cout_line = cout_line + 1
        else:
            for line in raw_file.readlines():
                line = line.replace(' ', '').replace('\n', '')
                data = line.split(',')
                strName = 'nodo_{}'.format(cout_line)
                ptrDatos = datos[strName]
                edos = ptrDatos['edos']
                edos.append(data[3])
                cout_line = cout_line + 1
        cont = cont + 1
        raw_file.close()

    with io.open('data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(datos,
                          indent=2, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))


if __name__ == '__main__':
    main()