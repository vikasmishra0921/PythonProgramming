import logging

logging.basicConfig(level=logging.INFO,
                    filemode ='w',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename = 'model.log',force= True)


logging.info("Hello world")