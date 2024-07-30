import urllib.request
import gzip
import os

def download_and_extract_xmltv(url, output_file):
    response = urllib.request.urlopen(url)
    if url.endswith('.gz'):
        with gzip.open(response, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                f_out.write(f_in.read())
    else:
        with open(output_file, 'wb') as f_out:
            f_out.write(response.read())

def main():
    url = 'http://m3u4u.com/epg/jq2zy9v62gfw9x37nxr5'
    output_file = 'guide.xml'
    download_and_extract_xmltv(url, output_file)
    os.system(f'git add {output_file}')
    os.system('git commit -m "Update XMLTV file"')
    os.system('git push')

if __name__ == "__main__":
    main()