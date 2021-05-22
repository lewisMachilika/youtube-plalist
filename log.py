import logging

#logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
def logs(videoname, url):
    #logging.basicConfig(filename='links.log', level = logging.WARNING,  filemode='a', format='%(message)s')
    #logging.warning(videoname  +" ["+url+"]." )


    logging.basicConfig(filename='links.log', encoding='utf-8', level=logging.DEBUG)

    logging.warning(videoname  +" ["+url+"]." )

if __name__ == '__main__': 
    logs('luja','man============')