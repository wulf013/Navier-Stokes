#this a python script written by Enrique Castro
import logging #importing standard python logging
import log #importing my logging module, handles some basic calls
from NavierStokes import fluids

#boilerlate logging
log.setup_logging()
log = logging.getLogger(__name__)

def main():
    log.info('Navier-Stokes script running')
    fluids.execute()

if __name__ == "__main__":
    main()